PDF Reader using RAG

This project implements a simple Retrieval-Augmented Generation (RAG)
pipeline for answering questions from PDF documents.

Pipeline:

PDF → Text Extraction → Chunking → Embedding Generation → Vector Storage → Retrieval

Steps:
1. Extract text from PDF
2. Split text into chunks
3. Generate embeddings
4. Store embeddings in FAISS
5. Retrieve relevant sections for user queries