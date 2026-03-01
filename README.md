[README.md](https://github.com/user-attachments/files/25658657/README.md)
# PDF Reader using LLM and RAG - By Saumya Prasad Sinha 23FE10CSE00140 

This project implements a Retrieval-Augmented Generation (RAG) based system for question answering over PDF documents.

The goal of the system is to allow users to upload a PDF file and ask natural language questions about its content. The system retrieves relevant portions of the document and uses a Large Language Model (LLM) to generate accurate, context-aware responses.

Project Workflow

1. Load PDF document
2. Extract text from the document
3. Split text into manageable chunks
4. Generate embeddings for each chunk
5. Store embeddings in a vector database
6. Retrieve relevant chunks based on user query
7. Generate final answer using an LLM

Tech Stack

- Python
- LangChain
- OpenAI API
- FAISS (Vector Store)
- PyPDF2
- Streamlit (planned)

Current Status

- Project structure initialized
- Dependencies defined
- RAG pipeline under development

Installation

pip install -r requirements.txt

Usage (In Progress)

python app.py

Note

This project is under active development. Additional features and improvements will be added in subsequent commits.
