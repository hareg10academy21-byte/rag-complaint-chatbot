import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict
class Retriever:
    def __init__(self, index_path, metadata_path):
        self.index = faiss.read_index(index_path)
        self.metadata = pd.read_parquet(metadata_path) if metadata_path.endswith(".parquet") else pd.read_csv(metadata_path)

        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def embed_query(self, query: str):
        return self.model.encode([query]).astype("float32")

    def search(
    self,
    query: str,
    k: int = 5,
) -> List[Dict]:
        query_vec = self.embed_query(query)

        distances, indices = self.index.search(query_vec, k)

        results = []

        for idx in indices[0]:
            row = self.metadata.iloc[idx]

            results.append({
                "complaint_id": row.get("complaint_id"),
                "product": row.get("product"),
                "issue": row.get("issue"),
                "chunk_text": row.get("chunk_text", "")
            })

        return results