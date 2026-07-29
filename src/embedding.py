from sentence_transformers import SentenceTransformer
import numpy as np

from src.config import ModelConfig

config = ModelConfig()


class EmbeddingModel:
    """
    Wrapper around SentenceTransformer for generating embeddings.
    """

    def __init__(self) -> None:
        self.model = SentenceTransformer(config.embedding_model)

    def encode(self, texts: list[str]) -> np.ndarray:
        """
        Generate embeddings for a list of texts.

        Args:
            texts: List of text strings.

        Returns:
            Numpy array of embeddings.
        """

        embeddings = self.model.encode(
            texts,
            show_progress_bar=False,
        )

        return np.array(
            embeddings,
            dtype="float32",
        )