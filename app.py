# import streamlit as st
# from sentence_transformers import SentenceTransformer
# import faiss
# import pandas as pd
# import numpy as np
# import os
# from src.constants import APP_TITLE, DEFAULT_TOP_K
# from src.config import PathConfig

# config = PathConfig()
# # -----------------------------
# # Load Model and Vector Store
# # -----------------------------

# @st.cache_resource
# def load_model():
#     return SentenceTransformer(
#         "sentence-transformers/all-MiniLM-L6-v2"
#     )

# model = load_model()

# # Debug checks
# print("Current directory:")
# print(os.getcwd())

# print("FAISS exists?")
# print(os.path.exists("vector_store/faiss_index.bin"))

# # Load FAISS index
# index = faiss.read_index(
#     config.faiss_index
# )

# # Load chunks
# chunks = pd.read_csv(
#     config.chunks_file
# )
# # -----------------------------
# # Retrieval Function
# # -----------------------------

# def retrieve(
#     query: str,
#     k: int = DEFAULT_TOP_K,
# ):

#     query_vector = model.encode([query])

#     distances, indices = index.search(
#         np.array(query_vector, dtype="float32"),
#         k
#     )

#     results = []
#     seen = set()

#     for idx in indices[0]:

#         text = chunks.iloc[idx]["chunk_text"]

#         if text not in seen:

#             seen.add(text)

#             results.append(
#                 chunks.iloc[idx]
#             )

#     return results

# # -----------------------------
# # Streamlit UI
# # -----------------------------

# st.title(APP_TITLE)

# question = st.text_input(
#     "Ask a question about complaints"
# )

# col1, col2 = st.columns(2)

# with col1:

#     if st.button("Ask"):

#         if question.strip() == "":

#             st.warning(
#                 "Please enter a question."
#             )

#         else:

#             retrieved_chunks = retrieve(
#                 question
#             )

#             st.subheader(
#                 "Relevant Complaint Evidence"
#             )

#             for i, item in enumerate(
#                 retrieved_chunks
#             ):

#                 st.write(
#                     f"### Result {i+1}"
#                 )

#                 st.write(
#                     item["chunk_text"]
#                 )

#             st.subheader(
#                 "Source Information"
#             )

#             for item in retrieved_chunks:

#                st.write(item["metadata"])

#                st.write("---")

# with col2:

#     if st.button("Clear"):

#         st.rerun()

# import os

# import faiss
# import numpy as np
# import pandas as pd
# import streamlit as st
# from sentence_transformers import SentenceTransformer

# from src.constants import APP_TITLE, DEFAULT_TOP_K
# from src.config import PathConfig

# config = PathConfig()


# # -------------------------------------------------
# # Page Configuration
# # -------------------------------------------------

# st.set_page_config(
#     page_title="Financial Complaint Chatbot",
#     page_icon="💳",
#     layout="wide",
# )

# st.title(APP_TITLE)

# st.caption(
#     "AI-powered Retrieval-Augmented Generation (RAG) system for financial complaint analysis."
# )


# # -------------------------------------------------
# # Sidebar
# # -------------------------------------------------

# with st.sidebar:

#     st.header("Project Information")

#     st.markdown("""
# **Business Problem**

# Financial institutions receive thousands of customer complaints.
# Finding similar complaints manually is slow and expensive.

# This chatbot retrieves the most relevant historical complaints to help analysts make faster decisions.
# """)

#     st.markdown("---")

#     st.subheader("Technology")

#     st.write("• Sentence Transformers")
#     st.write("• FAISS")
#     st.write("• Streamlit")
#     st.write("• Python")

#     st.markdown("---")

#     st.subheader("Project Statistics")

#     st.write("Embedding Model:")
#     st.success("all-MiniLM-L6-v2")

#     st.write("Top Retrieved Chunks:")
#     st.info(DEFAULT_TOP_K)


# # -------------------------------------------------
# # Load Resources
# # -------------------------------------------------

# @st.cache_resource
# def load_model():
#     return SentenceTransformer(
#         "sentence-transformers/all-MiniLM-L6-v2"
#     )


# model = load_model()

# index = faiss.read_index(config.faiss_index)

