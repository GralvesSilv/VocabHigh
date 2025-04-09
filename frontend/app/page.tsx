'use client'

import { useState } from 'react';

export default function Home() {
  const [word, setWord] = useState('');
  const [flashcard, setFlashcard] = useState('');

  const handleSubmit = async () => {
    const res = await fetch('http://localhost:8000/flashcard', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ word }),
    });
    const data = await res.json();
    setFlashcard(data.flashcard);
  };

  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold mb-4">Gerador de Flashcards</h1>
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
      {flashcard && (
        <div className="mt-4 p-4 border bg-gray-100">
          <strong>Flashcard:</strong>
          <p>{flashcard}</p>
        </div>
      )}
    </main>
  );
}
