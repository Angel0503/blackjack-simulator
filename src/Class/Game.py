from Class.Deck import Deck

class Game:
    def __init__(self):
        self.deck = Deck()
        self.playerHand, self.bankHand = self.deck.deal()
        self.splittedHand = None
    
    def __str__(self):
        return f"Player Hand:{self.playerHand}\nBank Hand:{self.bankHand}"
    
    def playerChoice(self):
        return self.playerHand.bestChoice(self.bankHand)
    
    def bankDraw(self):
        while(self.bankHand.value < 17):
            drawnCard = self.deck.drawCard()
            self.bankHand.addCard(drawnCard)
            print(f"Bank draws card: {drawnCard}, total: {self.bankHand.value}")


    def handlePlayerAction(self):
        print("#----PLAYER'S TURN----#")
        
        while not self.playerHand.stand and self.playerHand.value <= 21:
            choice = self.playerChoice()
            print(f"Player choice: {choice}")
            
            match choice:
                case "hit":
                    self.playerHand.hit(self.deck, self.playerHand)
                case "split":
                    self.splittedHand = self.playerHand.split(self.deck)
                    print(f"Base hand:{self.playerHand}")
                    print(f"Splitting hand:{self.splittedHand}")
                case "double":
                    if self.playerHand.getNumberOfCardInHand() == 2:
                        self.playerHand.double(self.deck)
                        self.playerHand.standAction()
                    else:
                        self.playerHand.hit(self.deck, self.playerHand)
                case "stand":
                    self.playerHand.standAction()
                    
        if self.playerHand.value > 21:
            print(f"Player busts with {self.playerHand.value}! Bank doesn't need to draw.")
        else:
            print("#----BANK'S TURN----#")
            self.bankDraw()

    def hasPlayerWin(self):
        return self.playerHand.isWin(self.bankHand)