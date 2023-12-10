# from chatgpt
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import subprocess
import os
from picamera2 import Picamera2, Preview
import time
picam2 = Picamera2()

# app instance
app = FastAPI()

# define a route for uploading an image
@app.post('/upload')
async def upload_image(file: UploadFile = File(None)):
    temp_file = f'{file.filename}'
    with open(temp_file, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {'filename':file.filename, 'size': os.path.getsize(temp_file)}

# define a route for downloading an image
@app.get('/download/{filename}')
async def download_image(filename:str):
    
    picam2.start()
    time.sleep(0.1)
    picam2.capture_file("test.jpg")
    subprocess.Popen(
        'curl -X POST -F "file=@test.jpg" http://127.0.0.1:8000/upload',
        stdout = subprocess.PIPE, shell = True
        )
    temp_file = f'{filename}'
    if os.path.exists(temp_file):
        return FileResponse(temp_file)
    else:
        return {'error': 'File not found'}
