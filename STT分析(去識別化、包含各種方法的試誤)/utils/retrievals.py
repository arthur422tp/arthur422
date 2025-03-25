"""
This is for retrieval
"""
import faiss
from sentence_transformers import SentenceTransformer

class Retrieval:
    def __init__(self):
        self.model = SentenceTransformer("intfloat/multilingual-e5-large")



    def build_index(self, embeddings):
        """
        Args:
            embeddings (_type_): _description_
        """
        faiss.normalize_L2(embeddings)
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatIP(dimension)
        index.add(embeddings) #pylint: disable=no-value-for-parameter

        return index

    def retrieval(self, query, text, index, k:int, threshold:int):
        """_summary_

        Args:
            query (_type_): _description_
            text (_type_): _description_
            k (int): _description_
        """
        query_embedding = self.model.encode(query)
        new_query_embedding = query_embedding.reshape(1,-1)
        faiss.normalize_L2(new_query_embedding)
        d, I = index.search(new_query_embedding, k)

        retrieval_docs = [text[I[0][i]] for i in range(len(d[0])) if d[0][i] >= threshold]

        return retrieval_docs
