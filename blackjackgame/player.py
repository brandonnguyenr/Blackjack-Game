"""A Player will be invented and attain everyting that belongs to that player"""

from blackjackgame.cards import Deck

class Player:
    """Player class for the Blackjack game."""

    def __init__(self, name):
        """Create a player with an empty hand."""
        self.name = name
        self.hand = []

    def add_cards(self, card):
        """Adding a card to the players hand."""
        self.hand.extend(card)

    def calculate_hand(self):
        """This will calculate the hand of the current player"""
        value = sum(Deck.value_dict[card.rank] for card in self.hand)
        if 'Ace' in [card.rank for card in self.hand] and value + 10 <= 21:
            value += 10
        return value
    
    def print_all(self):
        """Print all the cards"""
        return f"{self.name}: {', '.join(str(card) for card in self.hand)}"
    
    def __str__(self):
        """Convert the player into a string."""
        if self.name == 'Dealer':
            return f"{self.name}: {str(self.hand[0])}, ?"
        else:
            return f"{self.name}: {', '.join(str(card) for card in self.hand)}"