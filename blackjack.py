#!/usr/bin/env python3
#Brandon Nguyen
#nguyen.brandon771@csu.fullerton.edu
#@brandonnguyenr

""" This is a simple Blackjack Game that is played against a dealer."""

from blackjackgame.game import Game
from blackjackgame import player
from blackjackgame import cards

def main():
    """ This function calls the beginning of the game and loops until the game ends. """
    dealer  = player.Player('Dealer') 

    print('\nWelcome to Blackjack! \
           \nThis game is created by Brandon Nguyen \
           \nPlease contact me at nguyen.brandon771@csu.fullerton.edu for more information!')
    print('\nReady to Win Big? Place your bets now! \
           \nThis game is a 2:1 Payout! \
           \nHave Fun!')
    
    name = input('\nEnter your name: ')
    player1 = player.Player(name)
    
    game = Game([player1, dealer])
    game.play_game(dealer)
    game.play_game(player1)

if __name__ == '__main__':
    main()