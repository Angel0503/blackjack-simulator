from Class.Card import Card

class Hand:
    def __init__(self, cardList, bet=10, is_split=False):
        self.cards = cardList
        self.value = self.getSumOfCardValues()
        self.bet = bet
        self.totalBet = bet
        self.stand = False
        self.ace = Card(1)
        self.is_split = is_split 
        
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
        
    def bestChoice(self, bankHand):
        stand = "stand"
        hit = "hit"
        double = "double"
        split = "split"
        
        if self.isPair():
            match self.cards[0].value:
                case 2 | 3:
                    return split if bankHand.value < 8 else hit
                case 4:
                    return split if bankHand.value in [4, 5] else hit
                case 5:
                    return hit if bankHand.value > 9 else double
                case 6:
                    return split if bankHand.value < 7 else hit 
                case 7:
                    return split if bankHand.value < 8 else hit  
                case 9: 
                    return stand if bankHand.value in [7, 10, 11] else split
                case 10 | 8 | 11:
                    return split
                case _:
                    return stand
        elif self.hasAce():
            match self.value - self.ace.value:
                case 2 | 3:
                    return double if bankHand.value in [5, 6] else hit
                case 4 | 5:
                    return double if bankHand.value in [4, 5, 6] else hit
                case 6:
                    return double if bankHand.value in [3, 4, 5, 6] else hit
                case 7:
                    if bankHand.value > 8:
                        return hit
                    else:
                        return stand if bankHand.value in [2, 7, 8] else double
                case _:
                    return stand
        else:
            match self.value:
                case 5 | 6 | 7 | 8:
                    return hit
                case 9:
                    return double if bankHand.value in [3, 4, 5] else hit
                case 10:
                    return hit if bankHand.value in [10, 11] else double
                case 11:
                    return hit if bankHand.value == 11 else double
                case 12:
                    return stand if bankHand.value in [4, 5, 6] else hit
                case 13 | 14 | 15 | 16:
                    return stand if bankHand.value < 7 else hit
                case _:
                    return stand
                
    def hit(self, deck, hand):
        newCard = deck.drawCard()
        hand.addCard(newCard)
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