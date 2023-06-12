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

    def see_hand(self):
            """"Print"""
            for card in self.hand:
                print(f"Rank: {card.rank}, Value: {Deck.value_dict[card.rank]}")

    def __str__(self):
        """Convert the player into a string."""
        return f"{self.name}: \n{', '.join(str(card) for card in self.hand)}\n"