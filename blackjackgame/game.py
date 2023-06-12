"""Rules to the Game of Blackjack"""

from blackjackgame.cards import Deck

class Game:
    """This class will contain all the rules to Blackjack, determine winners, and process dialogue """

    def __init__(self, players):
        """Create a game with players and a deck of cards"""
        self.deck = Deck()
        self.deck.shuffle()
        self.players = players

    def deal_two_cards(self):
         """Deal two cards to each player one-by-one."""
         for _ in range(1):
              for player in self.players:
                   player.add_cards(self.deck.deal())

    def play_round(self, player):
        """Play a round of the Game"""
        print(player)
        if player.name != 'Dealer':
             while True:
                choice = input('Do you want to hit? (y/n): ').lower()
                if choice == 'y':
                    player.add_cards(self.deck.deal())
                    print(player)
                    break
                elif choice =='n':
                    break

    def play_game(self, player):
         """Run the full game."""
         self.deal_two_cards()
         self.play_round(player)
         player.see_hand()