# chunks = pd.read_csv(config.chunks_file)


# # -------------------------------------------------
# # Retrieval Function
# # -------------------------------------------------

# def retrieve(
#     query: str,
#     k: int = DEFAULT_TOP_K,
# ):

#     query_vector = model.encode([query])

#     distances, indices = index.search(
#         np.array(query_vector, dtype="float32"),
#         k,
#     )

#     results = []

#     seen = set()

#     for idx in indices[0]:

#         text = chunks.iloc[idx]["chunk_text"]

#         if text not in seen:

#             seen.add(text)

#             results.append(chunks.iloc[idx])

#     return results


# # -------------------------------------------------
# # User Input
# # -------------------------------------------------

# st.header("Ask a Question")

# question = st.text_input(
#     "Enter your financial complaint question"
# )


# if st.button("Analyze Complaint"):

#     if question.strip() == "":

#         st.warning("Please enter a question.")

#     else:

#         results = retrieve(question)

#         st.success(
#             f"Retrieved {len(results)} relevant complaint documents."
#         )

#         st.markdown("## Retrieved Complaint Evidence")

#         for i, row in enumerate(results, start=1):

#             with st.expander(f"Result {i}"):

#                 st.write(row["chunk_text"])

#                 if "metadata" in row:
#                     st.caption(row["metadata"])

#         st.markdown("---")

#         st.subheader("Business Impact")

#         st.success(
#             """
# ✔ Helps analysts investigate complaints faster.

# ✔ Improves customer service efficiency.

# ✔ Reduces manual search effort.

# ✔ Supports consistent financial decision making.
# """
#         )

# import faiss
# import numpy as np
# import pandas as pd
# import streamlit as st
# from sentence_transformers import SentenceTransformer

# from src.constants import APP_TITLE, DEFAULT_TOP_K
# from src.config import PathConfig
# from src.retriever import Retriever
# from src.rag_pipeline import RAGPipeline
# config = PathConfig()
# rag = None

# try:

#     retriever = Retriever(
#         config.faiss_index,
#         config.chunks_file,
#     )

#     rag = RAGPipeline(retriever)

# except Exception as e:

#     st.warning(
#         "AI answer generation is unavailable. Retrieval mode is still available."
#     )

#     print(e)
# # -------------------------------------------------
# # PAGE CONFIGURATION
# # -------------------------------------------------

# st.set_page_config(
#     page_title="AI Financial Complaint Analysis Platform",
#     page_icon="🏦",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # -------------------------------------------------
# # HEADER
# # -------------------------------------------------

# st.title("🏦 AI Financial Complaint Analysis Platform")

# st.markdown("""
# ### Production-Ready Retrieval-Augmented Generation (RAG) System

# Analyze financial customer complaints using semantic search and artificial intelligence.

# This system helps financial institutions quickly retrieve similar historical complaints,
# support faster investigations, improve customer service, and reduce manual search effort.
# """)

# st.markdown("---")

# # -------------------------------------------------
# # LOAD MODEL
# # -------------------------------------------------

# @st.cache_resource
# def load_model():
#     return SentenceTransformer(
#         "sentence-transformers/all-MiniLM-L6-v2"
#     )

# model = load_model()

# # -------------------------------------------------
# # LOAD VECTOR STORE
# # -------------------------------------------------

# index = faiss.read_index(config.faiss_index)

# chunks = pd.read_csv(config.chunks_file)

# # -------------------------------------------------
# # KPI DASHBOARD
# # -------------------------------------------------

# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     st.metric(
#         "📄 Complaints",
#         f"{len(chunks):,}"
#     )

# with col2:
#     st.metric(
#         "🤖 Model",
#         "MiniLM"
#     )

# with col3:
#     st.metric(
#         "🔍 Top Results",
#         DEFAULT_TOP_K
#     )

# with col4:
#     st.metric(
#         "✅ Status",
#         "Ready"
#     )

# st.markdown("---")

# # -------------------------------------------------
# # SIDEBAR
# # -------------------------------------------------

# with st.sidebar:

#     st.title("🏦 Project Dashboard")

#     st.markdown("---")

#     st.subheader("Business Problem")

