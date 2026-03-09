from Class.Card import Card

class Hand:
    def __init__(self, cardList, bet=10, is_split=False, verbose=False):
        self.cards = cardList
        self.value = self.getSumOfCardValues()
        self.bet = bet
        self.totalBet = bet
        self.stand = False
        self.ace = Card(1)
        self.is_split = is_split 
        self.verbose = verbose
        
    def __str__(self):
        cards_str = " | ".join(str(card.value) for card in self.cards)
        return f"{cards_str}  (Total: {self.value})"

    def addBet(self):
        self.totalBet += self.bet

    def getNumberOfCardInHand(self):
        return len(self.cards)

    def getSumOfCardValues(self):
        total = 0
        aces = 0
        for card in self.cards:
            total += card.value
            if card.value == 11:
                aces += 1
        
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
            
        return total

    def isPair(self):
        return self.cards[0] == self.cards[1] and self.getNumberOfCardInHand() == 2
    
    def hasAce(self):
        return any(card.value == 11 for card in self.cards)
    
    def addCard(self, card):
        self.cards.append(card)
        self.value = self.getSumOfCardValues()
        
    def hit(self, deck, hand):
        newCard = deck.drawCard()
        hand.addCard(newCard)
        if self.verbose:
            print(f"Player hit : {newCard}")

    def standAction(self):
        self.stand = True

    def double(self, deck):
        self.addBet()
        self.hit(deck, self)

    def split(self, deck):
        card = self.cards[0]
        del self.cards[0]
        
        self.is_split = True
        splittedHand = Hand([card], bet=self.bet, is_split=True)

        self.hit(deck, self)
        self.hit(deck, splittedHand)

        return splittedHand
    
    def isWin(self, bankHand):
        if self.value > 21:
            return "Lose"
        elif self.value == 21 and len(self.cards) == 2 and not self.is_split:
            return "Blackjack"
        elif bankHand.value > 21:
            return "Win"
        elif self.value == bankHand.value:
            return "Push"
        else:
            return "Win" if self.value > bankHand.value else "Lose"