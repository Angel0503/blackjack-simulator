import random

from Class.Hand import Hand
from Class.Card import Card

class Deck():
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.allCards = []
        self.build_and_shuffle()
    
    def __repr__(self):
        message=""
        for i in range(len(self.allCards)):
            message=message + str(self.allCards[i]) + "\n"
        return message
    
    def build_and_shuffle(self):
        self.allCards = []
        for _ in range(self.num_decks):
            for i in range(1,14):
                for _ in ["hearts","clubs","spades","diamonds"]:
                    self.allCards.append(Card(i))
        self.shuffle()
        
    def needs_reshuffle(self):
        total_initial_cards = self.num_decks * 52
        if len(self.allCards) <= (total_initial_cards * 0.25):
            return True
        return False

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
        c1 = self.drawCard()
        c2 = self.drawCard()
        bankCard = self.drawCard()
        
        playerHand = Hand([c1, c2], verbose=verbose)
        bankHand = Hand([bankCard], verbose=verbose)
        return playerHand, bankHand