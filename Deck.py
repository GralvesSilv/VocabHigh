class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def show_deck_target_words(self):
        target_words_text = ""  # Inicializa uma string vazia para armazenar as target_words

        for index, card in enumerate(self.cards, start=1):
            target_words_text += f"Card {index}: {card.get_target_word()}\n"  # Adiciona a target_word ao texto

        return target_words_text  # Assumindo que a classe Card tem um método show_info()