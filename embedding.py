# ----------- Embedding Model -----------
from typing import List, Union
from sentence_transformers import SentenceTransformer
from logs import logger
class EmbeddingModel:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.dimension = len(self.model.encode("test"))

    def encode(self, text: str) -> List[float]:
        return self.model.encode(text).tolist()

    def encode_batch(self, texts: List[str]) -> List[List[float]]:
        return self.model.encode(texts).tolist()

# Initialize once (important)
embedding_model = EmbeddingModel()