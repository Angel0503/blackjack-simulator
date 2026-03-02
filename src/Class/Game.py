from Class.Deck import Deck

class Game:
    def __init__(self):
        self.deck = Deck()
        self.playerHand, self.bankHand = self.deck.deal()
    
    def __str__(self):
        return f"#---------#\nPlayer Hand: {self.playerHand}\nBank Hand: {self.bankHand}\n#---------#"
    
    def playerChoice(self):
        return self.playerHand.bestChoice(self.bankHand)
    
    def bankDraw(self):
        while(self.bankHand.value < 16):
            drawnCard = self.deck.drawCard()
            self.bankHand.addCard(drawnCard)
            print(f"Bank draws card: {drawnCard}, total: {self.bankHand.value}")


    def nextPlay(self):
        choice = self.playerChoice()
        match choice:
            case "hit":
                self.playerHand.hit(self.deck, self.playerHand)
            case "split":
                self.playerHand = self.playerHand.split(self.deck)
            case "double":
                self.playerHand.double(self.deck)
            case "stand":
                self.playerHand.standAction()
        self.bankDraw()

    def hasPlayerWin(self):
        return self.playerHand.isWin(self.bankHand)