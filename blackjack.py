#!/usr/bin/env python3
#Brandon Nguyen
#nguyen.brandon771@csu.fullerton.edu
#@brandonnguyenr

""" This is a simple Blackjack Game that is played against a dealer."""

from blackjackgame.game import Game
from blackjackgame import player

def main():
    """ This function calls the beginning of the game and loops until the game ends. """
    max_bet = 10000
    play_again = 'y'
    dealer = player.Player('Dealer')
    name = input('\nEnter your name: ')
    player1 = player.Player(name)
    while True:
        betted_amount = input('Hello ' + name + ', how much would you like to bet \
out of your $10,000?: $')
        if not betted_amount.isdigit():
            print("Invalid input. Please enter a valid integer.")
            continue
        betted_amount = int(betted_amount)
        if betted_amount > 10000:
            print("Bet amount cannot exceed $10,000.")
        else:
            break
    while play_again == 'y':
        player1.hand = []
        dealer.hand = []
        game = Game([player1, dealer])
        betted_amount = game.play_game(player1, betted_amount)
        player1_hand_value = game.play_round(player1)
        dealer_hand_value = game.play_round(dealer)
        if player1_hand_value > 21:
            print("Player BUST! Dealer wins.")
            max_bet = max_bet - betted_amount
        elif dealer_hand_value > 21:
            print("Dealer BUST! Player wins.")
            max_bet += betted_amount
        elif player1_hand_value == dealer_hand_value:
            print("It's a tie! No Losses, it's a push!")
        elif player1_hand_value > dealer_hand_value:
            print("Player wins!")
            max_bet += betted_amount
        else:
            print("Dealer wins!")
            max_bet = max_bet - betted_amount
        play_again = input('You have $' + str(max_bet) + " left to bet! Want to play again?(y/n): ")
        if play_again == 'y':
            while True:
                betted_amount = input('How much would you like to bet this time?: $')
                if not betted_amount.isdigit():
                    print("Invalid input. Please enter a valid integer.")
                    continue
                betted_amount = float(betted_amount)
                if betted_amount > max_bet:
                    print("Bet amount cannot exceed your amount.")
                else:
                    break
    print('\nHope you had fun! See you next time!')

if __name__ == '__main__':
    main()
