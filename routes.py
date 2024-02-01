from fastapi import FastAPI
import main

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "result"}

@app.get('/question')
async def question():
    return {"question": "question"}