from src.pdf_loader import load_pdf
from src.chunking import chunk_text
from src.embeddings import create_embeddings, embed_query
from src.vector_store import create_index, search_index
from src.llm_generator import generate_answer


def build_rag(pdf_path):

    text = load_pdf(pdf_path)

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    index = create_index(embeddings)

    return index, chunks


def query_rag(index, chunks, question):

    query_embedding = embed_query(question)

    indices = search_index(index, query_embedding)

    context = ""

    for i in indices[0]:
        context += chunks[i] + "\n"

    answer = generate_answer(question, context)

    return answer