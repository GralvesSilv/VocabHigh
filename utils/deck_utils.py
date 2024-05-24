import csv
import os
from models.Card import Card

def save_to_file(deck, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for card in deck.cards:
            writer.writerow([card.get_target_word(),
                             card.get_sentence(),
                             card.get_translation(),
                             card.get_definition()])

def load_from_file(deck, filename):
    if not os.path.exists(filename):
        return
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            target_word, sentence, translation, definition = row
            card = Card(target_word, sentence, translation, definition)
            deck.add_card(card)
