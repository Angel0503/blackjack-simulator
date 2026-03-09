# 🎰 Python Blackjack Simulator

A fully functional, object-oriented Blackjack simulation built in Python. This project is designed to simulate thousands of Blackjack hands in seconds using mathematically optimal basic strategy, complete with bankroll tracking, realistic casino payouts, and advanced hand handling (like recursive splitting and doubling down).

## ✨ Features

* **Dual-Strategy Engine:** Employs the Strategy Design Pattern to separate *how* the player plays from *how* they bet. Seamlessly swap between different `PlayingStrategy` modules (like perfect Basic Strategy) and `BettingStrategy` modules (like Flat Betting or dynamic Hi-Lo Card Counting).
* **Realistic Casino Shoe:** Simulates a persistent multi-deck shoe (e.g., 6 or 8 decks) across games. Cards are dealt continuously and the shoe is only reshuffled when the "cut card" is reached (75% empty), perfectly mirroring real-world casino variance.
* **Advanced Hand Management:** Seamlessly handles edge cases like dynamic Aces (switching from 11 to 1 to avoid busting) and recursive hand splitting (splitting a hand, then splitting the splits).
* **Realistic Bankroll Tracking:** Tracks player balance across thousands of games. Features 3:2 payouts for Blackjacks, 1:1 for standard wins, and bankroll checks to prevent doubling/splitting when broke.
* **Simulation & Verbose Modes:** Run massive 10,000+ game simulations silently to gather win/loss statistics, or toggle `verbose=True` to watch a game play out card-by-card in the terminal.

## 📂 Project Structure

The code relies on a specific directory structure. Make sure your files are organized like this:

    blackjack-simulator/
    │
    ├── docs/                      
    │   └── basic-strategy.jpg     # Visual basic strategy guide
    │
    └── src/                      
        ├── main.py                # The entry point to run the simulation
        │
        └── Class/                 
            ├── Card.py            # Card object definition and math logic
            ├── Deck.py            # Deck generation, shuffling, and dealing logic
            ├── Game.py            # The main game engine and turn loop
            ├── Hand.py            # Hand evaluation and score counting
            ├── PlayingStrategy.py # Decision making logic (Hit, Stand, Double, Split)
            └── BettingStrategy.py # Betting strategies (Flat, Hi-Lo)

## ⚙️ Prerequisites

* **Python 3.10 or higher:** This project utilizes Python's `match ... case` syntax, which is only available in Python 3.10+.
* No external libraries are required! The project uses Python's built-in modules (like `random`).

## 🚀 Setup and Installation

1.  **Clone or Download** this repository to your local machine.
2.  Ensure your file structure matches the diagram above (with the `Class` folder).
3.  Open your terminal or command prompt.
4.  Navigate to the `src` directory of the project:
    `cd src`
5.  Run the main script:
    `python main.py`

## 🎮 Usage & Configuration

You can easily tweak the simulation parameters by editing the variables inside the `if __name__ == '__main__':` block in `main.py`:

* **`playing_strategy`**: Choose how the virtual player plays their cards (e.g., `BasicStrategy()`).
* **`betting_strategy`**: Choose how the virtual player manages their bankroll (e.g., `FlatBetting()` or `HiLo()`).
* **`games_to_play`**: Change the number of games to simulate (e.g., `10_000`).
* **`number_of_decks`**: Change the size of the shoe (e.g., `6` for standard modern casinos).
* **`starting_balance`**: Set the player's initial bankroll (e.g., `1000`).
* **`allow_negative_balance`**: 
    * Set to `True` for an infinite bankroll (good for pure statistical testing).
    * Set to `False` for realistic casino rules (simulation stops if the player goes bankrupt).
* **Verbose Mode**: To see a game played out step-by-step, change `verbose=False` to `verbose=True` when initializing the game:
    `bj_game = Game(deck=shoe, playing_strategy=playing_strategy, balance=current_balance, allow_negative=allow_negative_balance, base_bet=current_bet, verbose=True)`

## 📊 Example Output (Simulation Mode)

    Simulating 10000 games with 6 decks...
    Betting Strategy: Hi-Lo Card Counting
    Playing Strategy: Perfect Basic Strategy
    Starting Balance: $1000
    
    #--------- SIMULATION RESULTS ---------#
    Games Played: 10000 / 10000
    Total Hands Evaluated: 10245
    Shoe Reshuffles: 135
    ----------------------------------------
    Final Balance: $2145.00
    Net Profit/Loss: $1145.00
    ----------------------------------------
    Wins:       4310 (42.07%)
    Blackjacks: 482 (4.70%)
    Losses:     4915 (47.97%)
    Pushes:     538 (5.25%)
    #--------------------------------------#