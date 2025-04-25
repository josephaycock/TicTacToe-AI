from constants import *
from ai import MinimaxAI

class GameBoard:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]

    def mark(self, row, col, player):
        if self.board[row][col] == "":
            self.board[row][col] = player
            return True
        return False

    def is_full(self):
        return all(cell != "" for row in self.board for cell in row)

    def check_winner(self):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != "":
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != "":
                return b[0][i]
        if b[0][0] == b[1][1] == b[2][2] != "":
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != "":
            return b[0][2]
        return "Draw" if self.is_full() else None

    def available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ""]

    def reset(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]

class GameManager:
    def __init__(self):
        self.board = GameBoard()
        self.current_player = "X"
        self.ai = MinimaxAI()
        self.winner = None
        self.over = False

    def make_move(self, row, col):
        if not self.over and self.board.mark(row, col, self.current_player):
            self.winner = self.board.check_winner()
            self.over = self.winner is not None
            if not self.over:
                self.ai_move()
            return True
        return False

    def ai_move(self):
        row, col = self.ai.best_move(self.board)
        self.board.mark(row, col, "O")
        self.winner = self.board.check_winner()
        self.over = self.winner is not None

    def reset(self):
        self.board.reset()
        self.current_player = "X"
        self.winner = None
        self.over = False