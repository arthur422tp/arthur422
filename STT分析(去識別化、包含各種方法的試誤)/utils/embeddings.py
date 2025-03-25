"""
This is for embedding.
"""

import numpy as np
import torch
from sentence_transformers import SentenceTransformer

class WordEmbedding():
    def __init__(self):
        self.model = SentenceTransformer("intfloat/multilingual-e5-large")
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.text = None

    def embedding(self, text):
        """_summary_

        Args:
            model (_type_): _description_
            text (_type_): _description_
        """
        embeddings = self.model.encode(text, device=self.device)
        return embeddings
