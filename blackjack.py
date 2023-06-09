#!/usr/bin/env python3
#Brandon Nguyen
#nguyen.brandon771@csu.fullerton.edu
#@brandonnguyenr

""" This is a simple Blackjack Game that is played against a dealer."""

from blackjackgame.game import start_game

def main():
    """ This function calls the blackjack game directory and loops until the game ends."""
    start_game()

if __name__ == '__main__':
    main()