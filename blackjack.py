"A simple blackjack game."
#Imports modules
import time
import random_plus

#Sets starting variables
IN_PLAY = 1

random_plus.test()

def play_game():
    "Runs the game."
    played_cards = []
    startup = 1
    current_score = 0
    ace_choise = True

    #Draws the starting cards
    current_score, display_card, played_cards = random_plus.draw_card(current_score, played_cards, False)
    current_score, display_card, played_cards = random_plus.draw_card(current_score, played_cards, False)

    while True:
        #Tells the user what their score is
        if startup == 1:
            print ('Your starting score is:')
            print(current_score)
            time.sleep(0.5)
            print (' ')
            print ('Your starting cards are:')
            print (played_cards)

            #Checks for a blackjack
            if current_score == 21:
                print ('BLACKJACK!!!!')
                print ('Congratulations!')
                break
            startup += 1
        else:
            print ('The drawn card is:')
            print (display_card)
            print (' ')
            print ('Your current score is: ')
            print (current_score)

        time.sleep(0.5)

        #Asks the user to stick or twist
        stick_or_twist = input('Would you like to stick or twist? ')
        time.sleep(0.5)
        if stick_or_twist == 'twist':
            current_score, display_card, played_cards = random_plus.draw_card(current_score, played_cards, ace_choise)
        elif stick_or_twist == 'stick':
            break

        #Checks for blackjack
        if current_score > 21:
            print ("I'm afraid you've gone over 21!")
        elif current_score == 21:
            print ('BLACKJACK!!!!')
            print ('Congratulations!')
    str(current_score)
    print ('Your final score was:')
    print (current_score)

while True:
    #Repeats the game until the user dosen't want to play
    play_game()
    time.sleep(0.5)
    playAgain = input('Would you like to play again? y/n ')
    if playAgain == 'n':
        break
time.sleep(0.5)

print ('Thanks for playing!')
time.sleep(3)
