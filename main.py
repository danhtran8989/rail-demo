import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Railway Python Backend",
    description="A production-ready Python backend for Railway",
    version="1.0.0"
)

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Railway Python Backend!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/items/")
def create_item(item: Item):
    return {
        "message": f"Item '{item.name}' created successfully",
        "item": item.model_dump()
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
