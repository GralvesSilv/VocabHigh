import streamlit as st
import google.generativeai as genai

from Card import Card
from Deck import Deck
from Ai_config import Ai_config
import Ai_settings

st.set_page_config(page_title="VocabHigh")

api_key = st.text_input("insira a APIKEY", type="password")
chat = Ai_config(api_key, Ai_settings.safety_settings, Ai_settings.generation_config, Ai_settings.system_instruction)
deck_filename = 'deck.csv'

with st.container():
    st.title("VocabHigh")
    prompt = st.text_input("Digite uma palavra em inglês")
    deck = Deck()
    deck.load_from_file(deck_filename)

    if prompt:
        response = chat.send_message(prompt)
        st.write(response.text)

        # Dividindo a string em substrings usando a vírgula como separador
        values = response.text.split(',')

        # Atribuindo os valores às variáveis correspondentes
        target_word = values[0].strip()
        sentence = values[1].strip()
        translation = values[2].strip()
        definitions = values[3].strip()
        card = Card(target_word, sentence, translation, definitions)
        deck.add_card(card)
        deck.save_to_file(deck_filename)

        st.write(deck.show_deck_details())
