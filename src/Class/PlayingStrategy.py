class PlayingStrategy:
    def __init__(self):
        self.name = "Base Playing Strategy"
        
    def get_best_choice(self, hand, bankHand):
        return "stand"


class BasicStrategy(PlayingStrategy):
    def __init__(self):
        super().__init__()
        self.name = "Perfect Basic Strategy"

    def get_best_choice(self, hand, bankHand):
        stand = "stand"
        hit = "hit"
        double = "double"
        split = "split"
        
        if hand.isPair():
            match hand.cards[0].value:
                case 2 | 3: return split if bankHand.value < 8 else hit
                case 4: return split if bankHand.value in [4, 5] else hit
                case 5: return hit if bankHand.value > 9 else double
                case 6: return split if bankHand.value < 7 else hit 
                case 7: return split if bankHand.value < 8 else hit  
                case 9: return stand if bankHand.value in [7, 10, 11] else split
                case 10 | 8 | 11: return split
                case _: return stand
                
        elif hand.hasAce():
            match hand.value - hand.ace.value:
                case 2 | 3: return double if bankHand.value in [5, 6] else hit
                case 4 | 5: return double if bankHand.value in [4, 5, 6] else hit
                case 6: return double if bankHand.value in [3, 4, 5, 6] else hit
                case 7:
                    if bankHand.value > 8: return hit
                    else: return stand if bankHand.value in [2, 7, 8] else double
                case _: return stand
                
        else:
            match hand.value:
                case 5 | 6 | 7 | 8: return hit
                case 9: return double if bankHand.value in [3, 4, 5] else hit
                case 10: return hit if bankHand.value in [10, 11] else double
                case 11: return hit if bankHand.value == 11 else double
                case 12: return stand if bankHand.value in [4, 5, 6] else hit
                case 13 | 14 | 15 | 16: return stand if bankHand.value < 7 else hit
                case _: return stand

class NeverBustStrategy(PlayingStrategy):
    def __init__(self):
        super().__init__()
        self.name = "Never Bust (Stand on 12+)"

    def get_best_choice(self, hand, bankHand):
        # Always split Aces and 8s (basic rule of thumb)
        if hand.isPair() and hand.cards[0].value in [8, 11]:
            return "split"
        # If we have 12 or more, we ALWAYS stand to avoid busting
        if hand.value >= 12:
            return "stand"
        return "hit"