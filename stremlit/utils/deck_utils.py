import csv
import os
from models.Card import Card


def save_deck_to_file(deck, filename):
    filepath = os.path.abspath(filename)
    with open(filepath, 'w', newline='') as csvfile:
        write_cards_to_csv(deck.cards, csvfile)


def write_cards_to_csv(cards, csvfile):
    writer = csv.writer(csvfile)
    for card in cards:
        write_in_row(card, writer)


def write_in_row(card, writer):
    writer.writerow([card.get_target_word(),
                     card.get_sentence(),
                     card.get_translation(),
                     card.get_definition()])


def load_deck_from_file(deck, filename):
    filepath = os.path.abspath(filename)
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', newline='') as csvfile:
        cards = read_cards_from_csv(csvfile)
        add_cards_to_deck(deck, cards)


def add_cards_to_deck(deck, cards):
    for card in cards:
        deck.add_card(card)


def read_cards_from_csv(csvfile):
    reader = csv.reader(csvfile)
    cards = []
    for row in reader:
        row_to_card(cards, row)
    return cards


def row_to_card(cards, row):
    target_word, sentence, translation, definition = row
    cards.append(Card(target_word, sentence, translation, definition))
