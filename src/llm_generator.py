import ollama

def generate_answer(question, context):

    prompt = f"""
You are an assistant that answers questions based only on the provided document context.

Context:
{context}

Question:
{question}

Answer clearly and concisely based only on the context.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]