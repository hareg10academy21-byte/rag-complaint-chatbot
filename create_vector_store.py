from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import faiss
import os

# Load chunks
chunks_df = pd.read_csv(
    "data/processed/chunks.csv"
)

texts = chunks_df["chunk_text"].tolist()

print("Loading model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating embeddings...")

embeddings = model.encode(
    texts,
    show_progress_bar=True
)

embeddings = np.array(
    embeddings,
    dtype="float32"
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)

os.makedirs(
    "vector_store",
    exist_ok=True
)

faiss.write_index(
    index,
    "vector_store/faiss_index.bin"
)

chunks_df.to_csv(
    "vector_store/chunks.csv",
    index=False
)

print("Vector store saved!")