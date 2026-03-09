class BettingStrategy:
    def __init__(self):
        self.running_count = 0
        self.name = "Base Strategy"

    def reset_count(self):
        self.running_count = 0

    def update_count(self, card):
        pass

    def get_bet_size(self, base_bet, remaining_decks):
        return base_bet


class FlatBetting(BettingStrategy):
    def __init__(self):
        super().__init__()
        self.name = "Flat Betting (No Counting)"


class HiLo(BettingStrategy):
    def __init__(self):
        super().__init__()
        self.name = "Hi-Lo Card Counting"

    def update_count(self, card):
        # Low cards (+1)
        if 2 <= card.value <= 6:
            self.running_count += 1
        # High cards and Aces (-1)
        elif card.value >= 10: 
            self.running_count -= 1

    def get_bet_size(self, base_bet, remaining_decks):
        true_count = self.running_count / max(1, remaining_decks)
        
        if true_count >= 2:
            # 1-to-10 bet spread based on true count
            bet_multiplier = min(int(true_count), 10) 
            return base_bet * bet_multiplier
        else:
            return base_bet