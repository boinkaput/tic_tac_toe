# Tic Tac Toe

This is a Tic Tac Toe game implemented using Python and Pygame. The game allows the user to select between Player vs. Player (PvP) and Player vs. AI (PvE) modes. In PvE mode, the AI opponent utilizes the Minimax algorithm to make optimal moves.

## Installation

To install the game, follow these steps:
1. Clone the repository or download the source code.
2. Open a terminal and navigate to the project directory.
3. Ensure you have Python 3 installed on your machine.
4. Run the following command to install the required dependencies:
```shell
./install
```

## Usage

To run the game, execute the following command in your terminal:
```shell
python3 -m tic_tac_toe.py
```

When the game starts, the main menu will be displayed, allowing the user to choose the game mode.

* PvP Mode: Selecting this option will start a two-player game where two human players can take turns playing against each other.
* PvE Mode: Selecting this option will start a game where the user can play against an AI opponent. The AI opponent uses the Minimax algorithm to make optimal moves.

In the PvE mode, the AI opponent will analyze the game state and make moves based on the Minimax algorithm, ensuring a challenging game experience.

The game will continue until there is a winner or a draw. The final result will be displayed, and the user will have the option to play again or exit the game.

## Dependencies

The game requires the following dependencies:
- Python3
- Pygame
