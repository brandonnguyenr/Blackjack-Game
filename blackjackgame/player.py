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
        """"Print the hand of the current player"""
        for card in self.hand:
            print(f"Rank: {card.rank}, Value: {Deck.value_dict[card.rank]}")

    def calculate_hand(self):
        """This will calculate the hand of the current player"""
        value = sum(Deck.value_dict[card.rank] for card in self.hand)
        if 'Ace' in [card.rank for card in self.hand] and value + 10 <= 21:
            value += 10
        return value
    
    def hide_second_card(self):
        if len(self.hand) >= 2:
            self.hand[1].hide()

    def reveal_cards(self):
        if len(self.hand) >= 2:
            self.hand[1].reveal()

    def __str__(self):
        """Convert the player into a string."""
        return f"{self.name}: {', '.join(str(card) for card in self.hand)}"