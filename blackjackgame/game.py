"""Rules to the Game of Blackjack"""

from blackjackgame.cards import Deck

class Game:
    """This class will contain all the rules to Blackjack, determine winners,
    and process dialogue """

    def __init__(self, players):
        """Create a game with players and a deck of cards."""
        self.deck = self.create_master_deck()
        self.deck.shuffle()
        self.deck.cut()
        self.players = players

    def create_master_deck(self):
        """Creating 8 decks and combining them all together."""
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
        """Dealers cards."""
        if player.name == 'Dealer':
            while player.calculate_hand() <= 17:
                player.add_cards(self.deck.deal())

    def doubling_down(self, betted_amount):
        """Ask the player if they want to double down."""
        double_down = input('Would you like to double down? (y/n): ')
        if double_down == 'y':
            betted_amount = betted_amount * 2
        return betted_amount
    def play_round(self, player):
        """Play a round of the Game"""
        if player.name != 'Dealer':
            print(player)
            print('Current Hand Value:', player.calculate_hand())
            while player.calculate_hand() < 21:
                choice = input('Do you want to hit? (y/n): ').lower()
                if choice == 'y':
                    player.add_cards(self.deck.deal())
                    printout = player.print_all()
                    print('Current Hand Value:', player.calculate_hand())
                    print(printout)
                    if player.calculate_hand() > 21:
                        break
                elif choice == 'n':
                    break
        if player.name == 'Dealer':
            self.dealers_cards(player)
            result = player.print_all()
            print(result)
            print('Current Hand Value:', player.calculate_hand())

        return player.calculate_hand()
    def show_player_cards_at_the_start(self, player):
        """Shows the dealers and the players cards at the start of the game."""
        for player in self.players:
            print(player)

    def play_game(self, player, betted_amount):
        """Run the full game."""
        self.deal_two_cards(player)
        self.show_player_cards_at_the_start(player)
        doubling_down = self.doubling_down(betted_amount)
        return doubling_down
