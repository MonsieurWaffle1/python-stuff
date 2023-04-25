#Imports modules
import time
import random
import card_rand

#Sets starting variables
startup = 1
playing = 1
aceChoise = True

card_rand.test()

def playGame():
    playedCards = []
    startup = 1
    currentScore = 0
    isOut = 0

    #Draws the starting cards
    currentScore, displayCard, playedCards = card_rand.drawCard(currentScore, playedCards, False) 
    currentScore, displayCard, playedCards = card_rand.drawCard(currentScore, playedCards, False) 

    while isOut == 0:
        #Tells the user what their score is
        if startup == 1:
            print ('Your starting score is:')
            print(currentScore)
            time.sleep(0.5)
            print (' ')
            print ('Your starting cards are:')
            print (playedCards)

            #Checks for a blackjack
            if currentScore == 21:
                isOut = 1
                print ('BLACKJACK!!!!')
                print ('Congratulations!')
                isOut == 0
            startup += 1
        else:
            print ('The drawn card is:')
            print (displayCard)
            print (' ')
            print ('Your current score is: ')
            print (currentScore)

        time.sleep(0.5)

        #Asks the user to stick or twist
        stickOrTwist = input('Would you like to stick or twist? ')
        time.sleep(0.5)
        if stickOrTwist == 'twist':
            currentScore, displayCard, playedCards = card_rand.drawCard(currentScore, playedCards, aceChoise)
        elif stickOrTwist == 'stick':
            break

        #Checks for blackjack
        if currentScore > 21:
            isOut = 1
            print ("I'm afraid you've gone over 21!")
        elif currentScore == 21:
            isOut = 1
            print ('BLACKJACK!!!!')
            print ('Congratulations!')
    str(currentScore)
    print ('Your final score was:')
    print (currentScore)

while playing == 1:
    #Repeats the game until the user dosen't want to play
    playGame()
    time.sleep(0.5)
    playAgain = input('Would you like to play again? y/n ')
    if playAgain == 'n':
        playing = playing + 1
time.sleep(0.5)

print ('Thanks for playing!')
time.sleep(3)
        
