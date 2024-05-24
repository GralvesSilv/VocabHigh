# VocabHigh: Domine o Inglês com a ajuda da Inteligência Artificial
<div align="center">
    <img src="icon.jpeg" width="500px"/>
</div>

## Sobre o Projeto
**VocabHigh** é uma aplicação web que utiliza inteligência artificial para gerar flashcards de palavras em inglês, ajudando usuários a expandirem seu vocabulário. No momento, o foco principal é a criação de flashcards, mas futuros desenvolvimentos incluirão funcionalidades adicionais, como correção gramatical, melhoria da pronúncia, e um chatbot equipado com ferramentas de áudio para prática de escuta e conversação e suporte para mais línguas.

## Funcionalidades Principais

* **Geração de Flashcards com IA:** Digite uma palavra em inglês e deixe a IA gerar uma frase de exemplo, tradução e definição para criar flashcards personalizados.
  
* **Correção Gramatical:** (Funcionalidade Futuras) Receba feedback e correções para melhorar sua gramática em inglês.

* **Melhoria de Pronúncia:** (Funcionalidade Futuras) Utilize ferramentas de áudio para praticar e aperfeiçoar sua pronúncia.

* **Chatbot Educacional:** (Funcionalidade Futuras) Converse com um chatbot movido a IA que pode ajudá-lo a praticar a escuta e a conversação em inglês.

## Tecnologias Utilizadas

* **Python:** Principal linguagem de programação utilizada para o desenvolvimento do projeto.
* **Streamlit**Framework para criação de aplicações web interativas e de fácil uso
* **Google Generative AI (Gemini):** API de IA generativa da Google permite criar conteúdos ricos e personalizados com base em prompts fornecidos pelo usuário.

## Engenharia de Prompt
 **Técnicas de Prompt Engineering utilizadas para otimizar os prompts enviados à IA generativa, garantindo respostas mais precisas e relevantes.**
* **Few-shot Learning:** O modelo recebe alguns exemplos antes de realizar a tarefa, ajudando a melhorar a precisão.
* **Chain-of-thought Prompting:** O modelo é incentivado a pensar passo a passo, detalhando seu raciocínio antes de chegar à resposta final.
* **Instruction Tuning:** O modelo é treinado ou ajustado para seguir instruções específicas, melhorando sua capacidade de responder de acordo com prompts detalhados.
* **Contextual Prompting:** Fornecer um contexto detalhado ou uma narrativa antes da pergunta principal para guiar a resposta do modelo.
* **Role-playing Prompting:** Pedir ao modelo para assumir um papel ou persona específica para fornecer respostas mais alinhadas a essa perspectiva.
*  **Negative Prompting:** Indicar explicitamente o que não se quer na resposta para evitar informações irrelevantes.

  ## Como Começar
  1. **Clone o repositório:**

```bash
git clone https://github.com/GralvesSilv/VocabHigh.git
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```
3. **Execute o aplicativo:**

```bash
streamlit run streamlit run Main.py
```

4. **Acesse o aplicativo:** Abra seu navegador e acesse `http://localhost:8501`.

5. **Obetenha sua chave de API:**

    * acesse https://aistudio.google.com/ e obtenha uma chave de API do Google Generative AI e insira no campo da APIKEY

## Contribua com o Projeto
VocabHigh é um projeto de código aberto, e contribuições são bem-vindas!

## Contato
[Linkedin](https://www.linkedin.com/in/gabriel-da-silva-alves-38b223254/)
