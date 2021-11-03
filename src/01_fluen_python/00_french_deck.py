# Example 1-1. A deck as a sequence of cards.

from models.french_deck import Card, FrenchDeck

deck = FrenchDeck()

# deck length can be queried by len()
print(f"Cards in deck: {len(deck)}")

# deck items can be queried by index
print("--- first & last cards ---")
print(deck[0]) # first
print(deck[-1]) # last

# get random card
print("--- set of random cards ---")
from random import choice
print(choice(deck)) # random
print(choice(deck)) # random
print(choice(deck)) # random

# becuase of __getitem__, the deck can be sliced
print("--- top three cards ---")
print(deck[:3])
print("--- aces ---")
print(deck[12::13])

# because of __getitem__, the deck is iterable
print("--- deck iteration ---")
index = 0
for card in deck:
    print(f"{index} - {card}")
    index += 1

# verify for existing items
print("--- item existance check ---")
print(f"deck has queen of hearts?: {Card('Q', 'hearts') in deck}")
print(f"deck has king of beasts?: {Card('K', 'beasts') in deck}")

# how about some sorting by rank
print("--- items custom sorting ---")

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card: Card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)

# how about reversing the above process
print("--- items custom sorting, reversed ---")

reversed_sorted_deck = []
for card in sorted(deck, key=spades_high):
    reversed_sorted_deck.append(card)

reversed_sorted_deck.reverse()
print(reversed_sorted_deck)