class Card:
    def __init__(self, target_word, sentence, translation, definitions):
        self.__target_word = target_word  # Atributo privado
        self.__sentence = sentence
        self.__translation = translation
        self.__definitions = definitions

    # Métodos getters
    def get_target_word(self):
        return self.__target_word

    def get_sentence(self):
        return self.__sentence

    def get_translation(self):
        return self.__translation

    def get_definitions(self):
        return self.__definitions

    def show_info(self):
        print(f"Target Word: {self.__target_word}")
        print(f"Sentence: {self.__sentence}")
        print(f"Translation: {self.__translation}")