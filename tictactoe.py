# Initializing Pygame
from ttt_engine import TicTacToe
import pygame


def main_single_player():
    ttt_game = TicTacToe(single_player=True)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ttt_game.click()

        ttt_game.render_board()
        ttt_game.agent_move()
        ttt_game.render_board()
        result = ttt_game.check_game_result()
        print(result)
        if result != "Pending":
            if result == "Draw":
                ttt_game.has_drawn()
            else:
                ttt_game.has_won(winner=result)
            run = False


while True:
    if __name__ == '__main__':
        main_single_player()
