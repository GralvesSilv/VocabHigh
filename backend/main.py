from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 🛡️ CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ou ["*"] para testes locais
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WordRequest(BaseModel):
    word: str

@app.post("/flashcard")
def generate_flashcard(request: WordRequest):
    try:
        return {"flashcard": f"Definição de '{request.word}' gerada pela IA"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
