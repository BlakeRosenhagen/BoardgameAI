import random

from dlgo1.agent.base import Agent
from dlgo1 import gotypes
from dlgo1.gotypes import Player

MAX_SCORE = 999999
MIN_SCORE = -999999

#https://en.wikipedia.org/wiki/Tree_traversal


#-------------------------------------------------------------------------
#determining decisions based on the diffeerence of white 
# and black stones to "head in the right direction"


def capture_diff(game_state):
    black_stones = 0
    white_stones = 0
    for r in range(1, game_state.board.num_rows + 1):
        for c in range(1, game_state.board.num_cols + 1):
            p = gotypes.Point(r,c)
            color = game_state.board.get(p)
            if color == gotypes.Player.black:
                black_stones += 1
            if color == gotypes.Player.white:
                white_stones += 1
    diff = black_stones - white_stones
    if game_state.next_player == gotypes.Player.black:
        return diff
    return -1 * diff

#------------------------------------------------------------------------------------


#called in select_move in AlphaBetaAgent
def alpha_beta_result(game_state, max_depth, best_black, best_white, eval_fn):
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return MAX_SCORE
        else:
            return MIN_SCORE
    if max_depth == 0:
        return eval_fn(game_state)
    best_so_far = MIN_SCORE
    for candidate_move in game_state.legal_moves():
        print(str(max_depth))
        next_state = game_state.apply_move(candidate_move)
        opponent_best_result = alpha_beta_result(
            next_state, max_depth - 1,
            best_black, best_white,
            eval_fn)
        our_result = -1 * opponent_best_result
        if our_result > best_so_far:
            best_so_far = our_result
        if game_state.next_player == Player.white:
            if best_so_far > best_white:
                best_white = best_so_far
            outcome_for_black = -1 * best_so_far
            if outcome_for_black < best_black:
                return best_so_far
        elif game_state.next_player == Player.black:
            if best_so_far > best_black:
                best_black = best_so_far
            outcome_for_white = -1 * best_so_far
            if outcome_for_white < best_white:
                return best_so_far
    return best_so_far

# capture_diff is and example of eval_fn
class AlphaBetaAgent(Agent):
    def __init__(self, max_depth, eval_fn):
        Agent.__init__(self)
        self.max_depth = max_depth
        self.eval_fn = eval_fn
    def select_move(self, game_state):
        best_moves = []
        best_score = None
        best_black = MIN_SCORE
        best_white = MIN_SCORE
        #
        #
        #
        #fixed non-iterable
        legal_move_list = game_state.legal_moves()
        for possible_move in legal_move_list:
            print("1st")
            next_state = game_state.apply_move(possible_move)
            opponent_best_outcome = alpha_beta_result(next_state, self.max_depth, best_black, best_white, self.eval_fn)
            our_best_outcome = -1 * opponent_best_outcome
            if (not best_moves) or our_best_outcome > best_score:
                best_moves = [possible_move]
                best_score = our_best_outcome
                if game_state.next_player == Player.black:
                    best_black = best_score
                elif game_state.next_player == Player.white:
                    best_white = best_score
            elif our_best_outcome == best_score:
                best_moves.append(possible_move)
        return random.choice(best_moves)

