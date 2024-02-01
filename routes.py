from fastapi import FastAPI
import main

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "result"}

@app.get('/question')
async def question():
    return {"question": "question"}

@app.get('/job_posting/{id}')
async def get_job_posting(id):
    return {"id": id}

@app.post('/job_posting')
async def get_job_posting():
    return {"job posting": "null"}

