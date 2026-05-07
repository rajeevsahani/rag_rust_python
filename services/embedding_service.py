from embedding import embedding_model
from db.queries import insert_single, insert_batch
from logs import logger
def process_single(text: str):
    embedding = embedding_model.encode(text)
    insert_single(text, embedding)

    return {
        "message": "Single text inserted",
        "embedding_dim": len(embedding)
    }


def process_batch(texts):
    embeddings = embedding_model.encode_batch(texts)

    records = [(doc, emb) for doc, emb in zip(texts, embeddings)]

    insert_batch(records)

    return {
        "message": f"{len(records)} records inserted",
        "embedding_dim": len(embeddings[0]) if embeddings else 0
    }