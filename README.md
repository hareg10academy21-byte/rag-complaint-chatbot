# 💬 CrediTrust Intelligent Complaint Analysis (RAG System)

## 🚀 Overview

This project is a Retrieval-Augmented Generation (RAG) system designed for CrediTrust Financial to analyze and extract insights from customer complaints across financial products.

It enables non-technical users to ask natural language questions and receive **evidence-based answers grounded in real complaint data**.

---

## 🧠 Problem Statement

CrediTrust receives thousands of customer complaints across:

- Credit Cards
- Personal Loans
- Savings Accounts
- Money Transfers

Manual analysis is slow, inconsistent, and does not scale.

This system solves that by enabling:
- Semantic search over complaint data
- AI-generated insights
- Evidence-backed responses

---

## 🎯 Objectives

- Reduce complaint analysis time from days → minutes  
- Enable non-technical users to query complaints  
- Improve decision-making using AI-powered insights  
- Build scalable RAG architecture  

---

## 🏗️ System Architecture

```mermaid
flowchart TD
User --> UI[Streamlit UI]
UI --> RAG[RAG Pipeline]
RAG --> RET[FAISS Retriever]
RET --> EMB[MiniLM Embedding Model]
RET --> VEC[Vector Search]
VEC --> CHUNK[Top-K Complaint Chunks]
CHUNK --> PROMPT[Prompt Engineering]
PROMPT --> LLM[FLAN-T5 Model]
LLM --> ANSWER[Final Answer]
CHUNK --> SOURCE[Source Display]