import random

from Class.Hand import Hand
from Class.Card import Card

class Deck():
    def __init__(self):
        self.allCards = []
        for i in range(1,14):
            for _ in ["hearts","clubs","spades","diamonds"]:
                self.allCards.append(Card(i))
    
    def __repr__(self):
        message=""
        for i in range(len(self.allCards)):
            message=message + str(self.allCards[i]) + "\n"
        return message
        
    def getDeckLength(self):
        return len(self.allCards)
    
    def isEmpty(self):
        if self.allCards == []:
            return True
        else:
            return False
        
    def shuffle(self):
        random.shuffle(self.allCards)
        
    def drawCard(self):
        if self.isEmpty():
            return None
        else:
            card = self.allCards[0]
            del self.allCards[0]
            return card
        
    def addCard(self, card):
        self.allCards.append(card)
        
    def deal(self, verbose=False):
        """Deal 2 cards to the player and 1 to the bank"""
        self.shuffle()
        c1 = self.drawCard()
        c2 = self.drawCard()
        bankCard = self.drawCard()
        
        playerHand = Hand([c1, c2], verbose=verbose)
        bankHand = Hand([bankCard], verbose=verbose)
        return playerHand, bankHand