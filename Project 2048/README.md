# 2048 Game

A Python implementation of the classic 2048 game. This project brings the popular tile-matching puzzle game to life using basic game mechanics and logic, creating an interactive gaming experience with a minimalistic approach.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Contributing](#contributing)
- [License](#license)

## Overview
2048 is a sliding tile puzzle game where the goal is to combine like-numbered tiles on a grid to reach the tile with the number 2048. The game ends when there are no more moves to make. This Python implementation mimics the desktop version of the game and can be played via the terminal.

## Features
- **Interactive Gameplay**: Move tiles using arrow keys to combine them and create higher numbers.
- **Grid System**: A 4x4 grid where tiles with similar values merge together when moved.
- **Game Over Detection**: Game stops when there are no more valid moves.
- **Score Tracking**: The player’s score increases as tiles are combined.
- **Undo Feature**: Allows players to undo a move to test different strategies.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/kvamsi7/fun_projects.git
    ```

2. Navigate to the project directory:
    ```bash
    cd fun_projects/Project%202048
    ```

3. Install the required dependencies (if any). You can create a virtual environment and install dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the game:
    ```bash
    python 2048.py
    ```

## How to Play
1. Use the arrow keys (Up, Down, Left, Right) to move the tiles.
2. Combine matching tiles to double their value.
3. Keep playing until you reach the 2048 tile or run out of moves.
4. Press 'q' to quit the game at any time.

## Contributing
Contributions are welcome! To contribute to this project, fork the repository, create a new branch, and submit a pull request. 

<!-- ## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.--?
