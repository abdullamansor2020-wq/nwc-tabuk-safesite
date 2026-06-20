from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from ai_engine import analyze_image

app = FastAPI(title="NWC Tabuk SafeSite API")

@app.get("/")
def root():
    return {"message": "NWC Tabuk SafeSite API Running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()

    image = Image.open(
        io.BytesIO(contents)
    ).convert("RGB")

    return analyze_image(image)
