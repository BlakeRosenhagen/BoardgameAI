# tag::enumimport[]

import enum

# end::enumimport[]

# tag::namedtuple[]

from collections import namedtuple

# end::namedtuple[]

__all__ = [

    'Player',

    'Point',

]



# tag::color[]

class Player(enum.Enum):
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white

# end::color[]





# tag::points[]

class Point(namedtuple('Point', 'row col')):

    def neighbors(self):

        return [

            Point(self.row - 1, self.col),

            Point(self.row + 1, self.col),

            Point(self.row, self.col - 1),

            Point(self.row, self.col + 1),

        ]

# end::points[]



    def __deepcopy__(self, memodict={}):

        # These are very immutable.

        return self



class Move():  # <1>

    def __init__(self, point=None, is_pass=False, is_resign=False):

        assert (point is not None) ^ is_pass ^ is_resign

        self.point = point

        self.is_play = (self.point is not None)

        self.is_pass = is_pass

        self.is_resign = is_resign



    @classmethod
    def play(cls, point):  # <2>

        return Move(point=point)



    @classmethod
    def pass_turn(cls):  # <3>

        return Move(is_pass=True)



    @classmethod
    def resign(cls):  # <4>

        return Move(is_resign=True)