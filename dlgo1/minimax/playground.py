import random
from dlgo1.agent.base import Agent
from dlgo1.agent.helpers import is_point_an_eye
from dlgo1.gotypes import Move
from dlgo1.gotypes import Point
from dlgo1.goboard_slow import Board




#--------------------------------------------------------
#determining decisions based on the diffeerence of white 
# and black stones to "head in the right direction"




def best_resultttt(game_state, max_depth, eval_fn):
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return MAX_SCORE
        else:
            return MIN_SCORE
    if max_depth == 0:
        return eval_fn(game_state)

    best_so_far = MIN_SCORE

    for candidate_move in game_State.legal_moves():
        next_state = game_state.apply_move(candidate_move)
        opponent_best_result = best_result(
            next_state, max_depth -1, eval_fn)
        our_result = -1 * opponent_best_result 
        if our_result > best_so_far:
            best_so_far = our_result
    return best_so_far
#----------------------------------------------------------






#---------------------------------------------------------------


#prunes game tree with depth recution on tree search algorithm and position evaluation
def find_winning_move(game_state, next_player):
    "in a particular scenario check legal moves for winning and return that move"
    for candidate_move in game_state.legal_moves(next_player):
        next_state = game_state.apply_move(candidate_move)
        #
        #
        #
        # .winner is not created yet
        if next_state.is_over() and next_state.winner == next_player:
            return candidate_move
        return None

def eliminate_losing_moves(game_state. next_player):
    "calls find_winning_move"
    opponent = next_player.other()
    possible_moves = []
    for candidate_move in game_state.legal_moves(next_player):
        next_state = game_state.apply_move(candidate_move)
        opponent_winning_move = find_winning_move(next_state, opponent)
        if opponent_winning_move is None:
            possible_moves.append(candidate_move)
    return possible_moves


def find_two_step_win(game_state, next_player):
    "calls elmininate_losing moves"
    opponent = next_player.other()
    #
    #
    #
    # legal _moves doesnt have a parameter, and probably doesnt need one
    for candidate_move in game_state.legal_moves(next_player)
        next_state = game_state.apply_move(candidate_move)
        good_responses = eliminating_losing_moves(next_state, opponent)
        if not good_responses:
            return candidate_move
        return None
#---------------------------------------------------------------


