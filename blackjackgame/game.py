"""Rules to the Game of Blackjack"""

from blackjackgame.cards import Deck

class Game:
    """This class will contain all the rules to Blackjack, determine winners, and process dialogue """

    def __init__(self, players):
        """Create a game with players and a deck of cards"""
        self.deck = self.create_master_deck()
        self.deck.shuffle()
        self.deck.cut()
        self.players = players

    def create_master_deck(self):
        """Creating 8 decks and combining them all together"""
        master_deck = Deck()

        for _ in range(7):
            new_deck = Deck()
            master_deck.merge(new_deck)

        return master_deck

    def deal_two_cards(self, player):
        """Deal one card to each player one-by-one."""
        for _ in range(2):
            for player in self.players:
                player.add_cards(self.deck.deal())
        
    def dealers_cards(self, player):
        """Dealers cards"""
        if player.name == 'Dealer':
            while player.calculate_hand() <= 17:
                player.add_cards(self.deck.deal())

    def play_round(self, player):
        """Play a round of the Game"""
        if player.name != 'Dealer':
            print(player)
            print('Current Hand Value:', player.calculate_hand())
            while player.calculate_hand() < 21:
                choice = input('\nDo you want to hit? (y/n): ').lower()
                print('\n')
                if choice == 'y':
                    player.add_cards(self.deck.deal())
                    if player.calculate_hand() > 21:
                        print(player)
                        print('Current Hand Value:', player.calculate_hand())
                        break
                elif choice =='n':  
                        print(player)
                        print('Current Hand Value:', player.calculate_hand())
                        break
          
        if player.name == 'Dealer':
            print(player)
            self.dealers_cards(player)

        return player.calculate_hand()

    def play_game(self, player):
        """Run the full game."""
        self.deal_two_cards(player)
        self.play_round(player)

