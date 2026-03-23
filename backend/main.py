from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import os

from utils.downloader import download_file
from utils.ffmpeg_service import process_media

app = FastAPI()

TEMP_DIR = "temp"
OUTPUT_DIR = "output"

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

class RequestModel(BaseModel):
    url: str
    operation: str


@app.post("/process")
def process(request: RequestModel):
    try:
        file_id = str(uuid.uuid4())
        input_path = f"{TEMP_DIR}/{file_id}.mp4"

        # Step 1: Download
        download_file(request.url, input_path)

        # Step 2: Process
        output_path = process_media(input_path, request.operation, file_id)

        return {
            "status": "success",
            "output": output_path
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))