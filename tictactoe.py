from ttt_engine import TicTacToe
import pygame
import argparse


def main_game_single_player(start):
    ttt_game = TicTacToe(single_player=True, start=start)
    ttt_game.render_board()
    run = True
    if start == "agent":
        ttt_game.agent_move()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                changed = ttt_game.click()
                ttt_game.render_board()
                result = ttt_game.check_game_result()
                if result != "Pending":
                    if result == "Draw":
                        ttt_game.has_drawn()
                    else:
                        ttt_game.has_won(winner=result)
                    run = False
                    continue

                if changed:
                    ttt_game.agent_move()
                    ttt_game.render_board()
                    result = ttt_game.check_game_result()

                    if result != "Pending":
                        if result == "Draw":
                            ttt_game.has_drawn()
                        else:
                            ttt_game.has_won(winner=result)
                        run = False
        if run:
            ttt_game.render_board()


def main_game_two_player():
    ttt_game = TicTacToe(single_player=False, start=None)
    ttt_game.render_board()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                _ = ttt_game.click()
                ttt_game.render_board()
                result = ttt_game.check_game_result()
                if result != "Pending":
                    if result == "Draw":
                        ttt_game.has_drawn()
                    else:
                        ttt_game.has_won(winner=result)
                    run = False
                    continue

        ttt_game.render_board()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, help="Whether to run two-player mode or play with AI", required=True)
    parser.add_argument("--player_first", action='store_true')

    args = parser.parse_args()

    if args.mode == "two-player":
        while True:
            main_game_two_player()

    elif args.mode == "single-player":
        if args.player_first:
            while True:
                main_game_single_player(start="player")
        else:
            while True:
                main_game_single_player(start="agent")
    else:
        tp = "two-player"
        sp = "single-player"
        print(f"Not a valid mode. Either use the option {tp} or {sp} for --mode argument input")
