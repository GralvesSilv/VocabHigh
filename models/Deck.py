import csv
import os
import random
from models.Card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def show_deck_details(self):
        deck_details_text = ""
        for index, card in enumerate(self.cards, start=1):
            deck_details_text += (
                f"Card {index}:\n"
                f"  Target Word: {card.get_target_word()}\n"
                f"  Sentence: {card.get_sentence()}\n"
                f"  Translation: {card.get_translation()}\n"
                f"  Definitions: {card.get_definition()}\n\n"
            )
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
            return
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                target_word, sentence, translation, definition = row
                card = Card(target_word, sentence, translation, definition)
                self.add_card(card)

    def get_random_card(self):
        if not self.cards:
            return None
        return random.choice(self.cards)
