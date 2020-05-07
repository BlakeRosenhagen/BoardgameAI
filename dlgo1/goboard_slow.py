import copy
import numpy as np
from dlgo1.gotypes import Point
from dlgo1.gotypes import Player

class GoString():
    "Groups of stones"
    def __init__(self, color, stones, liberties):
        self.color = color
        self.stones = set(stones)
        self.liberties = set(liberties)
    
    def remove_liberty(self, point):
        self.liberties.remove(point)
    
    def add_libery(self,point):
        self.liberties.add(point)
    
    def merged_with(self, go_string):
        "called when player connects two of its groups by placing a stone"
        assert go_string.color == self.color
        combined_stones = self.stones | go_string.stones
        return GoString(
            self.color,
            combined_stones,
            (self.liberties | go_string.liberties) - combined_stones)
            

    @property
    def num_liberties(self):
        return len(self.liberties)
    
    def __eq__(self, other):
        return isinstance(other, GoString) and \
            self.color == other.color and \
            self.stones == other.stones and \
            self.liberties == other.liberties


class Board():
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}
        
    def get_grid_value(self, input):
        try:
            return self._grid[input] 
        except:
            return None

    def is_on_grid(self, point):
        "returns boolean on whether point is within board bounds"
        return 1 <= point.row <= self.num_rows and \
            1 <= point.col <= self.num_cols


    def get(self, point):
        string = self._grid.get(point)
        if string is None:
            return None
        # getting the color of the point retrieved from the _grid, mabie...
        return string.color

    def get_go_string(self, point):
        string = self._grid.get(point)
        if string is None:
            return None
        return string

    def _remove_string(self, string):
        """Black can capture a white stone, thereby regaining a liberty 
        for each of the Go strings adjacent to the captured stone."""
        for point in string.stones:
            for neighbor in point.neighbors():
                neighbor_string = self._grid.get(neighbor)
                if neighbor_string is None:
                    continue
                if neighbor_string is not string:
                    neighbor_string.add_liberty(point)
            self._grid[point] = None


    def place_stone(self, player, point):
        #check whether the piece is placed within bounds of game board
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None #used to be _grid.get(point)
        adjacent_same_color = []
        adjacent_opposite_color = []
        liberties = []
        for neighbor in point.neighbors(): # each of the four points around a particular point
            if not self.is_on_grid(neighbor):
                continue
            neighbor_string = self._grid.get(neighbor) #used to be _grid.get(neighbor)
            if neighbor_string is None: # each of the four points around a particular point
                liberties.append(neighbor)
            elif neighbor_string.color == player:
                if neighbor_string not in adjacent_same_color:
                    adjacent_same_color.append(neighbor_string)
            else:
                if neighbor_string not in adjacent_opposite_color:
                    adjacent_opposite_color.append(neighbor_string)
        new_string = GoString(player, [point], liberties)
        for same_color_string in adjacent_same_color:
            new_string = new_string.merged_with(same_color_string)
        for new_string_point in new_string.stones:
            self._grid[new_string_point] = new_string
        for other_color_string in adjacent_opposite_color:
            other_color_string.remove_liberty(point)
        for other_color_string in adjacent_opposite_color:
            if other_color_string.numliberties == 0:
                self._remove_string(other_color_string)

#placing stones steps: 
# 1.merge adjacent strings of same color.
# 2.reduce liverties of any adjacent strings of opposite color.
# 3.if any opposite color strings now have zero liberties, remove them.


class GameState():
    "core functioning part of game, plus certain gameplay rules go here"
    def __init__(self, board, next_player, previous, move):
        self.board = board
        self.next_player = next_player
        self.previous_state = previous
        self.last_move = move

    def apply_move(self, move):
        """returns new GameState after applying the move"""
        if move.is_play:
            next_board = copy.deepcopy(self.board)
            next_board.place_stone(self.next_player, move.point)
        else:
            next_board = self.board
        return GameState(next_board, self.next_player, self, move)
    
    @classmethod
    def new_game(cls, board_size):
        if isinstance(board_size, int):
            board_size = (board_size, board_size)
        board = Board(*board_size)
        return GameState(board, Player.black, None, None)
    
    def is_over(self):
        if self.last_move is None:
            return False
        if self.last_move.is_resign:
            return True
        second_last_move = self.previous_state.last_move
        if second_last_move is None:
            return False
        return self.last_move.is_pass and second_last_move
    
# confirm that point you want to place stone is empty
# check that move isn't self-capture
#confirm that move doesnt violate "ko" rule

#make rule to where when a GoString has only one liberty, the owner of that 
#string is not allowed to play there since that would be a self capture. Unless
#the player can capture enemy stones during that play.

    def is_move_self_capture(self, player, move):
        if not move.is_play:
            return False
        next_board = copy.deepcopy(self.board)
        next_board.place_stone(player, move.point)
        new_string = next_board.get_go_string(move.point)
        return new_string.num_liberties == 0
    
#player should not be able to play a move if that move would create a GameState
#identical to the previous GameState

    @property
    def situation(self):
        return (self.next_player, self.board)

    def does_move_violate_ko(self, player, move):
        if not move.is_play:
            return False
        next_board = copy.deepcopy(self.board)
        next_board.place_stone(player, move.point)
        next_situation = (player.other, next_board)
        past_state = self.previous_state
        while past_state is not None:
            if past_state.situation == next_situation:
                return True
            past_state = past_state.previous_state
        return False

    def is_valid_move(self, move):
        if self.is_over():
            return False
        if move.is_pass or move.is_resign:
            return True
        return(
            #point must be empty
            self.board.get(move.point) is None and
            #move doesn't capture own stone
            not self.is_move_self_capture(self.next_player, move) and
            #move doesn't violate ko
            not self.does_move_violate_ko(self.next_player, move))
    

# if we're not careful then the AI will continue playing legal moves as 
# long as they exist, which will make the AI fill up its own liberties 
# which will waste stones and strategic ground

#hueristics to ensure the AI plays the game in a "humanlike way"
#dont play a stone in an area where friendly stones surround
#dont play a stone that would have only one liberty 
#always capture enemy stone that has one liberty       