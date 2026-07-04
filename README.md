# Personalized Networking Assistant

An AI-powered web app that generates smart, tailored conversation starters for professional/networking events. It extracts themes from event descriptions using DistilBERT, generates context-aware conversation prompts using GPT-2, and verifies facts using the Wikipedia API.

## Requirements
- Python 3.10+
- Internet connection (for Hugging Face models download and Wikipedia API)

## Setup
1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
The application consists of a FastAPI backend and a Streamlit frontend. You need to run both in separate terminal windows.

### Start the Backend
```bash
uvicorn backend.main:app --reload
```
The backend will run on `http://localhost:8000`.
You can view the interactive API documentation at `http://localhost:8000/docs`.

### Start the Frontend
```bash
streamlit run frontend/app.py
```
The frontend will open in your default browser at `http://localhost:8501`.

## Testing
Run the test suite with `pytest`:
```bash
pytest
```
Tests are configured to use mocked pipelines so they run quickly and do not require downloading models or network access to Wikipedia during test execution.
