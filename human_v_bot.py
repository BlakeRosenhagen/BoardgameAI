from dlgo1 import agent
from dlgo1.agent import naive
from dlgo1 import goboard_slow as goboard
from dlgo1 import gotypes
from dlgo1.utils import print_board, print_move, point_from_coords
from six.moves import input


def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bot = agent.naive.RandomBot()

    while not game.is_over():
        print(chr(27) + "[2J")
        
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