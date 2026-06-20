from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "NWC Tabuk SafeSite API Running"
    }
