"""A French suited playing card class and a Deck of 52 cards class"""

from collections import namedtuple
from random import shuffle, randrange
from math import ceil

Card = namedtuple('Card', ['rank', 'suit'])


def _str_card(c):
    """Convert a card into a formatted string."""
    return "{} of {}".format(c.rank, c.suit)


Card.__str__ = _str_card


def is_ace(c):
    """Check to see if the card has the rank of Ace."""
    return c.rank == "Ace"


Card.is_ace = is_ace


def is_ten(c):
    """Check to see if a given card has the rank and value of 10."""
    return c.rank in '10 Jack Queen King'.split()


Card.is_ten = is_ten


class Deck:
    """Deck class to hold 52 French Suited playing cards."""

    ranks = ['Ace'] + [str(x) for x in range(2,11)] + 'Jack Queen King'.split()
    suits = 'Hearts Diamonds Spades Clubs'.split()
    values = list(range(1,11)) + [10, 10, 10]
    value_dict = dict(zip(ranks, values))

    def __init__(self):
        """Create one whole new deck of cards. The cards are not in new deck order."""
        self.cards = [Card(rank,  suit) for suit in self.suits for rank in self.ranks]
        self._cursor = 0

    def __len__(self):
        """Return the number of cards in the deck."""
        return len(self.cards)
    
    def __getitem__(self, position):
        """Return the card at the given postion"""
        return self.cards[position]
    
    def __iter__(self):
        """Iterator to start from the face of the deck and iterate to the bottom."""
        self._cursor = 0
        return self
    
    def __next__(self):
        """Return the next card in the deck."""
        if self._cursor < len(self._cards):
            pos = self._cursor
            self._cursor = self._cursor + 1
            return self._cursor[pos]
        else:
            self._cursor = 0
            raise StopIteration
        
    def shuffle(self, n=1):
        """Shuffle the deck n times. Default is 1 time."""
        for _ in range(n):
            shuffle(self.cards)

    def cut(self):
        """Cut the deck at approximately the half way point +/- 10 cards."""
        extra = ceil(len(self.cards) * 0.2)
        half = (len(self.cards) // 2) + randrange(-extra, extra)
        tophalf = self.cards[:half]
        bottomhalf = self.cards[half:]
        self.cards = bottomhalf + tophalf

    def deal(self, n=1):
        """Deal n cards. Default is 1 card."""
        return [self.cards.pop() for x in range(n)]
    
    def merge(self, deck):
        """Merge the current deck with the deck passed as a parameter."""
        self._cards = self._cards + deck._cards

    def __str__(self):
        """Convert the deck into a string."""
        return ", ".join(map(str, self.cards))
    

def card_value(c):
    """Return the numberical value of the rank of a given card."""
    return Deck.value_dict[c.rank]


Card.value = card_value
Card.__int__ = card_value


    



