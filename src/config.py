from dataclasses import dataclass


@dataclass
class ModelConfig:
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    llm_model: str = "google/flan-t5-small"
    max_new_tokens: int = 256
    top_k_results: int = 5
    stream_delay: float = 0.03


@dataclass
class PathConfig:
    faiss_index: str = "vector_store/faiss_index.bin"
    chunks_file: str = "vector_store/chunks.csv"