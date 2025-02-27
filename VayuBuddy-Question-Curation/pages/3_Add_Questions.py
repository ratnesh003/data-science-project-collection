import streamlit as st
import json
from pathlib import Path
from utils.code_services import format_code, execute_code

QUESTIONS_DIR = Path("data/questions")
QUESTIONS_DIR.mkdir(parents=True, exist_ok=True)

def get_next_question_id():
    existing_ids = [int(folder.name) for folder in QUESTIONS_DIR.iterdir() if folder.is_dir() and folder.name.isdigit()]
    return max(existing_ids, default=-1) + 1

st.title("📝 Add a New Question")

question_text = st.text_area("Enter Question", placeholder="Type the question here...", height=80)
answer_text = st.text_area("Enter Answer", placeholder="Type the answer here...", height=80)
user_code = st.text_area("Enter Code", placeholder="Write your Python solution here...", height=300)

category = st.text_input("Category", placeholder="e.g. spatial")
answer_category = st.text_input("#### Answer Category", placeholder="e.g. signal")
plot = st.checkbox("## Does this require a plot?")
libraries = st.text_input("Libraries (comma-separated)", placeholder="e.g. pandas, numpy")

if st.button("Save Question"):
    if not all([question_text.strip(), answer_text.strip(), user_code.strip(), category.strip(), answer_category.strip()]):
        st.error("❌ All fields are required. Please fill them out.")
    else:
        formatted_code = format_code(user_code)
        output, error = execute_code(formatted_code)

        if error:
            st.error("❌ Code execution failed! Fix the following error before saving:")
            st.code(error, language="plaintext")
        else:
            question_id = get_next_question_id()
            question_dir = QUESTIONS_DIR / str(question_id)
            question_dir.mkdir(parents=True, exist_ok=True)

            (question_dir / "question.txt").write_text(question_text, encoding="utf-8")

            (question_dir / "answer.txt").write_text(answer_text, encoding="utf-8")

            (question_dir / "code.py").write_text(formatted_code, encoding="utf-8")

            metadata = {
                "question_id": question_id,
                "category": category.strip().lower(),
                "answer_category": answer_category.strip(),
                "plot": plot,
                "libraries": [lib.strip() for lib in libraries.split(",")] if libraries else []
            }
            with open(question_dir / "metadata.json", "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=4)

            st.success(f"✅ Question saved successfully! (ID: {question_id})")
            st.info("refresh in-order to see the applied changes")
            if st.button("refresh") :
                st.rerun()

if user_code:
    st.subheader("💻 Test Your Code Before Saving")
    formatted_test_code = format_code(user_code)
    st.code(formatted_test_code, language="python")

    if st.button("Execute Code"):
        output, error = execute_code(formatted_test_code)
        
        if error:
            st.error("❌ Code execution failed! Fix the following error:")
            st.error(error)
        else:
            st.success("✅ Code executed successfully!")
            st.success(f"Execution Output : {output}")