import streamlit as st


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

def configure_page() -> None:
    """Configure Streamlit page settings."""

    st.set_page_config(
        page_title="AI Financial Complaint Analysis Platform",
        page_icon="🏦",
        layout="wide",
        initial_sidebar_state="expanded",
    )


# -------------------------------------------------
# HEADER
# -------------------------------------------------

def show_header() -> None:
    """Display application header."""

    st.title("🏦 AI Financial Complaint Analysis Platform")

    st.markdown(
        """
### Production-Ready Retrieval-Augmented Generation (RAG) System

Analyze financial customer complaints using semantic search and artificial intelligence.

This system helps financial institutions quickly retrieve similar historical complaints,
support faster investigations,improve customer service,and reduce manual search effort.
"""
    )

    st.markdown("---")


# -------------------------------------------------
# KPI METRICS
# -------------------------------------------------

def show_metrics(
    total_chunks: int,
    top_k: int,
) -> None:
    """Display dashboard metrics."""

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📄 Complaints",
            f"{total_chunks:,}",
        )

    with col2:
        st.metric(
            "🤖 Model",
            "MiniLM",
        )

    with col3:
        st.metric(
            "🔍 Top Results",
            top_k,
        )

    with col4:
        st.metric(
            "✅ Status",
            "Ready",
        )

    st.markdown("---")
    # -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

def show_sidebar(
    total_chunks: int,
    top_k: int,
) -> None:
    """Display the application sidebar."""

    with st.sidebar:

        st.title("🏦 Project Dashboard")

        st.markdown("---")

        st.subheader("Business Problem")

        st.write("""
Financial institutions receive thousands of customer complaints every year.

Finding previous complaints manually is slow, expensive, and inefficient.

This application retrieves the most relevant historical complaints using semantic search
and Retrieval-Augmented Generation (RAG), helping analysts investigate complaints
faster and make better decisions.
""")

        st.markdown("---")

        st.subheader("Project Features")

        st.success("✔ Semantic Search")
        st.success("✔ Retrieval-Augmented Generation (RAG)")
        st.success("✔ FAISS Vector Database")
        st.success("✔ Sentence Transformers")
        st.success("✔ Streamlit Dashboard")
        st.success("✔ Unit Tests")
        st.success("✔ GitHub Actions CI/CD")
        st.success("✔ Production-Ready Architecture")

        st.markdown("---")

        st.subheader("Technology Stack")

        st.write("🐍 Python")
        st.write("🤖 Sentence Transformers")
        st.write("📚 FAISS")
        st.write("🧠 Transformers")
        st.write("💻 Streamlit")
        st.write("⚙ GitHub Actions")
        st.write("🧪 PyTest")

        st.markdown("---")

        st.subheader("Project Statistics")

        st.info(f"Complaint Chunks: {total_chunks:,}")

        st.info("Embedding Model")
        st.success("sentence-transformers/all-MiniLM-L6-v2")

        st.info(f"Top Retrieved Results: {top_k}")

        st.markdown("---")

        st.subheader("Business Value")

        st.write("✔ Faster complaint investigation")
        st.write("✔ Reduced manual effort")
        st.write("✔ Better analyst productivity")
        st.write("✔ Improved customer service")
        st.write("✔ Evidence-based decision making")

        st.markdown("---")

        st.subheader("Project Quality")

        st.success("✓ Modular Code")
        st.success("✓ Type Hints")
        st.success("✓ Dataclasses")
        st.success("✓ Utility Functions")
        st.success("✓ Unit Tests")
        st.success("✓ CI/CD Pipeline")
        # -------------------------------------------------
# SEARCH BOX
# -------------------------------------------------

def show_search_box():
    """
    Display the complaint search area.

    Returns:
        tuple:
            question (str)
            search_clicked (bool)
            clear_clicked (bool)
    """

    st.header("🔍 Financial Complaint Search")

    st.write(
        "Enter a financial complaint or question to retrieve similar historical complaints."
    )

    question = st.text_input(
        "Customer Complaint",
        placeholder="Example: My bank account was frozen without notice..."
    )

    search_col, clear_col = st.columns([3, 1])

    with search_col:

        search_clicked = st.button(
            "🔍 Analyze Complaint",
            use_container_width=True,
        )

    with clear_col:

        clear_clicked = st.button(
            "🗑 Clear",
            use_container_width=True,
        )

    return question, search_clicked, clear_clicked
# -------------------------------------------------
# SEARCH RESULTS
# -------------------------------------------------

