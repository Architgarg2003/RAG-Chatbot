# app.py

import streamlit as st
from load_data import load_documents
from setup_rag import setup_rag

# Streamlit app
st.title("RAG Chatbot")
st.write("Upload a CSV, JSON, or TXT file to use as the knowledge base.")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["csv", "json", "txt"])

if uploaded_file is not None:
    try:
        documents = load_documents(uploaded_file)
        
        if documents:
            # Set up the RAG pipeline
            graph = setup_rag(documents)

            st.write("Knowledge base loaded successfully! You can now ask questions.")

            # User input
            user_input = st.text_input("You:", "")

            if st.button("Ask"):
                if user_input:
                    # Invoke the RAG pipeline
                    result = graph.invoke({"question": user_input})
                    
                    # Display the answer
                    st.write(f"**Bot:** {result['answer']}")
                else:
                    st.write("Please enter a question.")
    except Exception as e:
        st.error(str(e))
