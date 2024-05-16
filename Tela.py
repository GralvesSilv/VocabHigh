import streamlit as st
import google.generativeai as genai

API_KEY = "AIzaSyDgi6r54JYIOks09va5QDx4AYRwYq17B2U"

genai.configure(api_key=API_KEY)
generation_config = {
    "temperature": 1,
}
safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
chat = model.start_chat(history=[])
chat.send_message("""
Você é um professor de inglês para crianças brasileiras. Use palavras simples.
1. Enviarei uma palavra em ingês.
2. gere uma frase com essa palavra.
    frase simples
    não use mais que 15 palavras
3. A frase deve começar em ingês e ser seguida da tradução para o portugês.
4. Formate sua resposta no formato CSV.
    a formatação deve ser assim: palavra em inglês, frase em inglês que aplica a palavra, palavra em inglês traduzida para o portugês, frase com a palavra traduzida para o portuês.
    siga este exemplo:
          pergunta: love
          resposta: love, I love you, amor, eu amo você
          pergunta: book
          resposta: book, That book is interesting, livro, aquele livro é interesante
5. Não use vírgulas no meio das frases, pois arruinará a formatação. Se a fraase criada tiver vírgula, substitua por ; ou apenas um ponto.
6. Não inclua mais nenhuma instrução ou explicação.
""")
st.set_page_config(page_title="VocabHigh")

with st.container():
    st.title("VocabHigh")
    prompt = st.text_input("Digite uma palavra em inglês")
    if prompt:
        response = chat.send_message(prompt)
        st.write(response.text)