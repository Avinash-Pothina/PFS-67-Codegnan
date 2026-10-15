"""Command-line interface for the 2048 game."""

import logic

KEYS = {"w": "up", "s": "down", "a": "left", "d": "right"}
MAX_VALID_MOVES = 10  # Increase this number or set it to None for unlimited play.


def main() -> None:
    board = logic.new_board()
    announced_win = False
    valid_moves = 0
    print("2048 - combine matching tiles to reach 2048.")
    print(f"Move with W/A/S/D. Enter Q to quit. This demo ends after {MAX_VALID_MOVES} valid moves.\n")

    while True:
        print(logic.format_board(board))
        state = logic.game_state(board)
        if state == "won" and not announced_win:
            print("You reached 2048! You can keep playing until the demo move limit.")
            announced_win = True
        elif state == "lost":
            print("No moves remain. Game over!")
            return

        command = input("Move (W/A/S/D or Q): ").strip().lower()
        if command == "q":
            print("Thanks for playing!")
            return
        if command not in KEYS:
            print("Invalid input. Enter W, A, S, D, or Q.\n")
            continue

        # A new tile appears only after a move actually changes the board.
        if logic.move(board, KEYS[command]):
            logic.add_new_tile(board)
            valid_moves += 1
            if valid_moves >= MAX_VALID_MOVES:
                print(logic.format_board(board))
                print(f"Demo finished after {valid_moves} valid moves. Thanks for playing!")
                return
        else:
            print("That move changes nothing. Try another direction.\n")


if __name__ == "__main__":
    main()
