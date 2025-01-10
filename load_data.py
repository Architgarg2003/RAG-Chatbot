# load_data.py

import pandas as pd
import json
from langchain_core.documents import Document

def load_documents(uploaded_file):
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1]

        if file_extension == 'csv':
            # Load CSV file
            df = pd.read_csv(uploaded_file)
            documents = [{'page_content': row['answer'], 'metadata': {'question': row['question']}} for index, row in df.iterrows()]
            return documents

        elif file_extension == 'json':
            # Load JSON file
            data = json.load(uploaded_file)
            documents = [{'page_content': item['answer'], 'metadata': {'question': item['question']}} for item in data]
            return documents

        elif file_extension in ['txt', 'text']:
            # Load plain text file
            content = uploaded_file.read().decode("utf-8")
            documents = [{'page_content': line, 'metadata': {'question': line}} for line in content.splitlines() if line]
            return documents

        else:
            raise ValueError("Unsupported file format. Please upload a CSV, JSON, or TXT file.")
    return None
