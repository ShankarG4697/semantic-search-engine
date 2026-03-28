from contextlib import asynccontextmanager
import logging

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

@app.get("/search")
def search_api(
    q: str = Query(..., min_length=2, max_length=500, description="Search query"),
    limit: int = Query(2, ge=1, le=20, description="Top-k results to return"),
):
    try:
        return search(q, limit)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc