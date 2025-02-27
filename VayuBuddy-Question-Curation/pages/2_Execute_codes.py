import subprocess
import streamlit as st
from utils.load_jsonl import load_data

# Load Data
data_file = "output.jsonl"
data = load_data(data_file)

# Create category-wise dictionary
category_dict = {}
for entry in data:
    category = entry["metadata"].get("category", "Uncategorized")
    if category not in category_dict:
        category_dict[category] = []
    category_dict[category].append(entry)

st.title("Code Execution")

# Select Category
category_selected = st.selectbox("Select Category", list(category_dict.keys()))

# Select Question
question_dict = {q["question"]: {"code": q["code"], "folder": q["folder"]} for q in category_dict[category_selected]}
question_selected = st.selectbox("Select Question", list(question_dict.keys()))

# Get folder name and code snippet
selected_entry = question_dict[question_selected]
folder_name = selected_entry["folder"]
code_snippet = selected_entry["code"]

# Show Code Snippet
st.code(code_snippet, language="python")

# Execute Button
if st.button("Execute"):
    # Path to the selected code.py file
    # code_path = script_dir.parent / "data/questions" / folder_name / "code.py"
    code_path = f"data/questions/{folder_name}/code.py"

    try:
        # Execute the Python script and capture the output
        result = subprocess.check_output(["python", str(code_path)], text=True, stderr=subprocess.STDOUT)

        # Display the execution output
        st.subheader("Execution Output:")
        st.success(result)

    except subprocess.CalledProcessError as e:
        # Display any errors if execution fails
        st.error(f"Error executing script:\n{e.output}")