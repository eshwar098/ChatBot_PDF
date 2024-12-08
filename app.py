import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function Definitions
def get_pdf_text(pdf_docs):
    """Extract text from multiple PDFs."""
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    """Split text into manageable chunks."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    """Create and save a vector store for text chunks."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    """Define the conversational AI model and prompt."""
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details. 
    If the answer is not in the provided context, just say, "The answer is not available in the context."
    
    Context:
    {context}
    
    Question:
    {question}
    
    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    """Search vector store for relevant documents and get the answer."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    return response["output_text"]

# Main Function
def main():
    # Page Configuration
    st.set_page_config(page_title="Chat with Multiple PDFs", page_icon="📚", layout="wide")
    
    # CSS for Custom Styling
    st.markdown(
        """
        <style>
        .main {
            background-color: #202123;
            color: white;
        }
        .stButton button {
            background-color: #007BFF;
            color: white;
            border-radius: 5px;
            padding: 0.5em 1em;
        }
        .stTextInput > div {
            background-color: #333;
            border-radius: 5px;
            color: white;
        }
        .stMarkdown p {
            color: white;
        }
        .sidebar {
            background-color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Header
    st.markdown("<h1 style='text-align: center; color: white;'>📚 Chat with Multiple PDFs</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>Upload multiple PDFs, process them, and ask any question!</p>", unsafe_allow_html=True)

    # Sidebar for File Uploads
    with st.sidebar:
        st.title("📂 File Upload:")
        pdf_docs = st.file_uploader(
            "Upload your PDF Files (Multiple files supported)", 
            accept_multiple_files=True, 
            type=["pdf"]
        )
        if st.button("📤 Submit & Process"):
            if pdf_docs:
                with st.spinner("Processing your PDFs..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.success("✅ All files processed successfully!")
            else:
                st.error("❌ Please upload at least one PDF file.")

    # Input for User Questions
    st.markdown("---")
    st.markdown("<h3 style='color: white;'>💬 Ask a Question:</h3>", unsafe_allow_html=True)
    user_question = st.text_input(
        "Enter your question below:", 
        placeholder="E.g., What is DBMS?",
        help="Type a question to query the uploaded PDFs."
    )

    # Display Answer
    if user_question:
        with st.spinner("Searching for the answer..."):
            try:
                answer = user_input(user_question)
                st.markdown("<h4 style='color: white;'>📝 Reply:</h4>", unsafe_allow_html=True)
                st.markdown(
                    f"<div style='background-color: #333; padding: 10px; border-radius: 5px;'>{answer}</div>", 
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"❌ Error: {e}")

# Run the App
if __name__ == "__main__":
    main()
