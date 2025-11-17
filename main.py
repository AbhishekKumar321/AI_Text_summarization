from fastapi import FastAPI, UploadFile, File,HTTPException

from ai_text_summa import ai_model
import os,io
from model.FilePath import FilePath
from dotenv import load_dotenv
import PyPDF2
from auto_decode import decode_text_safely
app = FastAPI()
# load dotenv
load_dotenv()



MAX_FILES = int(os.getenv("MAX_FILES"))           # maximum number of files per request
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE"))  # maximum file size in bytes (~2 MB)
ALLOWED_EXTENSIONS =os.getenv("ALLOWED_EXTENSIONS")  # allowed file types




# provide path of file and get summarize
@app.post("/AI-Text-Summarize")
async def summarize_text(payload: FilePath):
    file_path = payload.file_path 
    if os.path.exists(file_path):
        with open(file_path,"r",encoding="utf-8") as f:
            raw_data = f.read()
            ai_summarize = ai_model(raw_data)
        return {"summarize_text": f"{ai_summarize}"}
    else:
        return {"message":"File not Found"}
    

#  directly upload file and get summarization
@app.post("/upload-and-summarize")
async def upload_and_summarize(file: UploadFile = File(...)):
    # Read file content as string
    raw_data = await file.read()
    raw_text = raw_data.decode("utf-8")  # decode bytes to string

    # Call your AI model
    ai_summarize = ai_model(raw_text)

    return {"summarized_text": ai_summarize}

# upload multiple file
@app.post("/upload-multiple-summarize")
async def upload_multiple_summarize(files: list[UploadFile] = File(...)):

    if len(files) > MAX_FILES:
        raise HTTPException(status_code=400, detail=f"Maximum {MAX_FILES} files allowed.")

    results = []

    for file in files:
         # Validate file extension
        if not any(file.filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
            raise HTTPException(
                status_code=400, detail=f"File '{file.filename}' has invalid type."
            )
        
        # -----------------------------------
        # HANDLE TEXT FILE
        # -----------------------------------
        if file.filename.endswith(".txt"):
            raw_data = await file.read()            # Read file as bytes
            raw_text = decode_text_safely(raw_data) # Decode to string
            summary = ai_model(raw_text)            # Call your summarization function
            results.append({
            "filename": file.filename,
            "summarized_text": summary
        })
        
        # -----------------------------------
        # HANDLE PDF FILE
        # -----------------------------------
        elif file.filename.endswith(".pdf"):
            raw_data = await file.read()
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(raw_data))
            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text() or ""
            summary = ai_model(pdf_text)   
            
            results.append({
                "filename": file.filename,
                "summarized_text": summary
            })

    return {"summaries": results}