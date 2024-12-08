Chat with Multiple PDFs 📚
This project is a Streamlit-based web application that allows users to upload multiple PDF files, process their text content, and interact with them using a conversational chatbot powered by Google Generative AI and LangChain. Users can upload PDFs, extract their content, and ask context-specific questions to retrieve detailed responses.

Features
Upload and Process PDFs

Drag and drop multiple PDF files into the app.
Extract text from the uploaded PDFs and preprocess them into manageable chunks using LangChain.
AI-Powered Chat

Ask questions related to the uploaded PDFs in natural language.
Get precise answers based on the content extracted from the uploaded files.
If the question cannot be answered using the PDFs, the chatbot gracefully informs the user that the answer is unavailable.
Easy-to-Use Interface

A sleek and modern UI built with Streamlit.
Sidebar for uploading PDFs and a main section for interacting with the chatbot.
How It Works
File Upload: Users upload their PDF files using the File Upload section in the sidebar. Multiple files can be uploaded simultaneously (200 MB limit per file).
Processing: After uploading, the user presses the Submit & Process button. This extracts text from the PDFs, processes it into smaller chunks, and saves it in a FAISS vector database for efficient similarity search.
Ask a Question: Once the PDFs are processed, users can ask any question using the input box. The app retrieves the most relevant chunks of text, sends them to the conversational AI, and displays a detailed response.
Detailed Responses: The chatbot answers using the context extracted from the PDFs. If no relevant context is found, it responds with, “The answer is not available in the context.”
Installation and Setup
1. Clone the Repository
First, clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/chat-with-multiple-pdfs.git
cd chat-with-multiple-pdfs
2. Set Up Your Environment
Install the required dependencies. These are listed in the requirements.txt file.

bash
Copy code
pip install -r requirements.txt
The required dependencies include:

streamlit: To build the web app.
google-generativeai: For Google Generative AI embeddings and conversational models.
python-dotenv: For managing environment variables.
langchain: To manage text processing and conversational AI workflows.
PyPDF2: To extract text from PDF files.
chromadb and faiss-cpu: For efficient vector storage and similarity search.
3. Configure the Google Generative AI API
To use Google Generative AI, you need an API key:

Sign up for Google Generative AI at Google Generative AI Platform.

Retrieve your API key.

Create a .env file in the root directory of your project and add the following:

makefile
Copy code
GOOGLE_API_KEY=your-google-api-key
Replace your-google-api-key with your actual API key.

4. Run the Application
Launch the Streamlit app using the following command:

bash
Copy code
streamlit run app.py
The app will start, and you can access it in your browser at http://localhost:8501 (or a similar URL displayed in your terminal).

Application Walkthrough
Uploading PDFs
Navigate to the File Upload section in the left sidebar of the application.
Drag and drop one or more PDF files into the upload area or browse for files manually.
Click the 📤 Submit & Process button. The app will process your files by:
Extracting text from each uploaded PDF using PyPDF2.
Splitting the extracted text into chunks with overlapping contexts using LangChain.
Storing the chunks in a FAISS vector store for efficient search and retrieval.
Asking Questions
In the Ask a Question section, type your question into the input box (e.g., “What is DBMS?”).
Press Enter or click outside the input box. The app will:
Search the vector store for the most relevant chunks of text related to your question.
Use Google Generative AI to generate a detailed response based on the retrieved text.
View the chatbot’s response in the 📝 Reply section.
Example Usage
Scenario: You upload a PDF about database systems and another one about artificial intelligence.

Question: What are the types of databases?
Response: A detailed explanation based on the content of the uploaded PDF(s).
Question: What is artificial intelligence?
Response: A clear answer if the PDF contains relevant information, or “The answer is not available in the context” if it does not.
Troubleshooting
Common Errors
API Key Missing: Ensure that the GOOGLE_API_KEY is correctly set in the .env file.
PDF Processing Issues: Make sure the uploaded files are valid PDFs and within the 200 MB size limit.
Dependency Issues: Reinstall the required dependencies with:
bash
Copy code
pip install -r requirements.txt
File Not Found Errors: Ensure the FAISS vector store is created properly during the processing step.
Future Improvements
Add support for other document formats (e.g., Word, Excel).
Enhance the chatbot's ability to answer multi-part or follow-up questions.
Deploy the app to cloud platforms such as Streamlit Cloud, AWS, or Google Cloud for global accessibility.
Folder Structure
bash
Copy code
📂 chat-with-multiple-pdfs/
├── app.py                # Main application script
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (e.g., Google API key)
├── README.md             # Documentation
Contribution Guidelines
We welcome contributions to improve this project! To contribute:

Fork this repository.
Create a new branch for your feature or bugfix.
Submit a pull request with a detailed description of your changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or support, please feel free to open an issue in the repository or contact the repository owner directly.

If you have more questions about the README or the project setup, feel free to ask! Here are seven potential follow-ups:

How can I deploy this app on Streamlit Cloud?
What are the alternatives to FAISS for vector storage?
How can I handle PDF files with images or non-text content?
Can this be extended to include real-time chatbots?
What’s the best way to secure API keys in a production environment?
How do I add tests for this project?
How can I optimize processing for larger PDFs?
Tip: For better user experience, test your README on a fresh setup to ensure all instructions work seamlessly!
