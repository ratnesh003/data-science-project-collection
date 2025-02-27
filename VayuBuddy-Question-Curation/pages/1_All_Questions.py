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

st.title("Questions by Category")

for category, questions in category_dict.items():
    st.subheader(category)
    for q in questions:
        st.write(f"🔹 {q['question']}")