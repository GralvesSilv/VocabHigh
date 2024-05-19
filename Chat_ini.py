import google.generativeai as genai


class Chat_ini:
    def __init__(self, api_key, safety_settings, generation_config, system_instruction):
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest",
                                      generation_config=generation_config,
                                      safety_settings=safety_settings,
                                      system_instruction=system_instruction)
        self.chat = model.start_chat(history=[])

    def send_message(self, prompt):
        return self.chat.send_message(prompt)