def show_results(
    results,
    ai_answer=None,
):
    """
    Display retrieved complaints and AI answer.
    """

    st.success(
        f"Retrieved {len(results)} relevant complaint(s)."
    )

    st.markdown("---")

    if ai_answer:

        st.subheader("🤖 AI Summary")

        st.success(ai_answer)

        st.markdown("---")

    st.header("📄 Retrieved Complaint Evidence")

    if len(results) == 0:

        st.warning(
            "No similar complaints were found."
        )

        return

    for rank, row in enumerate(results, start=1):

        with st.expander(f"⭐ Result {rank}"):

            st.markdown("### Complaint")

            st.write(row["chunk_text"])

            st.markdown("---")

            col1, col2 = st.columns(2)

            with col1:

                if "complaint_id" in row.index:

                    st.metric(
                        "Complaint ID",
                        row["complaint_id"],
                    )

                if "product" in row.index:

                    st.metric(
                        "Product",
                        row["product"],
                    )

            with col2:

                if "issue" in row.index:

                    st.metric(
                        "Issue",
                        row["issue"],
                    )

                if "metadata" in row.index:

                    st.caption(
                        row["metadata"],
                    )

    st.markdown("---")

    csv = results.to_csv(index=False)

    st.download_button(
        "📥 Download Results",
        csv,
        "retrieved_complaints.csv",
        "text/csv",
    )
    # -------------------------------------------------
# BUSINESS IMPACT
# -------------------------------------------------

def show_business_impact():
    """Display business impact section."""

    st.header("📈 Business Impact")

    st.success(
        """
✓ Reduces complaint investigation time.

✓ Helps analysts identify similar historical complaints.

✓ Improves customer service response.

✓ Supports faster financial decision making.

✓ Reduces manual search effort.

✓ Improves operational efficiency.
"""
    )

    st.info(
        """
### Business Interpretation

This Retrieval-Augmented Generation (RAG) system enables financial institutions to
retrieve similar customer complaints within seconds.

Instead of manually reviewing thousands of complaints, financial analysts receive
the most relevant historical cases instantly, improving productivity,
decision quality, and customer satisfaction.
"""
    )

    st.markdown("---")
    # -------------------------------------------------
# ABOUT PROJECT
# -------------------------------------------------

def show_about():
    """Display project description."""

    with st.expander("📖 About This Project"):

        st.markdown(
"""
## Financial Complaint RAG Chatbot

This project is a Retrieval-Augmented Generation (RAG) application designed
for financial institutions.

Instead of manually searching through thousands of customer complaints,
the application retrieves the most relevant historical complaints using
semantic search powered by FAISS and Sentence Transformers.

### Workflow

1. Customer enters a complaint.
2. Complaint is converted into an embedding.
3. FAISS retrieves similar complaints.
4. Relevant evidence is displayed.
5. Optional AI-generated summary is produced.

### Technologies

- Python
- Streamlit
- FAISS
- Sentence Transformers
- Transformers
- PyTest
- GitHub Actions
"""
        )
        # -------------------------------------------------
# ARCHITECTURE
# -------------------------------------------------

def show_architecture():
    """Display system architecture."""

    st.subheader("🏗 System Architecture")

    st.code(
"""
User Question
      │
      ▼
Sentence Transformer
      │
      ▼
Embedding Vector
      │
      ▼
FAISS Vector Store
      │
      ▼
Top Relevant Complaints
      │
      ▼
RAG Pipeline
      │
      ▼
AI Response
""",
language="text",
)

    st.markdown("---")
    # -------------------------------------------------
# ENGINEERING QUALITY
# -------------------------------------------------

def show_engineering_quality():
    """Display engineering improvements."""

    st.subheader("🏆 Engineering Improvements")

    col1, col2 = st.columns(2)

    with col1:

        st.success("✅ Modular Code")
        st.success("✅ Type Hints")
        st.success("✅ Dataclasses")
        st.success("✅ Utility Functions")
        st.success("✅ Constants Module")

    with col2:

        st.success("✅ Unit Tests")
        st.success("✅ GitHub Actions CI")
        st.success("✅ Streamlit Dashboard")
        st.success("✅ Professional Documentation")
        st.success("✅ Production Architecture")

    st.markdown("---")
    # -------------------------------------------------
# BUSINESS VALUE
# -------------------------------------------------

def show_business_value():
    """Display business value cards."""

    st.subheader("💼 Business Value")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.info(
"""
### ⚡ Faster Investigation

Retrieve similar complaints in seconds.
"""
        )

    with c2:

        st.info(
"""
### 📊 Better Decisions

Evidence-based complaint analysis.
"""
        )

    with c3:

        st.info(
"""
### 😊 Customer Experience

Faster complaint resolution.
"""
        )

    st.markdown("---")
    # -------------------------------------------------
# FOOTER
# -------------------------------------------------

def show_footer():
    """Display footer."""

    st.markdown(
"""
<div style="text-align:center">

## 👩‍💻 Developed by Haregeweyn Ataklt

Software Engineering Student

10 Academy AI Mastery Program

Financial Complaint RAG Chatbot

Built using

Python • Streamlit • FAISS • Sentence Transformers • RAG

</div>
""",
unsafe_allow_html=True,
)
    