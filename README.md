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

### 🧠 Architecture & Design Decisions

### Separation of Concerns

This project follows a clean backend architecture by separating responsibilities across different layers:

* **API Layer (`main.py`)**

  * Handles HTTP requests and responses
  * Orchestrates flow between components

* **Service Layer (`ai_service.py`)**

  * Handles interaction with the LLM (Ollama)
  * Keeps AI logic isolated and reusable

* **Memory Layer (`memory.py`)**

  * Manages conversation history
  * Enables context-aware responses

### Why this matters

* Improves code readability and maintainability
* Makes the system scalable
* Follows real-world backend design patterns

### Key Concept

LLMs do not have memory by default.
This project simulates memory by injecting past conversation into the prompt before sending it to the model.


## 🚀 Future Improvements

* Chat memory (context-aware AI)
* Notes storage & summarization
* Flutter frontend integration
* Deployment on cloud (AWS / GCP)

---

⭐ This project demonstrates building an AI-powered backend without relying on paid APIs.
