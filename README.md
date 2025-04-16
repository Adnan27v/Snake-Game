# Snake Game

A classic Snake game implementation using Python's Turtle graphics library. This project features a modern take on the classic arcade game with smooth controls, score tracking, and high score functionality.

## Features

- 🎮 Classic Snake gameplay
- ⬆️ Intuitive controls using both arrow keys and WASD
- 📊 Score tracking and high score system
- 🎯 Random food generation
- 🎨 Clean, modern graphics with a dark theme
- 🔄 Game reset functionality
- 🏆 Persistent high score storage

## Requirements

- Python 3.x
- Turtle graphics library (built-in with Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/snake-game.git
cd snake-game
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## How to Play

1. Run the game:
```bash
python main.py
```

2. Controls:
   - Use `WASD` or `Arrow Keys` to control the snake
   - Press `R` and then 'Click on screen' to exit the game
   - Click the window to exit

3. Game Rules:
   - Eat the food to grow longer and increase your score
   - Avoid hitting the walls or yourself
   - Try to beat your high score!

## Project Structure

- `main.py` - Main game loop and setup
- `snake.py` - Snake class implementation
- `food.py` - Food class implementation
- `scoreboard.py` - Score tracking and display
- `highscore.txt` - Stores the highest score achieved

## Contributing

Feel free to fork this project and submit pull requests with improvements!

## License

This project is open source and available under the MIT License. 
