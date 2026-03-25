from fastapi import FastAPI
from app.db import create_collection, insert_dummy_data, search_dummy

app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_collection()
    insert_dummy_data()
    
    
@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/test-search")
def test_search():
    return search_dummy()