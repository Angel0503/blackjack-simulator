from Class.Game import Game  

if __name__ == '__main__':
    games_to_play = 10_000
    
    # --- BANKROLL SETTINGS ---
    starting_balance = 1000
    current_balance = starting_balance
    allow_negative_balance = True
    
    wins, losses, pushes, blackjacks, total_hands = 0, 0, 0, 0, 0
    games_actually_played = 0

    print(f"Simulating {games_to_play} games of Blackjack...")
    print(f"Starting Balance: ${starting_balance}")

    for i in range(games_to_play):
        if not allow_negative_balance and current_balance < 10:
            print(f"\n❌ BANKRUPT! Player ran out of money at game {i+1}.")
            break
            
        bj_game = Game(balance=current_balance, allow_negative=allow_negative_balance, verbose=False) 
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

    # --- RESULTS ---
    win_pct = (wins / total_hands) * 100
    loss_pct = (losses / total_hands) * 100
    push_pct = (pushes / total_hands) * 100
    bj_pct = (blackjacks / total_hands) * 100

    print("\n#--------- SIMULATION RESULTS ---------#")
    print(f"Games Played: {games_actually_played} / {games_to_play}")
    print(f"Total Hands Evaluated: {total_hands}")
    print("----------------------------------------")
    print(f"Final Balance: ${current_balance:.2f}")
    print(f"Net Profit/Loss: ${(current_balance - starting_balance):.2f}")
    print("----------------------------------------")
    print(f"Wins:       {wins} ({win_pct:.2f}%)")
    print(f"Blackjacks: {blackjacks} ({bj_pct:.2f}%)")
    print(f"Losses:     {losses} ({loss_pct:.2f}%)")
    print(f"Pushes:     {pushes} ({push_pct:.2f}%)")
    print("#--------------------------------------#")