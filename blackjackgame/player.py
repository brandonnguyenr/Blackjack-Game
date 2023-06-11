"""A Player will be invented and attain everyting that belongs to that player"""

class Player:
    """Player class for the Blackjack game."""

    def __init__(self, name):
        """Create a player with an empty hand."""
        self.name = name
        self.hand = []

    def add_card(self, card):
        """Adding a card to the players hand."""
        self.hand.append(card)

    def __str__(self):
        """Convert the player into a string."""
        return f"{self.name}: {', '.join(str(card) for card in self.hand)}"