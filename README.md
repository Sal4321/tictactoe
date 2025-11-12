# Tic Tac Toe with Value Iteration

A Python implementation of Tic Tac Toe featuring an AI opponent powered by **value iteration**, a reinforcement learning algorithm. The computer learns to evaluate board states and make optimal moves based on state values.

## Overview

This project implements a classic Tic Tac Toe game where:
- **Human player (X):** Makes moves interactively by entering a number (1-9)
- **Computer player (O):** Uses value iteration to select the best move based on learned state values

The game runs for multiple episodes (1000 by default), allowing the AI to improve through value iteration.

## Features

- **Value Iteration Learning:** The computer evaluates all possible board states and assigns values (1.0 for winning states, 0.5 for non-terminal states)
- **State Space Analysis:** Generates and evaluates all valid tic-tac-toe board configurations
- **Interactive Gameplay:** Human vs. Computer matches with turn-based play
- **Board Visualization:** ASCII display of the game board after each move

## Board Layout

The board positions are numbered 1-9:

```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

## How to Run

```bash
python3 tictactoe.py
```

The program will:
1. Initialize the game and all valid board states with their values
2. Start an interactive game loop for 1000 episodes
3. Prompt you to enter a move (1-9) on each turn
4. Display the updated board after each move
5. Announce winners or draws

## Game Rules

- Players alternate turns: Human (X) first, then Computer (O)
- A player wins by placing three of their symbols in a row (horizontally, vertically, or diagonally)
- If all 9 squares are filled with no winner, the game is a draw
- The game resets and continues for the next episode

## Project Structure

- **TicTacToe class:** Main game engine with the following methods:
  - `__init__()` — Initialize board and state values
  - `initializestatevalues()` — Generate and evaluate all valid board states
  - `check_winner()` — Check if a winning condition is met
  - `det_winner()` — Determine which player won
  - `updateboard()` — Update board with player move
  - `pickbest()` — AI selects best move using state values
  - `printboard()` — Display current board state
  - `clearboard()` — Reset board for next game

## State Values

- **1.0:** States where the computer (O) has won
- **0.5:** Terminal states where neither player has won (draw)
- The AI prioritizes moves leading to higher-value states

## Requirements

- Python 3.x
- Standard library only (no external dependencies)

## Example Game Session

```
Starting a new game

Please enter a number between 1 and 9: 5
You entered: 5
 |  | 
- - -
 | X | 
- - -
 |  | 

The computer chose 1
 O |  | 
- - -
 | X | 
- - -
 |  | 

Please enter a number between 1 and 9: 9
You entered: 9
 O |  | 
- - -
 | X | 
- - -
 |  | X

Winner is: X
```

## Future Enhancements

- Implement Q-learning for online learning during gameplay
- Add difficulty levels (random, greedy, optimal)
- Implement minimax algorithm for comparison
- Add save/load game state functionality
- Create graphical UI

## Author

Nazmus Salehin

## Notes

- The game uses value iteration with a fixed state evaluation approach
- The computer makes deterministic choices based on learned state values
- Consider implementing `updatestatevalues()` for dynamic value updates during training
