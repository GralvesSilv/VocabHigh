from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class WordRequest(BaseModel):
    word: str

@app.post("/flashcard")
def generate_flashcard(request: WordRequest):
    try:
        return {"flashcard": f"Definição de '{request.word}' gerada pela IA"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
