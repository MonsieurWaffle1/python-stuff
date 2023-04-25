#Created by MonsieurWaffle
"card_rand v1.0.1"

#Imports modules
import random

def test():
    "Tests the module is correctly functioning"
    print ('The module is correctly functioning.')

def card_checker(drawn_card, played_cards):
    "Returns a variable based on weather or not the card has been drawn"
    if drawn_card in played_cards:
        is_viable = False
    else:
        played_cards.append(drawn_card)
        is_viable = True
    return played_cards, is_viable

def draw_card(current_score, played_cards, ace_choise):
    "Draws a playing card, provides a str representing the drawn card, as well as a current score. Will never draw the same card twice."
    draw = True
    while draw is True:
        #Draws the card and determines the suit
        drawn_card_number = random.randint(1, 13)
        card_suit = random.randint(1,4)

        if card_suit == 1:
            card_suit = 'of Spades'
        elif card_suit == 2:
            card_suit = 'of Clubs'
        elif card_suit == 3:
            card_suit = 'of Hearts'
        elif card_suit == 4:
            card_suit = 'of Diamonds'

        #Concentrates the drawn card from an int to a str
        if drawn_card_number == 1:
            display_card_number = 'Ace '
        elif drawn_card_number == 2:
            display_card_number = '2 '
        elif drawn_card_number == 3:
            display_card_number = '3 '
        elif drawn_card_number == 4:
            display_card_number = '4 '
        elif drawn_card_number == 5:
            display_card_number = '5 '
        elif drawn_card_number == 6:
            display_card_number = '6 '
        elif drawn_card_number == 7:
            display_card_number = '7 '
        elif drawn_card_number == 8:
            display_card_number = '8 '
        elif drawn_card_number == 9:
            display_card_number = '9 '
        elif drawn_card_number == 10:
            display_card_number = '10 '
        elif drawn_card_number == 11:
            display_card_number = 'Jack '
        elif drawn_card_number == 12:
            display_card_number = 'Queen '
        elif drawn_card_number == 13:
            display_card_number = 'King '

        display_card = display_card_number + card_suit

        #Assigns the correct values to the Jack, Queen and King cards
        if drawn_card_number == 11:
            drawn_card_number = 10
        elif drawn_card_number == 12:
            drawn_card_number = 10
        elif drawn_card_number == 13:
            drawn_card_number = 10

        #Asks the user to choose a value for the ace
        if drawn_card_number == 1:
            if ace_choise is True:
                ace_desition = input('Would you like your ace to be 1 or 11? ')
                int(ace_desition)
            else:
                ace_desition = '11'

            if ace_desition == '1':
                current_score = current_score + 1
            elif ace_desition == '11':
                current_score = current_score + 11
            else:
                current_score = current_score + 200
        else:
            current_score = current_score + drawn_card_number

        #Redraws the card if the card has already been drawn
        drawn_card = display_card
        played_cards, is_viable = card_checker(drawn_card, played_cards)
        if is_viable is True:
            draw = False

    return current_score, display_card, played_cards