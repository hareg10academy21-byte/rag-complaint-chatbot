import faiss
import pandas as pd
import pickle

index = faiss.read_index(
    "vector_store/faiss_index.bin"
)

metadata = pd.read_csv(
    "vector_store/metadata.csv"
)

print(index.ntotal)
print(metadata.head())