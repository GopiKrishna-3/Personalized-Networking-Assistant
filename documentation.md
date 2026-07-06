# 🤝 Personalized Networking Assistant Documentation

This is a local copy of the project documentation for offline reference. For the most updated version, please refer to the main repository.

---

> **AI-powered conversation starter generator** that extracts themes from networking event descriptions, generates tailored icebreakers using GPT-2, and verifies facts via Wikipedia — all wrapped in a FastAPI + Streamlit web application.

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co)
[![pytest](https://img.shields.io/badge/Tested%20with-pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Running the Application](#-running-the-application)
- [API Reference](#-api-reference)
- [Testing](#-testing)
- [Design Notes](#-design-notes)
- [Author](#-author)
- [License](#-license)

---

## 🌟 Overview

Networking events can be daunting — knowing what to say is half the battle. The **Personalized Networking Assistant** is an AI-powered web app that generates smart, tailored conversation starters for professional and networking events.

### How It Works

1. **You describe the event** — paste the event description or summary.
2. **AI extracts themes** — DistilBERT identifies the key professional themes in the description.
3. **AI generates starters** — GPT-2 creates context-aware conversation prompts based on those themes.
4. **You verify facts** — Wikipedia lookups let you fact-check any topic before you walk into the room.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🏷️ **Theme Extraction** | DistilBERT identifies the key professional themes from an event description |
| 💬 **Conversation Starters** | GPT-2 generates context-aware conversation prompts tailored to those themes |
| 🔍 **Fact Verification** | Wikipedia API lookups to verify topics, technologies, or concepts before an event |
| ⚡ **FastAPI Backend** | Interactive Swagger docs auto-generated at `/docs` |
| 🎨 **Streamlit Frontend** | Simple, interactive web interface for generating and browsing starters |
| 🧪 **Mocked Test Suite** | Tests run against mocked pipelines — no model downloads or network calls needed |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend API** | FastAPI + Uvicorn | Async REST API serving the AI pipeline |
| **Theme Extraction** | DistilBERT | Identify professional themes in event descriptions |
| **Text Generation** | GPT-2 | Generate natural, context-aware conversation starters |
| **Fact Checking** | Wikipedia API | Verify topics, technologies, or concepts on demand |
| **Frontend** | Streamlit | Interactive web dashboard |
| **Testing** | pytest | Unit tests with mocked pipelines for fast, offline runs |

---

## 🏗️ Architecture

### System Overview

```
┌───────────────────────────────────────────────────────────┐
│                  FRONTEND (Streamlit)                     │
│                 frontend/app.py — port 8501                │
└───────────────────────────┬─────────────────────────────────┘
                            │ HTTP/JSON
                            ▼
┌───────────────────────────────────────────────────────────┐
│               BACKEND (FastAPI + Uvicorn)                 │
│                backend.main:app — port 8000                │
│                                                             │
│   ┌────────────────┐  ┌────────────────┐  ┌─────────────┐ │
│   │  Event Theme    │  │   Conversation  │  │  Wikipedia   │ │
│   │  Extraction     │  │   Generation    │  │  Fact Check  │ │
│   │  (DistilBERT)   │  │    (GPT-2)      │  │              │ │
│   └────────────────┘  └────────────────┘  └─────────────┘ │
└───────────────────────────────────────────────────────────┘
```

### Request Lifecycle

```
User submits an event description in Streamlit
    │
    │  POST request to the FastAPI backend
    ▼
FastAPI backend
    │
    ├─ Step 1: Extract themes from the description (DistilBERT)
    ├─ Step 2: Generate conversation starters from those themes (GPT-2)
    └─ Step 3: Return themes + starters as JSON
         │
         ▼
Streamlit renders the themes and generated conversation starters
```

---

## 📁 Project Structure

```
Personalized-Networking-Assistant/
│
├── backend/                 # FastAPI application
│   └── main.py               # FastAPI entry point — run as backend.main:app
│
├── frontend/                 # Streamlit web interface
│   └── app.py                 # Streamlit entry point
│
├── tests/                    # Automated test suite (mocked pipelines)
│
├── .gitignore                # Git ignore rules
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

> Note: the backend and frontend packages contain the theme-extraction, text-generation, and fact-checking logic; refer to the source on GitHub for the current internal module breakdown.

---

## 🚀 Getting Started

### Prerequisites

| Requirement | Version | Check |
|------------|---------|-------|
| Python | 3.10+ | `python --version` |
| pip | Latest | `pip --version` |
| Internet connection | — | Required to download Hugging Face models and query the Wikipedia API |

### Step 1: Clone the Repository

```bash
git clone https://github.com/GopiKrishna-3/Personalized-Networking-Assistant.git
cd Personalized-Networking-Assistant
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv

# Activate — macOS / Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

You need **two terminals** — one for the backend, one for the frontend.

### Terminal 1: Start the FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

The backend runs at `http://localhost:8000`, with interactive API docs at `http://localhost:8000/docs`.

### Terminal 2: Start the Streamlit Frontend

```bash
streamlit run frontend/app.py
```

The frontend opens in your default browser at `http://localhost:8501`.

---

## 📡 API Reference

Base URL: `http://localhost:8000`

Full interactive documentation (Swagger UI) is available at `http://localhost:8000/docs` once the backend is running, including exact request/response schemas for each endpoint.

Based on the app's pipeline, the backend exposes endpoints to:

- **Extract themes** from an event description (DistilBERT)
- **Generate conversation starters** from those themes (GPT-2), as a full pipeline
- **Fact-check a topic** via the Wikipedia API

For exact endpoint paths and payloads, check `/docs` — it reflects the live schema straight from the code.

---

## 🧪 Testing

```bash
pytest
```

Tests are configured to use mocked pipelines so they run quickly and don't require downloading models or network access to Wikipedia during test execution.

---

## 🧠 Design Notes

- **FastAPI + Streamlit split**: keeps the AI/API layer independent from the UI layer, so either can be swapped or scaled separately.
- **Mocked test pipelines**: keeps the test suite fast and runnable offline/in CI without pulling down large model weights.
- **Wikipedia-backed fact-checking**: lets users verify a topic on the spot instead of relying purely on generated text.

---

## 👤 Author

- **GopiKrishna-3** — [GitHub Profile](https://github.com/GopiKrishna-3)

---

## 📄 License

No license file is currently published in the repository. Check the repository directly for the latest licensing status before reuse.
