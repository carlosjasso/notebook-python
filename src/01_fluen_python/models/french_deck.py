import collections

# construct a simple class to represent individual cards
Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    # initializer/constructor
    def __init__(self):
        self._cards = [Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks]
    
    # to get along with the len() python function
    def __len__(self):
        return len(self._cards)
    
    # for objects in the collection to be queried by index
    def __getitem__(self, index):
        return self._cards[index]