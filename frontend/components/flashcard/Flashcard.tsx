'use client';

import React, {useState} from "react";

type FlashcardProps = {
    target_word: string;
    sentence: string;
    translation: string;
    definition: string;
};

export default function Flashcard({ target_word, sentence, translation, definition}: FlashcardProps){

    const [showAnswer, setShowAnswer] = useState(false);

    return (
        <div className="mt-6 p-6 border bg-white rounded-2xl shadow-md max-w-md mx-auto">
      <h2 className="text-xl font-semibold mb-2 text-blue-700">{target_word}</h2>
      <p className="italic mb-4 text-gray-700">"{sentence}"</p>

      {!showAnswer ? (
        <button
          onClick={() => setShowAnswer(true)}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
        >
          Mostrar resposta
        </button>
      ) : (
        <div className="mt-4 text-gray-800">
          <p><strong>Tradução:</strong> {translation}</p>
          <p><strong>Definição:</strong> {definition}</p>
        </div>
      )}
    </div>
    )

}