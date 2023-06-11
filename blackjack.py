#!/usr/bin/env python3
#Brandon Nguyen
#nguyen.brandon771@csu.fullerton.edu
#@brandonnguyenr

""" This is a simple Blackjack Game that is played against a dealer."""

from blackjackgame import player
from blackjackgame import cards

def main():
    """ This function calls the beginning of the game and loops until the game ends. """
    deck1 = cards.Deck()
    total_betting_amount = 10000

    print('\nWelcome to Blackjack! \
           \nThis game is created by Brandon Nguyen \
           \nPlease contact me at nguyen.brandon771@csu.fullerton.edu for more information!')
    print('\nReady to Win Big? Place your bets now! \
           \nThis game is a 3:2 Payout! \
           \nHave Fun!')
    
    name = input('\nEnter your name: ')
    betting_amount = input('Out of $10,000, how much would you like to bet?: $')

    deck1.shuffle()
    deck1.shuffle()
    deck1.shuffle()

    player1 = player.Player(name)
    dealer  = player.Player('Dealer') 

    card = deck1.deal()
    player1.add_card(card)

    card2 = deck1.deal()
    dealer.add_card(card2) 
    
    print(player1)
    print(dealer)

if __name__ == '__main__':
    main()