from fastapi import FastAPI, UploadFile, File
from ai_engine import analyze_image
import shutil

app = FastAPI(
    title="NWC Tabuk SafeSite API"
)

@app.get("/")
def root():
    return {
        "message": "NWC Tabuk SafeSite API Running"
    }

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_image(file_path)

    return result
