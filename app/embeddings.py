from sentence_transformers import SentenceTransformer

# Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(texts: list[str]) -> list[list[float]]:
    embeddings = model.encode(texts)
    return embeddings.tolist()


def get_embedding(text: str):
    return get_embeddings([text])[0]
