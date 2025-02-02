from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from the provided JSON file
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

@app.get("/api")
def get_marks(name: str):
    marks_list = [entry["marks"] for entry in data if entry["name"] == name]
    return {"marks": marks_list}

@app.get("/")
def root():
    return {"message": "Welcome to the student marks API!"}
