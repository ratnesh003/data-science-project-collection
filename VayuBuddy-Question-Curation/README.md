# VayuBuddy Question Curation

## 🎯 Aim
The purpose to create this templet is to have the automated interface to collect and manage data analytic questions for VayuBuddy

## 📂 Folder Structure

The project is organized as follows:

```bash
project_root/
│── app.py                         # Main Streamlit application
│── requirements.txt               # Dependencies list
│── README.md                      # Documentation
│
├── data/
│   ├── questions/                 # Stores question-related data
│   │   ├── 0/                     # Folder for question ID 0
│   │   │   ├── question.txt       # Question text
│   │   │   ├── answer.txt         # Answer text
│   │   │   ├── code.py            # Reference code for the question
│   │   │   └── metadata.json      # Metadata for the question
│   │   ├── 1/                     # Folder for question ID 1
│   │   │   ├── question.txt       # Question text
│   │   │   ├── answer.txt         # Answer text
│   │   │   ├── code.py            # Reference code for the question
│   │   │   └── metadata.json      # Metadata for the question
│   ... ... ...                    # and so on...
│   │   ... ...
│   │
│   └── raw_data/                  # Stores the required CSV's
│       ├── NCAP_Funding.csv       # NCAP Funding Data
│       ├── State.csv              # States area & population Data
│       └── Data.csv               # Main AQI Data
│
├── pages/                         # Streamlit multipage support
│   ├── all_question.py            # Page to view questions
│   ├── execute_code.py            # Page to run the code of all questions
│   ├── add_question.py            # Page to add new questions
│   ├── edit_question.py           # Page to edit existing questions
│   └── delete_question.py         # Page to delete questions
│
├── utils/                         # Utility functions
│   ├── load_jsonl.py              # Function to load questions a list
│   ├── data_to_jsonl.py           # Function to convert question folders into JSONL 
│   ├── jsonl_to_data.py           # Function to convert JSONL into question folders 
│   └── code_services.py           # Handles code formatting & execution
│
└── output.jsonl                   # Processed question data in JSONL format
```

This structure ensures **modularity** and **maintainability** of the project. 🚀


## 📜 How to use this App

- Add questions through ```Add Questions``` Page
- Edit questions through ```Edit Questions``` Page
- Delete questions through ```Delete Questions``` Page
- The Data will not be saved in-case of missing fields or error in code

### ```NOTE```
- while entering Data form code.py in ```Add Questions``` Page or ```Edit Questions``` Page either follow the ```true_code format``` i.e. all code written in the true_code function and true_code function called in the end of it's defination or follow ```No true_code format```

#### true_code format
```python
def true_code():
    import pandas as pd
    
    df = pd.read_csv('data/raw_data/Data.csv', sep=",")
    
    data = df.groupby(['state','station'])['PM2.5'].mean()
    ans = data.idxmax()[0]
    print(ans)

true_code()
```

#### No true_code format
```python
import pandas as pd

df = pd.read_csv('data/raw_data/Data.csv', sep=",")

data = df.groupby(['state','station'])['PM2.5'].mean()
ans = data.idxmax()[0]
print(ans)
```

## 🧩 Sample Question

### question.txt
```bash
Which state has the highest average PM2.5 concentration across all stations?
```

### answer.txt
```bash
Delhi
```

### code.py
```python
def true_code():
    import pandas as pd
    
    df = pd.read_csv('data/raw_data/Data.csv', sep=",")
    
    data = df.groupby(['state','station'])['PM2.5'].mean()
    ans = data.idxmax()[0]
    print(ans)

true_code()
```

### metadata.json
```json
{
    "question_id": 0,
    "category": "spatial",
    "answer_category": "single",
    "plot": false,
    "libraries": [
        "pandas"
    ]
}
```


## 🛠️ How to Set-Up project

open the terminal in the empty folder and follow the following steps:

### 1st step : clone repo
```bash
git clone https://github.com/ratnesh003/VayuBuddy-Question-Curation.git .
```

### 2rd step : to install the dependencies to run the codes
```bash
pip install -r requirements.txt
```

### 3nd step : to create dummy /data folder from already present output.jsonl
```bash
py .\utils\jsonl_to_data.py 
```