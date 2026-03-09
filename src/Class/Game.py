from Class.Deck import Deck

class Game:
    def __init__(self, balance=1000, allow_negative=False, base_bet=10, verbose=False, num_decks=1):
        self.balance = balance
        self.allow_negative = allow_negative
        self.verbose = verbose
        self.base_bet = 10
        self.balance -= self.base_bet

        self.deck = Deck(num_decks=num_decks)
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
            print(f"Current Balance: ${self.balance + self.base_bet} (Betting ${self.base_bet})")
        
        i = 0
        while i < len(self.playerHands):
            current_hand = self.playerHands[i]
            
            if len(self.playerHands) > 1 and self.verbose:
                print(f"\n--- Playing Hand {i+1} ---")
            
            while not current_hand.stand and current_hand.value <= 21:
                choice = current_hand.bestChoice(self.bankHand)
                
                if choice in ["split", "double"]:
                    if not self.allow_negative and self.balance < self.base_bet:
                        if self.verbose:
                            print(f"Player wants to {choice}, but has insufficient funds. Defaulting to hit.")
                        choice = "hit"
                
                if self.verbose:
                    print(f"Player choice: {choice}")
                
                match choice:
                    case "hit":
                        current_hand.hit(self.deck, current_hand)
                    case "split":
                        self.balance -= self.base_bet 
                        new_hand = current_hand.split(self.deck)
                        self.playerHands.append(new_hand) 
                        if self.verbose:
                            print(f"Base hand: {current_hand}")
                            print(f"New split hand added: {new_hand}")
                    case "double":
                        if current_hand.getNumberOfCardInHand() == 2:
                            self.balance -= self.base_bet 
                            current_hand.double(self.deck)
                            current_hand.standAction()
                        else:
                            current_hand.hit(self.deck, current_hand)
                    case "stand":
                        current_hand.standAction()
                        
            if current_hand.value > 21 and self.verbose:
                print(f"Hand busts with {current_hand.value}!")
            
            i += 1 
                
        all_busted = all(hand.value > 21 for hand in self.playerHands)
        
        if all_busted:
            if self.verbose:
                print("\nAll player hands busted! Bank doesn't need to draw.")
        else:
            if self.verbose:
                print("\n#----BANK'S TURN----#")
            self.bankDraw()

    def getPlayerResults(self):
        results = []
        for hand in self.playerHands:
            results.append(hand.isWin(self.bankHand))
        return results

    def calculateFinalBalance(self):
        """Calculates the return of bets based on game outcomes."""
        for hand in self.playerHands:
            outcome = hand.isWin(self.bankHand)
            
            if outcome == "Win":
                self.balance += (hand.totalBet * 2) 
            elif outcome == "Blackjack":
                self.balance += hand.totalBet + (hand.totalBet * 1.5)
            elif outcome == "Push":
                self.balance += hand.totalBet
            
        return self.balance