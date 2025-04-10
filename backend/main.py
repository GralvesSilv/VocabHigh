from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.Chat_ini import Chat_ini
from config import Ai_settings

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
    api_key: str

@app.post("/flashcard")
def generate_flashcard(request: WordRequest):
    try:
        
        print("requisição recebida:", request.word)

        chat = Chat_ini(request.api_key,
                        Ai_settings.safety_settings,
                        Ai_settings.generation_config,
                        Ai_settings.system_instruction
                    )
        prompt = request.word
        response = chat.send_message(prompt)

        return {"flashcard": response.text}
    
    except Exception as e:
        print("erro:", str(e))
        raise HTTPException(status_code=500, detail=str(e))
