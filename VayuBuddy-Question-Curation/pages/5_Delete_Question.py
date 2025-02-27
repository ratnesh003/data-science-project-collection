import streamlit as st
import os
import shutil
from pathlib import Path
from utils.load_jsonl import load_data  

DATA_DIR = Path("data/questions")
JSONL_FILE = "output.jsonl"  

questions_data = load_data(JSONL_FILE)

categories = sorted(set(q["metadata"]["category"] for q in questions_data))

st.title("🗑️ Delete a Question")

if not categories:
    st.warning("No categories available.")
    st.stop()

selected_category = st.selectbox("Select a Category", categories)

filtered_questions = {int(q["folder"]): q["question"][:50] + "..." for q in questions_data if q["metadata"]["category"] == selected_category}

if not filtered_questions:
    st.warning("No questions found in this category.")
    st.stop()

selected_question_id = st.selectbox("Select Question to Delete", list(filtered_questions.keys()), format_func=lambda x: f"ID {x}: {filtered_questions[x]}")

selected_question = next((q for q in questions_data if int(q["folder"]) == selected_question_id), None)

if selected_question:
    st.subheader("Question Details")
    st.text_area("Question", value=selected_question["question"], disabled=True, height=70)
    st.text_area("Answer", value=selected_question["answer"], disabled=True, height=70)

    st.subheader("Code")
    st.code(selected_question["code"], language="python")
    
    metadata = selected_question["metadata"]
    st.subheader("Meta data")
    st.write(f"Category : **{metadata['category']}**")
    st.write(f"Answer Category : **{metadata['answer_category']}**")
    st.write(f"Plot Required : **{'Yes' if metadata['plot'] else 'No'}**")
    st.write(f"Libraries : **{', '.join(metadata['libraries']) if metadata['libraries'] else 'None'}**")

    def rename_folders(deleted_id):
        """Renames folders after deleting one to maintain continuous numbering."""
        all_folders = sorted([int(f) for f in os.listdir(DATA_DIR) if f.isdigit()])
        
        for folder_id in all_folders:
            if folder_id > deleted_id:
                old_path = DATA_DIR / str(folder_id)
                new_path = DATA_DIR / str(folder_id - 1)
                shutil.move(old_path, new_path) 

    st.info("Need to check the box in-order to delete the question")
    confirm = st.checkbox("Confirm Deletion")
    
    if st.button("🚨 Delete This Question"):
        if confirm:
            question_folder = DATA_DIR / str(selected_question_id)
            if question_folder.exists():
                shutil.rmtree(question_folder)  
                rename_folders(selected_question_id) 
                st.success(f"✅ Question ID {selected_question_id} deleted successfully!")
                st.info("Refresh to see the applied changes")
                if st.button("Refresh"):
                    st.rerun()
        else:
            st.warning("⚠️ Please check 'Confirm Deletion' before proceeding.")

else:
    st.error("❌ Failed to load question data.")