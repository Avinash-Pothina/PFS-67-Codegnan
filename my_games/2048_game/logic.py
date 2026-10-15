"""Core rules for a small terminal version of 2048."""

from __future__ import annotations

import random
from typing import Iterable

SIZE = 4
TARGET = 2048


def new_board() -> list[list[int]]:
    """Create a fresh board and place the starting tiles."""
    board = [[0] * SIZE for _ in range(SIZE)]
    add_new_tile(board)
    add_new_tile(board)
    return board


def add_new_tile(board: list[list[int]]) -> bool:
    """Add a 2 (90%) or 4 (10%) to an empty cell; return whether one was added."""
    empty = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if not empty:
        return False
    row, col = random.choice(empty)
    board[row][col] = 4 if random.random() < 0.1 else 2
    return True


def _merge_line(values: Iterable[int]) -> list[int]:
    """Slide and merge one line toward its beginning. Each tile merges once."""
    packed = [value for value in values if value]
    merged: list[int] = []
    index = 0
    while index < len(packed):
        if index + 1 < len(packed) and packed[index] == packed[index + 1]:
            merged.append(packed[index] * 2)
            index += 2
        else:
            merged.append(packed[index])
            index += 1
    return merged + [0] * (SIZE - len(merged))


def move(board: list[list[int]], direction: str) -> bool:
    """Apply a move in 'up', 'down', 'left', or 'right'; return whether board changed."""
    direction = direction.lower()
    if direction not in {"up", "down", "left", "right"}:
        raise ValueError("direction must be up, down, left, or right")

    before = [row[:] for row in board]
    if direction in {"left", "right"}:
        for row_index in range(SIZE):
            line = board[row_index] if direction == "left" else list(reversed(board[row_index]))
            result = _merge_line(line)
            board[row_index] = result if direction == "left" else list(reversed(result))
    else:
        for col in range(SIZE):
            line = [board[row][col] for row in range(SIZE)]
            if direction == "down":
                line.reverse()
            result = _merge_line(line)
            if direction == "down":
                result.reverse()
            for row in range(SIZE):
                board[row][col] = result[row]
    return board != before


def has_won(board: list[list[int]]) -> bool:
    return any(value >= TARGET for row in board for value in row)


def can_move(board: list[list[int]]) -> bool:
    """Return True if an empty cell or a horizontal/vertical merge is available."""
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:
                return True
            if col + 1 < SIZE and board[row][col] == board[row][col + 1]:
                return True
            if row + 1 < SIZE and board[row][col] == board[row + 1][col]:
                return True
    return False


def game_state(board: list[list[int]]) -> str:
    """Return 'won', 'playing', or 'lost'."""
    if has_won(board):
        return "won"
    return "playing" if can_move(board) else "lost"


def format_board(board: list[list[int]]) -> str:
    """Return a readable, aligned text representation of the board."""
    width = max(4, max((len(str(value)) for row in board for value in row), default=1))
    border = "+" + "+".join("-" * (width + 2) for _ in range(SIZE)) + "+"
    rows = [border]
    for row in board:
        rows.append("|" + "|".join(f" {value if value else '.':>{width}} " for value in row) + "|")
        rows.append(border)
    return "\n".join(rows)