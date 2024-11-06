def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")


def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n, solutions):
    # Base case: If all queens are placed, add the board to solutions
    if col >= n:
        # Make a deep copy of the board to add as a solution
        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            # Place queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_n_queens_util(board, col + 1, n, solutions)

            # Backtrack: Remove the queen from the current position
            board[i][col] = 0


def solve_n_queens(n):
    # Initialize board with all 0's
    board = [[0] * n for _ in range(n)]
    solutions = []

    # Find all solutions
    solve_n_queens_util(board, 0, n, solutions)

    # Print all solutions
    print(f"Total number of solutions for a {n}x{n} board: {len(solutions)}\n")
    for index, solution in enumerate(solutions):
        print(f"Solution {index + 1}:")
        print_board(solution)


# Get the board size from the user
n = int(input("Enter the size of the board (n for an n x n board): "))
solve_n_queens(n)
