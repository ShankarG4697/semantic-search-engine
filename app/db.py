from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

COLLECTION_NAME = "test_collection"

client = QdrantClient(host="localhost", port=6333)


def create_collection():
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=4, distance=Distance.COSINE),
    )


def insert_dummy_data():
    points = [
        PointStruct(id=1, vector=[0.1, 0.2, 0.3, 0.4], payload={"name": "A"}),
        PointStruct(id=2, vector=[0.2, 0.1, 0.4, 0.3], payload={"name": "B"}),
    ]

    client.upsert(collection_name=COLLECTION_NAME, points=points)


def search_dummy():
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=[0.1, 0.2, 0.3, 0.4],
        limit=2,
    )

    return [
        {"id": point.id, "payload": point.payload}
        for point in results.points
    ]