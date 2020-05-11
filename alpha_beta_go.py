from six.moves import input
from dlgo1 import goboard_slow
from dlgo1 import gotypes
from dlgo1 import minimax
from dlgo1.minimax import alphabeta
from dlgo1.minimax.alphabeta import AlphaBetaAgent 
from dlgo1.minimax.alphabeta import capture_diff

from dlgo1.utils import print_board, print_move, point_from_coords


def main():
    BOARD_SIZE = 9
    DEPTH = 3
    game = goboard_slow.GameState.new_game(BOARD_SIZE)
    bot = alphabeta.AlphaBetaAgent(DEPTH, capture_diff)
    while not game.is_over():
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            point = point_from_coords(human_move.strip())
            move = gotypes.Move.play(point)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)



if __name__ == '__main__':
    main()