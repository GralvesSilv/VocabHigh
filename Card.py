class Card:
    def __init__(self, target_word, sentence, translation, definition):
        self.__target_word = target_word  # Atributo privado
        self.__sentence = sentence
        self.__translation = translation
        self.__definition = definition

    # Métodos getters
    def get_target_word(self):
        return self.__target_word

    def get_sentence(self):
        return self.__sentence

    def get_translation(self):
        return self.__translation

    def get_definition(self):
        return self.__definition
