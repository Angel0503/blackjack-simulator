from Class.Deck import Deck

class Game:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.deck = Deck()
        initialHand, self.bankHand = self.deck.deal(verbose=verbose)
        self.playerHands = [initialHand] 
    
    def __str__(self):
        hands_str = "\n".join([f"  Hand {i+1}: {hand}" for i, hand in enumerate(self.playerHands)])
        return f"Player Hands:\n{hands_str}\nBank Hand: {self.bankHand}"
    
    def bankDraw(self):
        while(self.bankHand.value < 17):
            drawnCard = self.deck.drawCard()
            self.bankHand.addCard(drawnCard)
            if self.verbose:
                print(f"Bank draws card:{drawnCard}, total: {self.bankHand.value}")

    def handlePlayerAction(self):
        if self.verbose:
            print("#----PLAYER'S TURN----#")
        
        i = 0
        while i < len(self.playerHands):
            current_hand = self.playerHands[i]
            
            if len(self.playerHands) > 1:
                if self.verbose:
                    print(f"\n--- Playing Hand {i+1} ---")
            
            while not current_hand.stand and current_hand.value <= 21:
                choice = current_hand.bestChoice(self.bankHand)
                if self.verbose:
                    print(f"Player choice: {choice}")
                
                match choice:
                    case "hit":
                        current_hand.hit(self.deck, current_hand)
                    case "split":
                        new_hand = current_hand.split(self.deck)
                        self.playerHands.append(new_hand) 
                        if self.verbose:
                            print(f"Base hand: {current_hand}")
                            print(f"New split hand added: {new_hand}")
                    case "double":
                        if current_hand.getNumberOfCardInHand() == 2:
                            current_hand.double(self.deck)
                            current_hand.standAction()
                        else:
                            current_hand.hit(self.deck, current_hand)
                    case "stand":
                        current_hand.standAction()
                        
            if current_hand.value > 21:
                if self.verbose:
                    print(f"Hand busts with {current_hand.value}")
            
            i += 1
                
        all_busted = all(hand.value > 21 for hand in self.playerHands)
        
        if all_busted:
            if self.verbose:
                print("\nAll player hands busted")
        else:
            if self.verbose:
                print("\n#----BANK'S TURN----#")
            self.bankDraw()

    def hasPlayerWin(self):
        results = []
        for i, hand in enumerate(self.playerHands):
            result = hand.isWin(self.bankHand)
            results.append(f"Hand {i+1}: {result}")
        return " | ".join(results)

    def getPlayerResults(self):
        results = []
        for hand in self.playerHands:
            results.append(hand.isWin(self.bankHand))
        return results