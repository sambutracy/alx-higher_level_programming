#!/usr/bin/python3
"""Solves the N-queens puzzle to find all solutions for placing non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): NxN chessboard represented as a list of lists.
    solutions (list): List of solutions, each represented as a list of queen positions [r, c].
"""

import sys


def init_board(n):
    """Initializes an `n`x`n` chessboard with 0's."""
    return [[' ' for i in range(n)] for j in range(n)]


def board_deepcopy(board):
    """Returns a deepcopy of a chessboard."""
    return [board_deepcopy(row) for row in board] if isinstance(board, list) else board


def get_solution(board):
    """Returns the list of lists representation of a solved chessboard."""
    return [[r, c] for r in range(len(board)) for c in range(len(board)) if board[r][c] == "Q"]


def xout(board, row, col):
    """X out spots on a chessboard where non-attacking queens can no longer be placed."""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solves an N-queens puzzle.

    Args:
        board (list): Current chessboard.
        row (int): Current row.
        queens (int): Current number of placed queens.
        solutions (list): List of solutions.

    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][col] = "Q"
            xout(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit() or int(sys.argv[1]) < 4:
        print("Usage: nqueens N")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
