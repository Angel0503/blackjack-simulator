import random
from Class.Game import Game  
from Class.Deck import Deck
from Class.BettingStrategy import FlatBetting, HiLo
from Class.PlayingStrategy import BasicStrategy, NeverBustStrategy

if __name__ == '__main__':    
    games_to_play = 10_000
    number_of_decks = 6
    starting_balance = 1000
    base_bet = 10
    allow_negative_balance = False
    
    playing_strategies = [BasicStrategy(), NeverBustStrategy()]
    betting_strategies = [FlatBetting(), HiLo()]

    comparison_results = []

    print(f"Starting comparison matrix: {games_to_play} games per combination...\n")

    for p_strat in playing_strategies:
        for b_strat in betting_strategies:
            random.seed(42)
            
            current_balance = starting_balance
            wins, total_hands = 0, 0
            
            print(f"Testing: [{p_strat.name}] + [{b_strat.name}]...")

            shoe = Deck(num_decks=number_of_decks, strategy=b_strat)
            
            for i in range(games_to_play):
                if current_balance < base_bet:
                    break
                
                if shoe.needs_reshuffle():
                    shoe.build_and_shuffle()

                current_bet = b_strat.get_bet_size(base_bet, shoe.get_remaining_decks())

                bj_game = Game(
                    deck=shoe, 
                    playing_strategy=p_strat, 
                    balance=current_balance, 
                    allow_negative=allow_negative_balance,
                    base_bet=current_bet, 
                    verbose=False
                ) 
                
                bj_game.handlePlayerAction()
                current_balance = bj_game.calculateFinalBalance()
                
                outcomes = bj_game.getPlayerResults() 
                for outcome in outcomes:
                    total_hands += 1
                    if outcome in ["Win", "Blackjack"]:
                        wins += 1

            net_profit = current_balance - starting_balance
            win_rate = (wins / total_hands) * 100 if total_hands > 0 else 0
            
            comparison_results.append({
                "Playing Strategy": p_strat.name,
                "Betting Strategy": b_strat.name,
                "Net Profit": net_profit,
                "Win Rate": win_rate,
                "Bankrupt": current_balance < base_bet
            })

    print("\n#======================= STRATEGY LEADERBOARD =======================#")
    print(f"{'PLAYING STRATEGY':<25} | {'BETTING STRATEGY':<20} | {'WIN RATE':<8} | {'NET PROFIT'}")
    print("-" * 75)
    
    comparison_results.sort(key=lambda x: x["Net Profit"], reverse=True)
    
    for res in comparison_results:
        profit_str = f"${res['Net Profit']:.2f}"
        if res['Bankrupt']:
            profit_str = "BANKRUPT"
            
        print(f"{res['Playing Strategy']:<25} | {res['Betting Strategy']:<20} | {res['Win Rate']:>7.2f}% | {profit_str}")
    print("#====================================================================#")