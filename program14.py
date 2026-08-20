from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    result = []

    board = [["."] * n for _ in range(n)]

    columns = set()
    diagonals = set()
    anti_diagonals = set()

    def backtrack(row):
        # All queens placed
        if row == n:
            result.append(["".join(row) for row in board])
            return

        for col in range(n):

            # Check if column or diagonal is already occupied
            if col in columns:
                continue

            if row - col in diagonals:
                continue

            if row + col in anti_diagonals:
                continue

            # Place queen
            board[row][col] = "Q"
            columns.add(col)
            diagonals.add(row - col)
            anti_diagonals.add(row + col)

            # Move to next row
            backtrack(row + 1)

            # Remove queen (backtrack)
            board[row][col] = "."
            columns.remove(col)
            diagonals.remove(row - col)
            anti_diagonals.remove(row + col)

    backtrack(0)

    return result


# Example
n = 4

solutions = solveNQueens(n)

print("Number of solutions:", len(solutions))

for solution in solutions:
    for row in solution:
        print(row)
    print()
