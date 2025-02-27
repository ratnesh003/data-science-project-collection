import os
import json
from pathlib import Path

def data_to_jsonl(input_dir, output_file):
    """Reads data from folders inside input_dir and writes to a JSONL file."""
    data = []
    
    for folder_name in sorted(os.listdir(input_dir), key=lambda x: int(x)):  # Sort numerically
        folder_path = os.path.join(input_dir, folder_name)
        if os.path.isdir(folder_path):  # Ensure it's a folder
            
            try:
                with open(os.path.join(folder_path, "question.txt"), "r", encoding="utf-8") as f:
                    question = f.read()

                with open(os.path.join(folder_path, "answer.txt"), "r", encoding="utf-8") as f:
                    answer = f.read()

                with open(os.path.join(folder_path, "code.py"), "r", encoding="utf-8") as f:
                    code = f.read()

                with open(os.path.join(folder_path, "metadata.json"), "r", encoding="utf-8") as f:
                    metadata = json.load(f)

                data.append({
                    "folder": folder_name,
                    "question": question,
                    "answer": answer,
                    "code": code,
                    "metadata": metadata
                })
            except FileNotFoundError as e:
                print(f"Skipping {folder_name} due to missing file: {e}")

    with open(output_file, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"Data successfully written to {output_file}")

if __name__ == "__main__":
    outputfile = input('Enter the name of file without .jsonl : ')

    script_dir = Path(__file__).parent
    input_dir = script_dir.parent / "data/questions"
    data_to_jsonl(input_dir, f'{outputfile}.jsonl')