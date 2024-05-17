import csv
import os
from Card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def show_deck_details(self):
        deck_details_text = ""  # Inicializa uma string vazia para armazenar as informações das cartas

        for index, card in enumerate(self.cards, start=1):
            deck_details_text += (
                f"Card {index}:\n"
                f"  Target Word: {card.get_target_word()}\n"
                f"  Sentence: {card.get_sentence()}\n"
                f"  Translation: {card.get_translation()}\n"
                f"  Definitions: {card.get_definition()}\n\n"
            )  # Adiciona todas as informações da carta ao texto

        return deck_details_text

    def save_to_file(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for card in self.cards:
                writer.writerow([card.get_target_word(),
                                 card.get_sentence(),
                                 card.get_translation(),
                                 card.get_definition()])

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            return  # Se o arquivo não existe, simplesmente retorna
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                target_word, sentence, translation, definition = row
                card = Card(target_word, sentence, translation, definition)
                self.add_card(card)
