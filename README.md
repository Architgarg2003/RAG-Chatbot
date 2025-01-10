# RAG Chatbot

A Retrieval-Augmented Generation (RAG) Chatbot built with Streamlit, utilizing Groq for language modeling and Hugging Face for embeddings. This chatbot allows users to upload various file formats (CSV, JSON, TXT) as a knowledge base and interactively ask questions.

## Features

- Upload knowledge base in CSV, JSON, or TXT format.
- Uses Groq's language model for generating responses.
- Utilizes Hugging Face embeddings for document similarity search.
- Interactive web interface built with Streamlit.


## Installation

1. Clone the repository:

 ```bash
 git clone https://github.com/yourusername/RAG-Chatbot.git
 cd rag-chatbot
 ```

2. Create a virtual environment (optional but recommended):

  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```

3. Install the required packages:

  ```bash
  pip install -r requirements.txt
  ```

4. Set your Groq API key as an environment variable:

  ```bash
  GROQ_API_KEY="your_groq_api_key"
  ```

5. Run the Streamlit app:

  ```bash
  streamlit run app.py
  ```

Open your web browser and go to http://localhost:8501.
Upload a CSV, JSON, or TXT file to use as the knowledge base.
Ask questions in the input box and receive answers based on the uploaded knowledge base.


  
