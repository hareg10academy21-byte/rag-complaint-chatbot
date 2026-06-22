import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
import numpy as np
import os

# -----------------------------
# Load Model and Vector Store
# -----------------------------

@st.cache_resource
def load_model():
    return SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

model = load_model()

# Debug checks
print("Current directory:")
print(os.getcwd())

print("FAISS exists?")
print(os.path.exists("vector_store/faiss_index.bin"))

# Load FAISS index
index = faiss.read_index(
    "vector_store/faiss_index.bin"
)

# Load chunks
chunks = pd.read_csv(
    "vector_store/chunks.csv"
)

# -----------------------------
# Retrieval Function
# -----------------------------

def retrieve(query, k=3):

    query_vector = model.encode([query])

    distances, indices = index.search(
        np.array(query_vector, dtype="float32"),
        k
    )

    results = []
    seen = set()

    for idx in indices[0]:

        text = chunks.iloc[idx]["chunk_text"]

        if text not in seen:

            seen.add(text)

            results.append(
                chunks.iloc[idx]
            )

    return results

# -----------------------------
# Streamlit UI
# -----------------------------

st.title("💳 Financial Complaint Chatbot")

question = st.text_input(
    "Ask a question about complaints"
)

col1, col2 = st.columns(2)

with col1:

    if st.button("Ask"):

        if question.strip() == "":

            st.warning(
                "Please enter a question."
            )

        else:

            retrieved_chunks = retrieve(
                question
            )

            st.subheader(
                "Relevant Complaint Evidence"
            )

            for i, item in enumerate(
                retrieved_chunks
            ):

                st.write(
                    f"### Result {i+1}"
                )

                st.write(
                    item["chunk_text"]
                )

            st.subheader(
                "Source Information"
            )

            for item in retrieved_chunks:

               st.write(item["metadata"])

               st.write("---")

with col2:

    if st.button("Clear"):

        st.rerun()