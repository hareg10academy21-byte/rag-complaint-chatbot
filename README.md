# 🏦 Finance Complaint RAG Chatbot

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-green)
![PyTest](https://img.shields.io/badge/Tests-6%20Passed-success)
![CI/CD](https://img.shields.io/badge/GitHub-Actions-orange)

An AI-powered **Retrieval-Augmented Generation (RAG)** application that helps financial institutions analyze customer complaints using semantic search and artificial intelligence.

The system retrieves similar historical complaints using vector embeddings and FAISS, helping analysts investigate complaints faster, reduce manual effort, and improve customer service decisions.

---

# 📌 Project Overview

Financial institutions receive thousands of customer complaints every year. Searching through previous complaints manually is time-consuming and inefficient.

This project solves this problem by building an AI complaint analysis platform that:

- Converts complaints into semantic embeddings
- Stores vectors using FAISS
- Retrieves similar historical complaints
- Provides evidence-based complaint analysis
- Presents results through an interactive Streamlit dashboard

The application demonstrates how AI can improve operational efficiency in the financial sector.

---

# 🎯 Business Problem

Financial analysts need to quickly understand customer complaints and identify similar previous cases.

Traditional manual searching:

- Requires significant time
- Increases operational cost
- Makes finding similar cases difficult
- Can lead to inconsistent responses

The Finance Complaint RAG Chatbot provides a faster and more intelligent approach using AI-powered search.

---

# 🚀 Original Project Achievements

The original project successfully implemented:

✅ Financial complaint preprocessing  
✅ Text cleaning and preparation  
✅ Complaint chunking  
✅ Sentence Transformer embeddings  
✅ FAISS vector database  
✅ Semantic similarity search  
✅ Retrieval-Augmented Generation pipeline  
✅ Basic chatbot functionality  

---

# ⭐ B9W12 Project Improvements

This project was improved from a prototype into a more production-ready AI application.

## 1. Modular Software Architecture

The project was reorganized into a clean `src/` structure:

```
src/
│
├── dashboard.py
├── config.py
├── constants.py
├── preprocessing.py
├── chunking.py
├── embedding.py
├── vector_store.py
├── retriever.py
├── rag_pipeline.py
├── llm.py
└── utils.py
```

Benefits:

- Better maintainability
- Easier debugging
- Reusable components
- Professional software structure

---

# 2. Code Quality Improvements

Implemented:

✅ Python type hints  
✅ Function docstrings  
✅ Constants management  
✅ Configuration management  
✅ Utility functions  
✅ Better separation of responsibilities  

---

# 3. Testing and Reliability

Added automated testing using PyTest.

Current test result:

```
============== 6 passed in 138.63s ==============
```

Test coverage includes:

- Preprocessing tests
- Utility tests
- Retrieval tests
- Embedding tests
- RAG pipeline tests

---

# 4. CI/CD Pipeline

Configured GitHub Actions to automatically:

- Install dependencies
- Validate Python code
- Run automated tests

This ensures code quality whenever changes are pushed.

---

# 5. Interactive Streamlit Dashboard

The project now includes a professional dashboard with:

- Complaint search interface
- Retrieved complaint evidence
- AI analysis section
- Business impact explanation
- System architecture visualization
- Project quality overview

---

# 📸 Application Screenshots

## Dashboard Overview
```
#  Interactive Streamlit Dashboard

The project now includes a professional dashboard with:

- Financial complaint search interface
- Semantic retrieval of similar complaints
- Retrieved complaint evidence display
- Business impact explanation
- System architecture visualization
- Engineering quality overview
- Downloadable search results

The dashboard helps financial analysts quickly explore historical complaint cases.
docs/images/businessImpact.png
```


![Dashboard Overview](docs/images/businessImpact.png)


## Search Results
screenshot showing retrieved complaints:

```
docs/images/headtitleand-sadbar.png
```

![Search Results](docs/images/headtitleand-sadbar.png)


## Architecture Section

screenshot of architecture visualization:

```
docs/images/systemAchitecture.png
```

Example:

![Architecture](docs/images/systemAchitecture.png)

---

# 🏗 System Architecture

```
User Complaint
       |
       ↓
Sentence Transformer
       |
       ↓
Embedding Vector
       |
       ↓
FAISS Vector Database
       |
       ↓
Similar Complaint Retrieval
       |
       ↓
RAG Pipeline
       |
       ↓
AI Response
```

---

# 🛠 Technology Stack

## Programming

- Python

## AI / Machine Learning

- Sentence Transformers
- Transformers
- FAISS
- Natural Language Processing

## Application

- Streamlit

## Testing

- PyTest

## Engineering

- Git
- GitHub Actions CI/CD

---

# 📂 Project Structure

```
rag-complaint-chatbot/

│
├── app.py
├── README.md
├── requirements.txt
├── improvement_plan.md
├── roadmap.md
│
├── src/
│   ├── dashboard.py
│   ├── retriever.py
│   ├── rag_pipeline.py
│   ├── embedding.py
│   ├── preprocessing.py
│   ├── config.py
│   └── utils.py
│
├── tests/
│   ├── test_embedding.py
│   ├── test_preprocessing.py
│   ├── test_retriever.py
│   ├── test_rag_pipeline.py
│   └── test_utils.py
│
└── .github/
    └── workflows/
        └── python.yml
```

---

# ⚙ Installation Guide

Clone the repository:

```bash
git clone https://github.com/hareg10academy21-byte/rag-complaint-chatbot.git
```

Move into the project folder:

```bash
cd rag-complaint-chatbot
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🧪 Running Tests

Run:

```bash
pytest tests -v
```

Expected result:

```
6 passed
```

---

# 💼 Business Impact

This system provides:

✅ Faster complaint investigation  
✅ Reduced manual search effort  
✅ Improved analyst productivity  
✅ Evidence-based decision making  
✅ Better customer experience  

---

## 📊 Success Metrics

The success of the project improvements will be evaluated using the following measurable criteria:

| **Metric** | **Target Outcome** |
|---|---|
| 🏗️ **Code Organization** | Maintain a clean and modular `src/` based architecture with separated components for dashboard, retrieval, RAG pipeline, configuration, and utility functions. |
| 🧪 **Test Coverage** | Achieve a minimum of **5 automated tests passing** to validate core project functionality. |
| ⚙️ **Application Reliability** | Implement an automated **GitHub Actions CI pipeline** to run quality checks and tests on code changes. |
| 💻 **User Interface** | Provide a functional **Streamlit dashboard** for complaint search, retrieved evidence display, and AI response visualization. |
| 📚 **Documentation Quality** | Provide complete documentation including project overview, installation steps, usage instructions, architecture, and technical details. |
| 🔍 **Search Performance** | Retrieve relevant historical complaints within seconds using semantic search with FAISS and Sentence Transformer embeddings. |
| 😊 **User Experience** | Deliver a clear and interactive interface that presents complaint evidence and AI-generated insights effectively. |
---

# 👩‍💻 Author

**Haregeweyn Ataklt**

Software Engineering Student  
10 Academy AI Mastery Program

---
# 📈 Current Project Status

| Component | Status |
|---|---|
| Modular Architecture | ✅ Completed |
| Type Hints and Documentation | ✅ Completed |
| Unit Testing | ✅ 6 Tests Passing |
| GitHub Actions CI/CD | ✅ Completed |
| Streamlit Dashboard | ✅ Completed |
| Semantic Search Retrieval | ✅ Completed |
| Production Documentation | ✅ Completed | 

# 🔮 Future Improvements

Possible future enhancements:

- Deploy application to cloud platform
- Add advanced LLM integration
- Add user authentication
- Add analytics dashboard
- Improve response generation quality
