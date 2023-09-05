#!/usr/bin/python3
import sys
def solveNQueens(n):
    """This program solves the N Queens problem.
    
    N Queens problem: is a challange where you have to impliment code to place queens on the chessboard in positions where they cannot attack each otheh.
    Solution: The only way to solve this basicaly is to place each queen in their row, column and diagonal position in a way that no queens share the same row or column or diagonal lane.
    """
    def solve(row):
        """Checks through rows, colums and diagonal positions to check if they are elegible to place a Queen.

        Args:
            row: the row of the chessboard.
        """
        if row == n:
            res.append(["".join(row) for row in board[:]])
            return
        for c in range(n):
            if c not in col and (row + c) not in posdig and (row - c) not in negdig:
                board[row][c] = "Q"
                col.add(c)
                posdig.add(row + c)
                negdig.add(row - c)
                solve(row + 1)
                board[row][c] = "."
                col.remove(c)
                posdig.remove(row + c)
                negdig.remove(row - c)

    col = set()
    posdig = set()  # (r + c) is constant
    negdig = set()  # (r - c) is constant

    res = []
    board = [["." for _ in range(n)] for _ in range(n)]
    solve(0)
    return res

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solveNQueens(N)

    if not solutions:
        print(f"No solutions found for N = {N}")
    else:
        for solution in solutions:
            queen_positions = []
            for r, row in enumerate(solution):
                for c, cell in enumerate(row):
                    if cell == "Q":
                        queen_positions.append([r, c])
            print(queen_positions)
