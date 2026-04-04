import ollama

def generate_answer(query: str, context_chunks: list[str]):
    context = "\n".join(context_chunks)

    prompt = f"""
    You are an assistant. Answer ONLY using the context below.
    If the answer is not in the context, say "I don't know".

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]