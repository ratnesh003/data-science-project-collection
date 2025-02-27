import json
import streamlit as st
from pathlib import Path
from utils.load_jsonl import load_data
from utils.code_services import format_code, execute_code

DATA_DIR = Path("data/questions")
JSONL_FILE = "output.jsonl"

questions_data = load_data(JSONL_FILE)

categories = sorted(set(q["metadata"]["category"] for q in questions_data))

st.title("✏️ Edit a Question")

if not categories:
    st.warning("No categories available.")
    st.stop()

selected_category = st.selectbox("Select a Category", categories)

filtered_questions = {int(q["folder"]): q["question"][:50] + "..." for q in questions_data if q["metadata"]["category"] == selected_category}

if not filtered_questions:
    st.warning("No questions found in this category.")
    st.stop()

selected_question_id = st.selectbox("Select Question to Edit", list(filtered_questions.keys()), format_func=lambda x: f"ID {x}: {filtered_questions[x]}")

selected_question = next((q for q in questions_data if int(q["folder"]) == selected_question_id), None)

if selected_question:
    question_input = st.text_area("Edit Question", value=selected_question["question"])
    answer_input = st.text_area("Edit Answer", value=selected_question["answer"])
    code_input = st.text_area("Edit Code", value=selected_question["code"])

    metadata = selected_question["metadata"]
    category_input = st.text_input("Category", value=metadata["category"])
    answer_category_input = st.text_input("Answer Category", value=metadata["answer_category"])
    plot_input = st.checkbox("Does this require a plot?", value=metadata["plot"])
    libraries_input = st.text_input("Libraries (comma-separated)", value=", ".join(metadata["libraries"]))

    if st.button("Save Changes"):
        if not all([question_input.strip(), answer_input.strip(), code_input.strip(), category_input.strip(), answer_category_input.strip()]):
            st.error("❌ All fields are required. Please fill them out.")
        else:
            formatted_code = format_code(code_input)
            output, error = execute_code(formatted_code)

            if error:
                st.error("❌ Code execution failed! Fix the following error before saving:")
                st.code(error, language="plaintext")
            else:
                question_dir = DATA_DIR / str(selected_question_id)

                (question_dir / "question.txt").write_text(question_input, encoding="utf-8")
                (question_dir / "answer.txt").write_text(answer_input, encoding="utf-8")
                (question_dir / "code.py").write_text(formatted_code, encoding="utf-8")

                updated_metadata = {
                    "question_id": selected_question_id,
                    "category": category_input.strip(),
                    "answer_category": answer_category_input.strip(),
                    "plot": plot_input,
                    "libraries": [lib.strip() for lib in libraries_input.split(",")] if libraries_input else []
                }
                with open(question_dir / "metadata.json", "w", encoding="utf-8") as f:
                    json.dump(updated_metadata, f, indent=4)

                st.success(f"✅ Question ID {selected_question_id} updated successfully!")
                st.info("Refresh to see the applied changes")
                if st.button("Refresh"):
                    st.rerun()

else:
    st.error("❌ Failed to load question data.")

if code_input:
    st.subheader("💻 Test Your Code Before Saving")
    formatted_test_code = format_code(code_input)
    st.code(formatted_test_code, language="python")

    if st.button("Execute Code"):
        output, error = execute_code(formatted_test_code)
        
        if error:
            st.error("❌ Code execution failed! Fix the following error:")
            st.error(error)
        else:
            st.success("✅ Code executed successfully!")
            st.success(f"Execution Output: {output}")