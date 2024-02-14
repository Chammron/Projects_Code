#Cameron Norris

#This program will simulate a game of blackjack.

import random
import os

class Card:
    #This class will create a card object.
    def__init__(self, cardFace, value, symbol):
        #These methods will initialize the card objects.
        self.cardFace = cardFace
        self.value = value
        self.symbol = symbol

def showCards(cards, hidden):

    s = ''
    for card in cards:
        s = s + '\t ___________'
    if hidden:
        s += s + '\t ___________'
    print(s)

    s = ''
    for card in cards:
