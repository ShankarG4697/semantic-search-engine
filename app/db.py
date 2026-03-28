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
    docs = [
        {"id": 1, "text": "FastAPI is a modern Python web framework"},
        {"id": 2, "text": "PostgreSQL is a powerful relational database"},
        {"id": 3, "text": "Redis is used for caching and fast access"},
        {"id": 4, "text": "Vector databases enable semantic search"},
    ]

    try:
        existing_count = client.count(collection_name=COLLECTION_NAME, exact=True).count
        if existing_count > 0:
            return

        vectors = get_embeddings([doc["text"] for doc in docs])
        print("Vectors:", vectors)
        points = []
        for doc, vector in zip(docs, vectors):
            points.append(
                PointStruct(
                    id=doc["id"],
                    vector=vector,
                    payload={"text": doc["text"]},
                )
            )

        client.upsert(collection_name=COLLECTION_NAME, points=points)
    except ResponseHandlingException as exc:
        raise RuntimeError("Qdrant is unavailable") from exc


def search(query: str, limit: int = 2):
    try:
        query_vector = get_embedding(query)

        results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            limit=limit,
        )
    except ResponseHandlingException as exc:
        raise RuntimeError("Qdrant is unavailable") from exc

    return [
        {
            "score": point.score,
            "text": point.payload.get("text") if point.payload else None,
        }
        for point in results.points
    ]