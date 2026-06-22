from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

vector = model.encode(
    "What are common credit card complaints?"
)

print(vector.shape)