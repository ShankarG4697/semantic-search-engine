from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from qdrant_client.http.exceptions import ResponseHandlingException
from app.embeddings import get_embedding, get_embeddings

COLLECTION_NAME = "test_collection"

client = QdrantClient(host="localhost", port=6333)


def create_collection():
    try:
        if client.collection_exists(collection_name=COLLECTION_NAME):
            return

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )
    except ResponseHandlingException as exc:
        raise RuntimeError("Qdrant is unavailable") from exc


def insert_documents():
    # raw_text = """
    # FastAPI is a modern Python web framework.
    # PostgreSQL is a powerful relational database.
    # Redis improves performance by caching frequently accessed data.
    # Vector databases enable semantic search.
    # """
    raw_text = """
        Redis improves performance by caching frequently accessed data. It reduces database load significantly. PostgreSQL is used for structured storage and supports ACID transactions. FastAPI is used to build APIs quickly.
        """

    chunks = chunk_text_with_overlap(raw_text)

    try:
        # existing_count = client.count(collection_name=COLLECTION_NAME, exact=True).count
        # if existing_count > 0:
        #     return

        # if not chunks:
        #     return

        vectors = get_embeddings(chunks)

        points = []
        for idx, (chunk, vector) in enumerate(zip(chunks, vectors)):
            points.append(
                PointStruct(
                    id=idx,
                    vector=vector,
                    payload={"text": chunk},
                )
            )

        client.upsert(collection_name=COLLECTION_NAME, points=points)
    except ResponseHandlingException as exc:
        raise RuntimeError("Qdrant is unavailable") from exc


def search(query: str):
    query_vector = get_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=3,
    )

    return [point.payload["text"] for point in results.points]


def chunk_text(text: str) -> list[str]:
    sentences = text.strip().split(".")

    chunks = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            chunks.append(sentence)

    return chunks

def chunk_text_with_overlap(text: str, chunk_size=2, overlap=1):
    sentences = [s.strip() for s in text.split(".") if s.strip()]

    chunks = []
    i = 0

    while i < len(sentences):
        chunk = sentences[i:i + chunk_size]
        chunks.append(". ".join(chunk))

        i += (chunk_size - overlap)

    return chunks