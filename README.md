# AI Notes 🚀

An AI-powered system built using FastAPI and a locally hosted LLM (LLaMA 3 via Ollama).

## 🔥 Features

* AI text generation using local LLM (no API cost)
* FastAPI-based scalable backend
* Clean modular architecture (routes, services, schemas)
* Ready for frontend integration (Flutter)

## 🧠 Tech Stack

* Python
* FastAPI
* Ollama (LLaMA 3)
* Uvicorn

## ⚙️ Setup Instructions

### 1. Start Ollama

```bash
ollama serve
```

### 2. Run Backend

```bash
cd backend
uvicorn main:app --reload
```

### 3. Test API

Open:

```
http://127.0.0.1:8000/docs
```

## 🚀 Future Improvements

* Chat memory (context-aware AI)
* Notes storage & summarization
* Flutter frontend integration
* Deployment on cloud (AWS / GCP)

---

⭐ This project demonstrates building an AI-powered backend without relying on paid APIs.
