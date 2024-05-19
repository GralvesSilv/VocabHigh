import streamlit as st
from Card import Card
from Deck import Deck
from Chat_ini import Chat_ini
import Ai_settings

# Carrega o deck antes de inicializar o estado
deck_filename = 'deck.csv'
deck = Deck()
deck.load_from_file(deck_filename)


# Função para obter um novo card
def get_new_card(deck):
    return deck.get_random_card() if deck.cards else None


# Função para mostrar a resposta
def show_answer():
    st.session_state.show_answer = True
    st.experimental_rerun()


# Função para pegar um novo card
def next_card():
    st.session_state.card = get_new_card(deck)
    st.session_state.show_answer = False
    st.experimental_rerun()


# Função para interagir com o chatbot
def chat_with_bot(chat, prompt):
    response = chat.send_message(prompt)
    st.write(response.text)
    return [item.strip() for item in response.text.split(',')]


# Função principal para executar o aplicativo
def main():
    st.set_page_config(page_title="VocabHigh")

    api_key = st.text_input("Insira a APIKEY", type="password")
    chat = Chat_ini(api_key, Ai_settings.safety_settings, Ai_settings.generation_config,
                    Ai_settings.system_instruction)

    st.title("VocabHigh")

    # Inicializa o estado do card e show_answer se ainda não estiverem definidos
    if 'card' not in st.session_state or not st.session_state.card:
        st.session_state.card = get_new_card(deck)

    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False

    with st.container():
        prompt = st.text_input("Digite uma palavra em inglês")
        if prompt:
            values = chat_with_bot(chat, prompt)
            if len(values) == 4:
                target_word, sentence, translation, definitions = values
                card = Card(target_word, sentence, translation, definitions)
                deck.add_card(card)
                deck.save_to_file(deck_filename)

    with st.container():
        st.subheader("Flashcards")
        card = st.session_state.card

        if card:
            st.write(f"Target Word: {card.get_target_word()}")
            st.write(f"Sentence: {card.get_sentence()}")

            if not st.session_state.show_answer:
                if st.button("Show Answer"):
                    show_answer()

            if st.session_state.show_answer:
                st.write(f"Translation: {card.get_translation()}")
                st.write(f"Definition: {card.get_definition()}")
                if st.button("Next Card"):
                    next_card()
        else:
            st.write("O deck está vazio. Adicione novos flashcards para começar.")


if __name__ == "__main__":
    main()
