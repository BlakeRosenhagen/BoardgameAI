# Antagonistic bot setup

from dlgo1 import agent
from dlgo1.agent.naive import RandomBot
from dlgo1 import goboard_slow
from dlgo1 import gotypes
from dlgo1.utils import print_board, print_move
import time

def main():
    board_size = 9
    game = goboard_slow.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: agent.naive.RandomBot(),
        gotypes.Player.white: agent.naive.RandomBot(),
    }
    while not game.is_over():
        #time between each move
        time.sleep(.1)

        print(chr(27) + "[2J")
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)










if __name__ == '__main__':
    main()