#     st.write("""
# Financial institutions receive thousands of customer complaints every year.

# Finding previous complaints manually is slow and inefficient.

# This application retrieves the most relevant historical complaints using semantic search and Retrieval-Augmented Generation (RAG).
# """)

#     st.markdown("---")

#     st.subheader("Project Features")

#     st.success("✔ Semantic Search")
#     st.success("✔ FAISS Vector Database")
#     st.success("✔ Sentence Embeddings")
#     st.success("✔ Streamlit Dashboard")
#     st.success("✔ Unit Tested")
#     st.success("✔ GitHub Actions CI")
#     st.success("✔ Production-Ready Code")

#     st.markdown("---")

#     st.subheader("Technology Stack")

#     st.write("🐍 Python")
#     st.write("🤖 Sentence Transformers")
#     st.write("📚 FAISS")
#     st.write("🖥 Streamlit")
#     st.write("🧠 Transformers")

#     st.markdown("---")

#     st.subheader("Project Statistics")

#     st.info(f"Complaint Chunks: {len(chunks):,}")

#     st.info("Embedding Model")

#     st.success("all-MiniLM-L6-v2")

#     st.info(f"Top Retrieved Results: {DEFAULT_TOP_K}")

#     st.markdown("---")

#     st.subheader("Business Value")

#     st.write("✔ Faster complaint investigation")

#     st.write("✔ Better customer support")

#     st.write("✔ Improved analyst productivity")

#     st.write("✔ Reduced operational costs")

#     st.write("✔ Consistent financial decision making")
#     # -------------------------------------------------
# # RETRIEVAL FUNCTION
# # -------------------------------------------------

# def retrieve(
#     query: str,
#     k: int = DEFAULT_TOP_K,
# ):

#     query_vector = model.encode([query])

#     distances, indices = index.search(
#         np.array(query_vector, dtype="float32"),
#         k,
#     )

#     results = []

#     seen = set()

#     for idx in indices[0]:

#         if idx == -1:
#             continue

#         row = chunks.iloc[idx]

#         text = row["chunk_text"]

#         if text not in seen:

#             seen.add(text)

#             results.append(row)

#     return results


# # -------------------------------------------------
# # SEARCH AREA
# # -------------------------------------------------

# st.header("🔍 Financial Complaint Search")

# st.write(
#     "Enter a customer complaint or question to retrieve the most relevant historical complaints."
# )

# question = st.text_input(
#     "Customer Complaint",
#     placeholder="Example: My bank account was frozen without notice..."
# )

# search_col, clear_col = st.columns([3, 1])

# search_clicked = search_col.button(
#     "🔍 Analyze Complaint",
#     use_container_width=True
# )

# clear_clicked = clear_col.button(
#     "🗑 Clear",
#     use_container_width=True
# )

# if clear_clicked:
#     st.rerun()

# # -------------------------------------------------
# # SEARCH EXECUTION
# # -------------------------------------------------

# if search_clicked:

#     if question.strip() == "":

#         st.error(
#             "Please enter a financial complaint before searching."
#         )

#     else:

#         with st.spinner(
#             "Searching similar complaints..."
#         ):

#             results = retrieve(question)
# ai_answer = None

# if rag is not None:

#     try:

#         contexts, generator = rag.run_stream(question)

#         ai_answer = ""

#         placeholder = st.empty()

#         for chunk in generator:

#             ai_answer = chunk

#             placeholder.markdown(
#                 f"""
# ### 🤖 AI Answer

# {ai_answer}
# """
#             )

#     except Exception as e:

#         st.error(e)
#         st.success(
#             f"Search completed successfully. Retrieved {len(results)} relevant complaints."
#         )

#         st.markdown("---")
#         if ai_answer:

#          st.success("AI answer generated successfully.")
#         st.header("📄 Retrieved Complaint Evidence")

#         if len(results) == 0:

#             st.warning(
#                 "No matching complaints were found."
#             )

#         else:

#             for rank, row in enumerate(results, start=1):

#                 with st.expander(
#                     f"⭐ Rank #{rank}"
#                 ):

#                     st.markdown("### Complaint")

#                     st.write(row["chunk_text"])

