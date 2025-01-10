# setup_rag.py 
# setup_rag.py

from langchain import hub
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document
from langgraph.graph import StateGraph, START
from typing_extensions import List, TypedDict
import getpass
import os

# Get the API key for Groq
if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = "API_KEY"

# Load the LLM
llm = ChatGroq(model="llama3-8b-8192")

# Load the embeddings model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# Set up the vector store
vector_store = InMemoryVectorStore(embeddings)

# Define the prompt for question-answering
prompt = hub.pull("rlm/rag-prompt")

# Define the state for the application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

# Define application steps
def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}

# Compile application
def setup_rag(documents):
    vector_store.add_documents([Document(page_content=doc['page_content'], metadata=doc['metadata']) for doc in documents])
    
    graph_builder = StateGraph(State).add_sequence([retrieve, generate])
    graph_builder.add_edge(START, "retrieve")
    return graph_builder.compile()