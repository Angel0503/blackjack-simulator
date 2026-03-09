from Class.Game import Game  
from Class.Deck import Deck
from Class.BettingStrategy import FlatBetting, HiLo, BettingStrategy
from Class.PlayingStrategy import BasicStrategy

if __name__ == '__main__':    
    #---SIMULATION SETTINGS---#
    games_to_play = 10_000
    number_of_decks = 6

    betting_strategy = HiLo() 
    # betting_strategy = FlatBetting()
    # betting_strategy = BettingStrategy()

    playing_strategy = BasicStrategy()

    #---BANKROLL SETTINGS---#
    starting_balance = 1000
    current_balance = starting_balance
    allow_negative_balance = True
    base_bet = 10

    #---STATISTICS SETUP---#
    wins, losses, pushes, blackjacks, total_hands = 0, 0, 0, 0, 0
    games_actually_played = 0
    reshuffles = 0

    print(f"Simulating {games_to_play} games with {number_of_decks} decks...")
    print(f"Betting Strategy: {betting_strategy.name}")
    print(f"Playing Strategy: {playing_strategy.name}")
    print(f"Starting Balance: ${starting_balance}")

    shoe = Deck(num_decks=number_of_decks, strategy=betting_strategy)
    for i in range(games_to_play):
        if not allow_negative_balance and current_balance < base_bet:
            print(f"\n❌ BANKRUPT! Player ran out of money at game {i+1}.")
            break
        
        if shoe.needs_reshuffle():
            shoe.build_and_shuffle()
            reshuffles += 1

        current_bet = betting_strategy.get_bet_size(base_bet, shoe.get_remaining_decks())
        bj_game = Game(
            deck=shoe, 
            playing_strategy=playing_strategy,
            balance=current_balance, 
            allow_negative=allow_negative_balance, 
            base_bet=base_bet,
            verbose=False
        ) 
        
        bj_game.handlePlayerAction()
        
        current_balance = bj_game.calculateFinalBalance()
        
        games_actually_played += 1
        outcomes = bj_game.getPlayerResults() 
        for outcome in outcomes:
            total_hands += 1
            if outcome == "Win": wins += 1
            elif outcome == "Lose": losses += 1
            elif outcome == "Push": pushes += 1
            elif outcome == "Blackjack": blackjacks += 1

    win_pct = (wins / total_hands) * 100
    loss_pct = (losses / total_hands) * 100
    push_pct = (pushes / total_hands) * 100
    bj_pct = (blackjacks / total_hands) * 100

    print("\n#--------- SIMULATION RESULTS ---------#")
    print(f"Games Played: {games_actually_played} / {games_to_play}")
    print(f"Total Hands Evaluated: {total_hands}")
    print(f"Shoe Reshuffles: {reshuffles}")
    print("----------------------------------------")
    print(f"Final Balance: ${current_balance:.2f}")
    print(f"Net Profit/Loss: ${(current_balance - starting_balance):.2f}")
    print("----------------------------------------")
    print(f"Wins:       {wins} ({win_pct:.2f}%)")
    print(f"Blackjacks: {blackjacks} ({bj_pct:.2f}%)")
    print(f"Losses:     {losses} ({loss_pct:.2f}%)")
    print(f"Pushes:     {pushes} ({push_pct:.2f}%)")
    print("#--------------------------------------#")