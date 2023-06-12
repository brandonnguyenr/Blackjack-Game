#!/usr/bin/env python3
#Brandon Nguyen
#nguyen.brandon771@csu.fullerton.edu
#@brandonnguyenr

""" This is a simple Blackjack Game that is played against a dealer."""

from blackjackgame.game import Game
from blackjackgame import player

def main():
    """ This function calls the beginning of the game and loops until the game ends. """

    print('\nWelcome to Blackjack! \
           \nThis game is created by Brandon Nguyen \
           \nPlease contact me at nguyen.brandon771@csu.fullerton.edu for more information!')
    print('\nReady to Win Big? Place your bets now! \
           \nThis game is a 2:1 Payout! \
           \nHave Fun!')
    max_bet = 10000
    winnings = 0
    play_again = 'y'
    dealer = player.Player('Dealer')
    
    name = input('\nEnter your name: ')
    player1 = player.Player(name)

    while True:
        betted_amount = input('Hello ' + name + ', how much would you like to bet out of your $10,000?: $')

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

        game = Game([dealer, player1])
        
        double_down = input('Would you like to double down? (y/n): ')
        game.play_game(dealer)
        player1_hand_value = game.play_round(player1)
        dealer_hand_value = game.play_round(dealer)
        
        if double_down == 'y':
            betted_amount = betted_amount + betted_amount

        if player1_hand_value > 21:
            print("Player BUST! Dealer wins.")
            max_bet = max_bet - betted_amount
        elif dealer_hand_value > 21:
            print("Dealer BUST! Player wins.")
            winnings = betted_amount / 2
            betted_amount += winnings
            max_bet += betted_amount
        elif player1_hand_value == dealer_hand_value:
            print("It's a tie! No Losses, it's a push.")
        elif player1_hand_value > dealer_hand_value:
            print("Player wins!")
            winnings = betted_amount / 2
            betted_amount += winnings
            max_bet += betted_amount
        else:
            print("Dealer wins!")
            max_bet = max_bet - betted_amount

        play_again = input('You have $' + str(max_bet) + " left to bet! Want to play again? (y/n): ")

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

    print('\n\nHope you had fun! See you next time!')

if __name__ == '__main__':
    main()