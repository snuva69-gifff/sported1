from fastapi import FastAPI
from fastapi.responses import Response
import requests
import os

app = FastAPI()

HF_TOKEN = os.getenv("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")

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

@app.post("/generate")
def generate(prompt: str):
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    return Response(content=response.content, media_type="image/png")