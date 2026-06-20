from fastapi import FastAPI, UploadFile, File
from ai_engine import analyze_image
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {
        "message": "NWC Tabuk SafeSite API Running"
    }

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_image(file_path)
    return result
