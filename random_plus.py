#card_rand v1.0
#Created by MonsieurWaffle

#Imports modules
import time
import random

def test():
    print ('The module is correctly functioning.')

def cardChecker(drawnCard, playedCards):
    #Returns a variable based on weather or not the card has been drawn
    if drawnCard in playedCards:
        isViable = False
    else:
        playedCards.append(drawnCard)
        isViable = True
    return playedCards, isViable

def drawCard(currentScore, playedCards, aceChoise):
    draw = True
    while draw == True:
        #Draws the card and determines the suit
        drawnCardNumber = random.randint(1, 13)
        cardSuit = random.randint(1,4)

        if cardSuit == 1:
            cardSuit = 'of Spades'
        elif cardSuit == 2:
            cardSuit = 'of Clubs'
        elif cardSuit == 3:
            cardSuit = 'of Hearts'
        elif cardSuit == 4:
            cardSuit = 'of Diamonds'

        #Concentrates the drawn card from an int to a str
        if drawnCardNumber == 1:
            displayCardNumber = 'Ace '
        elif drawnCardNumber == 2:
            displayCardNumber = '2 '
        elif drawnCardNumber == 3:
            displayCardNumber = '3 '
        elif drawnCardNumber == 4:
            displayCardNumber = '4 '
        elif drawnCardNumber == 5:
            displayCardNumber = '5 '
        elif drawnCardNumber == 6:
            displayCardNumber = '6 '
        elif drawnCardNumber == 7:
            displayCardNumber = '7 '
        elif drawnCardNumber == 8:
            displayCardNumber = '8 '
        elif drawnCardNumber == 9:
            displayCardNumber = '9 '
        elif drawnCardNumber == 10:
            displayCardNumber = '10 '
        elif drawnCardNumber == 11:
            displayCardNumber = 'Jack '
        elif drawnCardNumber == 12:
            displayCardNumber = 'Queen '
        elif drawnCardNumber == 13:
            displayCardNumber = 'King '

        displayCard = (displayCardNumber + cardSuit)

        #Assigns the correct values to the Jack, Queen and King cards   
        if drawnCardNumber == 11:
            drawnCardNumber = 10
        elif drawnCardNumber == 12:
            drawnCardNumber = 10
        elif drawnCardNumber == 13:
            drawnCardNumber = 10

        #Asks the user to choose a value for the ace
        if drawnCardNumber == 1:
            if aceChoise == True:
                aceDesition = input('Would you like your ace to be 1 or 11? ')
                int(aceDesition)
            else:
                aceDesition = '11'

            if aceDesition == '1':
                currentScore = currentScore + 1
            elif aceDesition == '11':
                 currentScore = currentScore + 11
            else:
                currentScore = currentScore + 200
        else:
            currentScore = currentScore + drawnCardNumber

        #Redraws the card if the card has already been drawn
        drawnCard = displayCard
        playedCard, isViable = cardChecker(drawnCard, playedCards)
        if isViable == True:
            draw = False
            
    return currentScore, displayCard, playedCards
