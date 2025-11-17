# 🧠 AI Text Summarization API (FastAPI + HuggingFace)

A lightweight, production-ready **Text Summarization REST API** built using **FastAPI** and **HuggingFace Inference API**.  
This project allows you to summarize text from:

✔ File path (local system)  
✔ Direct file upload  
✔ Multiple file uploads (TXT & PDF)  

It is designed as a simple demonstration of how to integrate LLMs with modern Python backend services.

---

## 📁 Project Structure

AI_Text_Summarization/
│
├── main.py # FastAPI application + endpoints
├── ai_text_summarize_model.py # HuggingFace model call
├── auto_decode.py # Safe text decoding (supports multi-encoding)
├── model/
│ └── FilePath.py # Pydantic model for file-path request
├── .env # API keys & configuration (you create this)
└── requirements.txt # Required Python libraries

## 🚀 Features

### ✔ Summaries using HuggingFace Model  
Uses `facebook/bart-large-cnn` via Inference API.

### ✔ 3 REST Endpoints  
1️⃣ `/AI-Text-Summarize` – Summarize text from a file path  
2️⃣ `/upload-and-summarize` – Upload a single file  
3️⃣ `/upload-multiple-summarize` – Upload and summarize multiple files (TXT/PDF)

### ✔ File Handling  
- TXT files: auto-detect encoding using `chardet`  
- PDF files: extracted using `PyPDF2`  
- Validation:
  - Max file count  
  - Max file size  
  - Allowed extensions  

### ✔ Clean Code & Modular Architecture  
Everything is separated for readability and maintainability.

---

## ⚙️ Setup Instructions

Follow these steps to run the project on your machine.

---

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd AI_Text_Summarization

2️⃣ Create a Virtual Environment
This ensures isolated package installation.

For Windows:
python -m venv venv
venv\Scripts\activate

For Linux/Mac:
python3 -m venv venv
source venv/bin/activate


3️⃣ Install Dependencies
pip install -r requirements.txt

You should see packages like FastAPI, PyPDF2, Python-dotenv, and HuggingFace Hub being installed.

4️⃣ Create a HuggingFace API Token


1.Login to HuggingFace
2.Go to Settings → Access Tokens
3.Create a New Token
4.Permissions → Enable Inference
5.Copy the token



5️⃣ Create a .env File
Inside the project folder:
HUGGINGFACEHUB_API_TOKEN = "<your-token>"

# Multiple file configuration
MAX_FILES = 5
MAX_FILE_SIZE = 2000000
ALLOWED_EXTENSIONS = [".txt", ".pdf"]


6️⃣ Run the FastAPI Server
uvicorn main:app --reload

Now open:
📌 API Docs: http://localhost:8000/docs
📌 ReDoc: http://localhost:8000/redoc

🧪 API Endpoints Overview
🔹 1. Summarize by File Path
POST /AI-Text-Summarize
{
  "file_path": "C:/Users/.../example.txt"
}


🔹 2. Upload & Summarize Single File
POST /upload-and-summarize
Accepts: .txt, .pdf

🔹 3. Upload Multiple Files
POST /upload-multiple-summarize
✔ Supports TXT (auto-decoded)
✔ Supports PDF via PyPDF2
✔ Generates summary for each file

🧠 Tech Used


FastAPI – REST framework


HuggingFace Inference API – Text summarization


PyPDF2 – PDF text extraction


Chardet – Smart encoding detection


Pydantic – Request validation


Python-dotenv – Environment handling



📌 Future Improvements (Optional Roadmap)


Add authentication with API keys


Add frontend (React/Streamlit) for file upload


Add more models (T5, Pegasus, Llama)


Convert into real production workflow using Docker + Azure



🙌 Author
Abhishek Kumar
Python Developer | AI-ML Engineer
