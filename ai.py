import math

class MinimaxAI:
    def best_move(self, board_obj):
        best_score = -math.inf
        move = None
        board = board_obj.board

        for row, col in board_obj.available_moves():
            board[row][col] = "O"
            score = self.minimax(board_obj, 0, False)
            board[row][col] = ""
            if score > best_score:
                best_score = score
                move = (row, col)
        return move

    def minimax(self, board_obj, depth, is_max):
        winner = board_obj.check_winner()
        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        elif winner == "Draw":
            return 0

        if is_max:
            best = -math.inf
            for row, col in board_obj.available_moves():
                board_obj.board[row][col] = "O"
                score = self.minimax(board_obj, depth + 1, False)
                board_obj.board[row][col] = ""
                best = max(score, best)
            return best
        else:
            best = math.inf
            for row, col in board_obj.available_moves():
                board_obj.board[row][col] = "X"
                score = self.minimax(board_obj, depth + 1, True)
                board_obj.board[row][col] = ""
                best = min(score, best)
            return best