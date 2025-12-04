from sentence_transformers import SentenceTransformer
import numpy as np
from config import EMBED_MODEL

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(EMBED_MODEL)

    def embed(self, text: str):
        return np.array(self.model.encode(text))







