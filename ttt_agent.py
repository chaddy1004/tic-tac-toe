from typing import List

SCORE = {"Player": 1, "Opponent": -1, "Draw": 0}


class TTT_Agent():
    def __init__(self, token: str):
        self.my_token = token  # either O or X
        self.enemy_token = "X" if self.my_token == "O" else "O"
        self.go_first = (token == "X")  # X goes first
        self.best_move = None

        pass

    def checkWinner(self, board: List[List[str]]):
        unfinished = True
        for col in range(3):
            column = [board[0][col], board[1][col], board[2][col]]
            if " " in column:
                unfinished = True
            col_set = set(column)
            if len(col_set) == 1:
                if self.my_token in col_set:
                    return "Player"
                elif self.enemy_token in col_set:
                    return "Opponent"
                else:
                    pass

        for row in board:
            if " " in row:
                continue
            row_set = set(row)
            if len(row_set) == 1:
                if self.my_token in row_set:
                    return "Player"
                elif self.enemy_token in row_set:
                    return "Opponent"
                else:
                    pass

        diag1 = set([board[0][0], board[1][1], board[2][2]])
        if len(diag1) == 1:
            if self.my_token in diag1:
                return "Player"
            elif self.enemy_token in diag1:
                return "Opponent"
            else:
                pass

        diag2 = set([board[0][2], board[1][1], board[2][0]])
        if len(diag2) == 1:
            if self.my_token in diag2:
                return "Player"
            elif self.enemy_token in diag2:
                return "Opponent"
            else:
                pass

        if unfinished:
            return "Pending"
        else:
            return "Draw"

    def minimax(self, board: List[List[str]], myTurn):
        outcome = self.checkWinner(board)
        if outcome != "Pending":
            return SCORE[outcome]

        if myTurn:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = self.my_token
                        score = self.minimax(board=board, myTurn=False)
                        best_score = max(score, best_score)
                        board[row][col] = " "
            return best_score

        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = self.my_token
                        score = self.minimax(board=board, myTurn=True)
                        best_score = min(score, best_score)
                        board[row][col] = " "
            return best_score

    def choose_move(self, board: List[List[str]]):
        best_move = None
        best_score = float(-inf)
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    score = minimax(board=board, myTurn=True)
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move

    def __call__(self, *args, **kwargs):
        pass
