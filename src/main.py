from Class.Game import Game  

if __name__ == '__main__':
    games_to_play = 10000
    
    # Trackers for our statistics
    wins = 0
    losses = 0
    pushes = 0
    blackjacks = 0
    total_hands_played = 0 # This will be > 10,000 because of splits!

    print(f"Simulating {games_to_play} games of Blackjack...")

    for i in range(games_to_play):
        # 1. Initialize and play the game
        bj_game = Game(verbose=False)
        bj_game.handlePlayerAction()
        
        # 2. Fetch the results for all hands played in this game
        outcomes = bj_game.getPlayerResults() 
        
        # 3. Tally the results
        for outcome in outcomes:
            total_hands_played += 1
            if outcome == "Win":
                wins += 1
            elif outcome == "Lose":
                losses += 1
            elif outcome == "Push":
                pushes += 1
            elif outcome == "Blackjack":
                blackjacks += 1

    # 4. Calculate and print the final percentages
    win_pct = (wins / total_hands_played) * 100
    loss_pct = (losses / total_hands_played) * 100
    push_pct = (pushes / total_hands_played) * 100
    bj_pct = (blackjacks / total_hands_played) * 100
    total_win_rate = ((wins + blackjacks) / total_hands_played) * 100

    print("\n#--------- SIMULATION RESULTS ---------#")
    print(f"Initial Games Dealt: {games_to_play}")
    print(f"Total Hands Played (including splits): {total_hands_played}")
    print("----------------------------------------")
    print(f"Wins:       {wins} ({win_pct:.2f}%)")
    print(f"Blackjacks: {blackjacks} ({bj_pct:.2f}%)")
    print(f"Losses:     {losses} ({loss_pct:.2f}%)")
    print(f"Pushes:     {pushes} ({push_pct:.2f}%)")
    print("----------------------------------------")
    print(f"Total Win Rate (Wins + Blackjacks): {total_win_rate:.2f}%")
    print("#--------------------------------------#")