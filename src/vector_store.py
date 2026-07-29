import faiss
import numpy as np


class VectorStore:
    """
    Simple FAISS vector store wrapper.
    """

    def __init__(
        self,
        dimension: int,
    ) -> None:

        self.index = faiss.IndexFlatL2(dimension)

    def add(
        self,
        embeddings: np.ndarray,
    ) -> None:

        self.index.add(embeddings)

    def search(
        self,
        query_vector: np.ndarray,
        k: int = 5,
    ):

        distances, indices = self.index.search(
            query_vector,
            k,
        )

        return distances, indices

    def save(
        self,
        path: str,
    ) -> None:

        faiss.write_index(
            self.index,
            path,
        )

    @staticmethod
    def load(
        path: str,
    ):

        return faiss.read_index(path)