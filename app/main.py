from contextlib import asynccontextmanager
import logging

from app.rag import generate_answer
from fastapi import FastAPI, HTTPException, Query
from app.db import create_collection, insert_documents, search

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(_: FastAPI):
    try:
        create_collection()
        insert_documents()
    except RuntimeError as exc:
        logger.warning("Startup initialization skipped: %s", exc)
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/ask")
def ask(q: str):
    chunks = search(q)
    answer = generate_answer(q, chunks)

    return {
        "query": q,
        "retrieved_chunks": chunks,
        "answer": answer
    }