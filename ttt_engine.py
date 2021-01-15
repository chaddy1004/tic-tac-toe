import pygame
import math
from typing import List
from ttt_agent import TTT_Agent

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)


class TicTacToe():
    def __init__(self, single_player=True, start="player"):
        # Screen
        pygame.init()
        self.single_player = single_player
        self.agent = None
        self.WIDTH = 500
        self.ROWS = 3
        self.win = pygame.display.set_mode((self.WIDTH, self.WIDTH))
        pygame.display.set_caption("TicTacToe")

        # Colors

        # Fonts
        self.RESULT_FONT = pygame.font.Font('SDSamliphopangcheTTFOutline.ttf', 40)
        self.DRAW_FONT = pygame.font.Font('SDSamliphopangcheTTFOutline.ttf', 50)

        self.gap = self.WIDTH // self.ROWS
        self.start = start
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.playable_positions = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
        self.position_array = [[None, None, None], [None, None, None], [None, None, None]]
        self.x_turn = True
        self.o_turn = False
        self.x_token = "X"  # either O or X
        self.o_token = "O"
        if self.single_player:
            self.agent = TTT_Agent(token=self.o_token)

        self.initialize_grid()

    def draw_grid(self):
        # Starting points
        x = 0
        y = 0

        for i in range(self.ROWS):
            x = i * self.gap
            pygame.draw.line(self.win, GRAY, (x, 0), (x, self.WIDTH), 3)
            pygame.draw.line(self.win, GRAY, (0, x), (self.WIDTH, x), 3)

    def initialize_grid(self):
        half_grid_length = (self.WIDTH // 3) // 2

        for row in range(3):
            for col in range(3):
                x = half_grid_length * (2 * col + 1)
                y = half_grid_length * (2 * row + 1)

                # Adding centre coordinates
                self.position_array[row][col] = (x, y)

    def click(self):
        padding= 20
        distance_to_grid_centre = (((self.WIDTH // 3) // 2)**2 +  ((self.WIDTH // 3) // 2)**2)**(0.5) - padding
        # Mouse position
        m_x, m_y = pygame.mouse.get_pos()
        changed = False
        for row in range(3):
            for col in range(3):
                mark = self.board[row][col]
                x, y = self.position_array[row][col]
                is_playable = (row,col) in self.playable_positions
                # Distance between mouse and the centre of the square
                dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)

                # If it's inside the square
                print(m_x, m_y, x,y,dis, distance_to_grid_centre)
                if dis < distance_to_grid_centre and is_playable:
                    if self.start == "player":  # If it's X's turn
                        self.board[row][col] = 'X'

                    elif self.start == "agent":  # If it's O's turn
                        self.board[row][col] = 'O'
                    self.playable_positions.remove((row, col))
                    changed = True

        print("at click")
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        return changed

    def agent_move(self):
        if len(self.playable_positions) > 0:
            row, col = self.agent.choose_move(board=self.board)
            if self.start == "player":  # If it's X's turn
                self.board[row][col] = 'O'

            elif self.start == "agent":  # If it's O's turn
                self.board[row][col] = 'X'
            self.playable_positions.remove((row, col))
        else:
            print("HERE")
            return

    def check_game_result(self):
        unfinished = False
        for col in range(3):
            column = [self.board[0][col], self.board[1][col], self.board[2][col]]
            if " " in column:
                unfinished = True
            col_set = set(column)
            if len(col_set) == 1:
                if self.x_token in col_set:
                    return "X"
                elif self.o_token in col_set:
                    return "O"
                else:
                    pass

        for row in self.board:
            if " " in row:
                continue
            row_set = set(row)
            if len(row_set) == 1:
                if self.x_token in row_set:
                    return "X"
                elif self.o_token in row_set:
                    return "O"
                else:
                    pass

        diag1 = {self.board[0][0], self.board[1][1], self.board[2][2]}
        if len(diag1) == 1:
            if self.x_token in diag1:
                return "X"
            elif self.o_token in diag1:
                return "O"
            else:
                pass

        diag2 = {self.board[0][2], self.board[1][1], self.board[2][0]}
        if len(diag2) == 1:
            if self.x_token in diag2:
                return "X"
            elif self.o_token in diag2:
                return "O"
            else:
                pass
        print("check")
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        if unfinished:
            return "Pending"
        else:
            return "Draw"

    def render_board(self):
        self.win.fill(WHITE)
        self.draw_grid()

        # Drawing X's and O's
        for row in range(3):
            for col in range(3):
                x, y = self.position_array[row][col]
                mark = self.board[row][col]
                mark_text = self.DRAW_FONT.render(mark, True, BLACK)
                self.win.blit(mark_text, (x - mark_text.get_width() // 2, y - mark_text.get_height() // 2))

        pygame.display.update()

    def display_message(self, content):
        pygame.time.delay(500)
        self.win.fill(WHITE)
        end_text = self.RESULT_FONT.render(content, True, BLACK)
        self.win.blit(end_text, ((self.WIDTH - end_text.get_width()) // 2, (self.WIDTH - end_text.get_height()) // 2))
        pygame.display.update()
        pygame.time.delay(3000)

    def has_drawn(self):
        self.display_message(content="It's a draw!")
        return True

    def has_won(self, winner):
        self.display_message(content=f"{winner} won!")
        return True


def main():
    ttt_game = TicTacToe()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ttt_game.click()

        ttt_game.render_board()
        result = ttt_game.check_game_result()
        print(result)
        if result != "Pending":
            if result == "Draw":
                ttt_game.has_drawn()
            else:
                ttt_game.has_won(winner=result)
            run = False

#
# while True:
#     if __name__ == '__main__':
#         main()
