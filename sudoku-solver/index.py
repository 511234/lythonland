from pprint import pprint


def find_next_empty(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:  # If this coordinate is empty
                return row, column

    return None, None  # All blocks have been filled


def solve_sudoku(puzzle):
    row, column = find_next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, column):
            puzzle[row][column] = guess
            if solve_sudoku(puzzle):
                return True

        puzzle[row][column] = -1

    return False


def is_valid(puzzle, guess, row, col):
    row_values = puzzle[row]
    if guess in row_values:
        return False

    col_values = [puzzle[i][col] for i in range(9)]
    if guess in col_values:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


if __name__ == "__main__":
    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],
        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],
        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1],
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
