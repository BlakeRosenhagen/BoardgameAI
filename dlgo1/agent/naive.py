import random
from dlgo1.agent.base import Agent
from dlgo1.agent.helpers import is_point_an_eye
from dlgo1.gotypes import Move
from dlgo1.gotypes import Point
from dlgo1.goboard_slow import Board

class RandomBot(Agent):
    def select_move(self, game_state):
        """Selects random value that preserves eyes"""
        candidates = []
        for r in range(1, game_state.board.num_rows + 1):
            for c in range(1, game_state.board.num_cols + 1):
                candidate = Point(row=r, col=c)#added first parameter to Move.play below to be "1"
                if game_state.is_valid_move(Move.play(candidate)) and \
                        not is_point_an_eye(game_state.board, \
                                        candidate, \
                                        game_state.next_player):
                    candidates.append(candidate)
        if not candidates:
            return Move.pass_turn()
        return Move.play(random.choice(candidates))
       