#                     st.markdown("---")

#                     c1, c2 = st.columns(2)

#                     with c1:

#                         if "complaint_id" in row.index:

#                             st.metric(
#                                 "Complaint ID",
#                                 row["complaint_id"]
#                             )

#                         if "product" in row.index:

#                             st.metric(
#                                 "Product",
#                                 row["product"]
#                             )

#                     with c2:

#                         if "issue" in row.index:

#                             st.metric(
#                                 "Issue",
#                                 row["issue"]
#                             )

#                         if "metadata" in row.index:

#                             st.caption(
#                                 row["metadata"]
#                             )

#         st.markdown("---")

#         st.header("📈 Business Impact")

#         st.success(
#             """
# ✓ Reduces complaint investigation time.

# ✓ Helps analysts identify similar historical complaints.

# ✓ Improves customer service response.

# ✓ Supports faster financial decision making.

# ✓ Reduces manual search effort.

# ✓ Improves operational efficiency.
# """
#         )

#         st.info(
#             """
# Business Interpretation

# This Retrieval-Augmented Generation (RAG) system enables financial institutions to quickly locate similar customer complaints using semantic search.

# Instead of manually reviewing thousands of complaints, analysts can retrieve the most relevant historical cases within seconds, improving investigation quality and operational efficiency.
# """
#         )

#         st.markdown("---")

#         csv = pd.DataFrame(results)

#         st.download_button(
#             label="📥 Download Search Results",
#             data=csv.to_csv(index=False),
#             file_name="retrieved_complaints.csv",
#             mime="text/csv",
#         )
#         # -------------------------------------------------
# # ABOUT THE PROJECT
# # -------------------------------------------------

# st.markdown("---")

# with st.expander("📖 About This Project"):

#     st.markdown("""
# ### Financial Complaint RAG Chatbot

# This project is a **Retrieval-Augmented Generation (RAG)** application developed to support
# financial institutions in analyzing customer complaints.

# Instead of searching thousands of complaints manually, the system uses semantic search
# to retrieve the most relevant historical complaints from a FAISS vector database.

# The retrieved information helps financial analysts:

# - Investigate complaints faster
# - Identify recurring customer issues
# - Improve customer support
# - Reduce manual workload
# - Support data-driven decision making

# ---

# ### Project Workflow

# 1. User enters a financial complaint.
# 2. The complaint is converted into an embedding using Sentence Transformers.
# 3. FAISS searches for the most similar complaint chunks.
# 4. The retrieved evidence is presented to the analyst.
# 5. (Optional) A Large Language Model generates a summarized response.

# ---

# ### Technologies Used

# - 🐍 Python
# - 🤖 Sentence Transformers
# - 📚 FAISS Vector Database
# - 💻 Streamlit
# - 🔍 Retrieval-Augmented Generation (RAG)
# - ✅ PyTest
# - ⚙ GitHub Actions CI/CD
# """)

# # -------------------------------------------------
# # SYSTEM ARCHITECTURE
# # -------------------------------------------------

# st.markdown("---")

# st.subheader("🏗 System Architecture")

# st.code(
# """
# User Question
#       │
#       ▼
# Sentence Transformer
#       │
#       ▼
# Embedding Vector
#       │
#       ▼
# FAISS Vector Database
#       │
#       ▼
# Top Relevant Complaint Chunks
#       │
#       ▼
# RAG Pipeline
#       │
#       ▼
# Financial Analyst
# """,
# language="text"
# )

# # -------------------------------------------------
# # PROJECT QUALITY
# # -------------------------------------------------

# st.markdown("---")

# st.subheader("🏆 Engineering Improvements")

# quality_col1, quality_col2 = st.columns(2)

# with quality_col1:

#     st.success("✅ Modular Code Structure")
#     st.success("✅ Type Hints")
#     st.success("✅ Dataclass Configuration")
#     st.success("✅ Utility Functions")
#     st.success("✅ Constants Module")

# with quality_col2:

#     st.success("✅ Unit Tests")
#     st.success("✅ GitHub Actions CI")
#     st.success("✅ Streamlit Dashboard")
#     st.success("✅ Professional Documentation")
#     st.success("✅ Production-Ready Design")

