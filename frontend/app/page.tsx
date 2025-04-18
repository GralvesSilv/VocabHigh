'use client'

import Flashcard from '@/components/flashcard/Flashcard';
import { useState } from 'react';


type FlashcardData = {
  target_word: string;
  sentence: string;
  translation: string;
  definition: string;
}

export default function Home() {
  const [word, setWord] = useState('');
  const [apiKey, setApikey] = useState('');
  const [flashcard, setFlashcard] = useState<FlashcardData | null>(null);

  const handleSubmit = async () => {
    const res = await fetch('http://localhost:8000/flashcard', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ word, api_key: apiKey }),
    });

    const data = await res.json();
    setFlashcard(data.flashcard);
  };

  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold mb-4">Gerador de Flashcards</h1>
      
      <input
        type="password"
        value={apiKey}
        onChange={(e) => setApikey(e.target.value)}
        className="border p-2 mb-2 block w-full"
        placeholder="Insira sua API Key"
      />

      <input
        type="text"
        value={word}
        onChange={(e) => setWord(e.target.value)}
        className="border p-2 mr-2"
        placeholder="Digite uma palavra"
      />

      <button onClick={handleSubmit} className="bg-blue-600 text-white px-4 py-2">
        Gerar
      </button>
      
      {flashcard && <Flashcard {...flashcard} />}

    </main>
  );
}
