from fastapi import APIRouter, HTTPException
from models.schemas import TextInput
from services.embedding_service import process_single, process_batch
from logs import logger
from embedding import embedding_model

router = APIRouter()


@router.get("/")
def root():
    logger.info("Root endpoint hit")
    return {"message": "Hello"}


@router.get("/health")
def health():
    logger.info("Health is okay")
    return {"message": "Health is okay"}


# ----------- STORE + EMBED -----------
@router.post("/embed")
def embed(data: TextInput):
    logger.info(f"Received data for embedding: {data.text}")

    if not data.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    if isinstance(data.text, str):
        return process_single(data.text)
    else:
        logger.info(f"Processing batch of texts: {len(data.text)}")
        return process_batch(data.text)


# ----------- EMBED ONLY (for Rust / search) -----------
@router.post("/embed-only")
def embed_only(data: TextInput):
    logger.info(f"Embedding only request: {data.text}")

    if not data.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    if isinstance(data.text, str):
        embedding = embedding_model.encode(data.text)
        return {
            "embedding": embedding,
            "dim": len(embedding)
        }
    else:
        embeddings = embedding_model.encode_batch(data.text)
        return {
            "embeddings": embeddings,
            "dim": len(embeddings[0]) if embeddings else 0
        }