# # -------------------------------------------------
# # FINANCE IMPACT
# # -------------------------------------------------

# st.markdown("---")

# st.subheader("💼 Business Value")

# business1, business2, business3 = st.columns(3)

# with business1:
#     st.info(
# """
# ### ⚡ Efficiency

# Reduce complaint investigation time by retrieving relevant historical complaints within seconds.
# """
#     )

# with business2:
#     st.info(
# """
# ### 📊 Better Decisions

# Support financial analysts with evidence-based complaint analysis.
# """
#     )

# with business3:
#     st.info(
# """
# ### 😊 Customer Experience

# Improve customer satisfaction through faster and more consistent complaint resolution.
# """
#     )

# # -------------------------------------------------
# # FOOTER
# # -------------------------------------------------

# st.markdown("---")

# st.markdown(
# """
# <div style='text-align:center;'>

# ## 👩‍💻 Developed by Haregeweyn Ataklt

# **Software Engineering Student | AI & Machine Learning Enthusiast**

# **10 Academy – AI Mastery Program**

# Financial Complaint RAG Chatbot (Week 12 Capstone)

# Built using Python, Streamlit, FAISS, Sentence Transformers and Retrieval-Augmented Generation (RAG).

# </div>
# """,
# unsafe_allow_html=True,
# )
import faiss
import numpy as np
import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer

from src.constants import DEFAULT_TOP_K
from src.config import PathConfig
from src.retriever import Retriever

from src.dashboard import (
    configure_page,
    show_header,
    show_metrics,
    show_sidebar,
    show_search_box,
    show_results,
    show_business_impact,
    show_about,
    show_architecture,
    show_engineering_quality,
    show_business_value,
    show_footer,
)


# -------------------------------------------------
# CONFIGURATION
# -------------------------------------------------

config = PathConfig()


# -------------------------------------------------
# STREAMLIT PAGE
# -------------------------------------------------

configure_page()

show_header()


# -------------------------------------------------
# LOAD EMBEDDING MODEL
# -------------------------------------------------

@st.cache_resource
def load_model():

    return SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )


model = load_model()


# -------------------------------------------------
# LOAD VECTOR DATABASE
# -------------------------------------------------

index = faiss.read_index(
    config.faiss_index
)

chunks = pd.read_csv(
    config.chunks_file
)


# -------------------------------------------------
# RETRIEVER
# -------------------------------------------------

retriever = Retriever(
    config.faiss_index,
    config.chunks_file,
)


# -------------------------------------------------
# DASHBOARD INFORMATION
# -------------------------------------------------

show_metrics(
    len(chunks),
    DEFAULT_TOP_K,
)


show_sidebar(
    len(chunks),
    DEFAULT_TOP_K,
)


# -------------------------------------------------
# RETRIEVAL FUNCTION
# -------------------------------------------------

def retrieve(
    query: str,
    k: int = DEFAULT_TOP_K,
):
    """
    Retrieve similar complaint chunks using FAISS.
    """

    query_vector = model.encode(
        [query]
    )


    distances, indices = index.search(
        np.array(
            query_vector,
            dtype="float32"
        ),
        k,
    )


    results = []

    seen = set()


    for idx in indices[0]:

        if idx == -1:
            continue


        row = chunks.iloc[idx]

        text = row["chunk_text"]


        if text not in seen:

            seen.add(text)

            results.append(row)


    return results



# -------------------------------------------------
# SEARCH INTERFACE
# -------------------------------------------------

question, search_clicked, clear_clicked = show_search_box()


if clear_clicked:

    st.rerun()



if search_clicked:


    if question.strip() == "":

        st.error(
            "Please enter a financial complaint before searching."
        )


    else:


        with st.spinner(
            "Searching similar complaints..."
        ):

            results = retrieve(
                question
            )


        ai_answer = None


        show_results(
            pd.DataFrame(results),
            ai_answer,
        )



# -------------------------------------------------
# ADDITIONAL INFORMATION SECTIONS
# -------------------------------------------------

show_business_impact()

show_about()

show_architecture()

show_engineering_quality()

show_business_value()

show_footer()