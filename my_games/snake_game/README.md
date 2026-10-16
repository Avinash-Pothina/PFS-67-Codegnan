# Classic Snake Game

A simple Snake game written in Python with the built-in Turtle graphics library. Steer the yellow triangle around the play area, eat the red food, and grow the green body.

## Requirements

- Python 3
- No third-party Python packages are required.

## Run the game

1. Keep `snake_game.py` in a folder where you can save files.
2. Open a terminal or command prompt in that folder.
3. Run:

   ```text
   python snake_game.py
   ```

   On some Windows installations, use:

   ```text
   py snake_game.py
   ```

4. Click the game window, then use a direction key to start moving.

## Controls

| Key | Action |
| --- | --- |
| Arrow keys | Steer the snake |
| W, A, S, D | Alternative movement controls |
| P | Pause or resume the game |
| R | Replay after game over |
| Q | Close the game window |

The snake cannot turn directly back into itself. At the edges of the play area, it appears on the opposite side. The round ends when the head touches the snake's body.

## Scoring and speed

- Each food item adds 10 points and one body segment.
- The game begins with a 150 millisecond delay between moves.
- Each food item reduces the delay by 2 milliseconds, making the snake faster.
- The delay cannot go below 50 milliseconds per move.

## High score

The game looks for `snake_high_score.csv` in the same folder as `snake_game.py`. If the file is missing, the high score starts at 0. When you beat the saved high score, the game creates or updates the CSV file.

Keep the game script in a folder where Python can write the CSV file.
