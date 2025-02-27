import json
from pathlib import Path
from utils.data_to_jsonl import data_to_jsonl

def load_data(jsonl_file):
    data = []
    script_dir = Path(__file__).parent
    input_dir = script_dir.parent / "data/questions"
    data_to_jsonl(input_dir, jsonl_file)
    with open(jsonl_file, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data