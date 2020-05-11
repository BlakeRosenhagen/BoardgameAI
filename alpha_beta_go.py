from six.moves import input
from dlgo1 import goboard
from dlgo1 import gotypes
from dlgo1 import minimax

from dlgo1.utils import print_board, print_move, point_from_coords

def main():
    BOARD_SIZE = 9
    DEPTH = 3
    game = goboard.GameState.new_game(BOARD_SIZE)
    bot = minimax.AlphaBeta_Agent(DEPTH, capture_diff)
    while not game.is_over():
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            point = point_from_coords(human_move.strip())
            move = goboard.Move.play(point)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)






if __name__ == '__main__':
    main()