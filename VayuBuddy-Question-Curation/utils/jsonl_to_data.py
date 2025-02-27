import os
import json
from pathlib import Path

def jsonl_to_data(input_file, output_dir):
    """Reads a JSONL file and reconstructs the original folder structure."""
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)
            folder_path = os.path.join(output_dir, entry["folder"])
            os.makedirs(folder_path, exist_ok=True)

            with open(os.path.join(folder_path, "question.txt"), "w", encoding="utf-8") as f_q:
                f_q.write(entry["question"])

            with open(os.path.join(folder_path, "answer.txt"), "w", encoding="utf-8") as f_a:
                f_a.write(entry["answer"])

            with open(os.path.join(folder_path, "code.py"), "w", encoding="utf-8") as f_c:
                f_c.write(entry["code"])

            with open(os.path.join(folder_path, "metadata.json"), "w", encoding="utf-8") as f_m:
                json.dump(entry["metadata"], f_m, indent=4)

    print(f"Data successfully reconstructed in {output_dir}")

if __name__ == "__main__" :
    script_dir = Path(__file__).parent
    input_dir = script_dir.parent / "data/questions"
    jsonl_to_data('output.jsonl', input_dir)