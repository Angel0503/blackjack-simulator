# 🎰 Python Blackjack Simulator

A fully functional, object-oriented Blackjack simulation built in Python. This project is designed to simulate thousands of Blackjack hands in seconds using mathematically optimal basic strategy, complete with bankroll tracking, realistic casino payouts, and advanced hand handling (like recursive splitting and doubling down).

## ✨ Features

* **Basic Strategy Automation:** The virtual player makes mathematically optimal decisions (Hit, Stand, Double, Split) based on their hand and the dealer's upcard.
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
            └── Hand.py            # Hand evaluation, score counting, and basic strategy

## ⚙️ Prerequisites

* **Python 3.10 or higher:** This project utilizes Python's `match ... case` syntax, which is only available in Python 3.10+.
* No external libraries are required! The project uses Python's built-in modules (like `random`).

## 🚀 Setup and Installation

1.  **Clone or Download** this repository to your local machine.
2.  Ensure your file structure matches the diagram above (with the `Class` folder).
3.  Open your terminal or command prompt.
4.  Navigate to the project root folder.
5.  Run the main script:
    `python main.py`

## 🎮 Usage & Configuration

You can easily tweak the simulation parameters by editing the variables inside the `if __name__ == '__main__':` block in `main.py`:

* **`games_to_play`**: Change the number of games to simulate (e.g., `10_000`).
* **`starting_balance`**: Set the player's initial bankroll (e.g., `1000`).
* **`allow_negative_balance`**: 
    * Set to `True` for an infinite bankroll (good for pure statistical testing).
    * Set to `False` for realistic casino rules (simulation stops if the player goes bankrupt).
* **Verbose Mode**: To see a game played out step-by-step, change `verbose=False` to `verbose=True` when initializing the game:
    `bj_game = Game(balance=current_balance, allow_negative=allow_negative_balance, verbose=True)`

## 📊 Example Output (Simulation Mode)

    Simulating 10000 games of Blackjack...
    Starting Balance: $1000
    
    #--------- SIMULATION RESULTS ---------#
    Games Played: 10000 / 10000
    Total Hands Evaluated: 10245
    ----------------------------------------
    Final Balance: $845.00
    Net Profit/Loss: $-155.00
    ----------------------------------------
    Wins:       4310 (42.07%)
    Blackjacks: 482 (4.70%)
    Losses:     4915 (47.97%)
    Pushes:     538 (5.25%)
    #--------------------------------------#