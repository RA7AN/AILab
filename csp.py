class NQueens:
    def __init__(self, N):
        self.N = N
        self.board = [[0 for _ in range(N)] for _ in range(N)]

    def is_safe(self, row, col):
        # Check if there's a queen in the same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.N)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve(self, row):
        if row >= self.N:
            return True

        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row][col] = 1

                if self.solve(row + 1):
                    return True

                self.board[row][col] = 0

        return False

    def print_solution(self):
        if not self.solve(0):
            print("No solution exists")
            return

        for row in self.board:
            print(' '.join(map(str, row)))

# Example usage:
if __name__ == "__main__":
    N = 4  # Size of the chessboard
    n_queens = NQueens(N)
    n_queens.print_solution()
