"""Command-line interface for the 2048 game."""

import logic

KEYS = {"w": "up", "s": "down", "a": "left", "d": "right"}


def main():
    board = logic.new_board()
    announced_win = False
    print("2048 - combine matching tiles to reach 2048.")
    print("Move with W/A/S/D. Enter Q to quit. You can keep playing after reaching 2048.\n")

    while True:
        print(logic.format_board(board))
        state = logic.game_state(board)
        if state == "won" and not announced_win:
            print("You reached 2048! You can keep playing or quit with Q.")
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
        else:
            print("That move changes nothing. Try another direction.\n")


if __name__ == "__main__":
    main()