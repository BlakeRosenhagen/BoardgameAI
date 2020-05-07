import enum

class Player(enum.Enum):
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white


from collections import namedtuple
#  namedtuple allow for for point.row instead of point[0]
class Point(namedtuple('Point', 'row col')):
    def neighbors(self):
        "returns position of neighboring points"
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1),
        ]


#players, on their turn can play, pass, or resign
# move (play, pass, resign)

class Move():
    def __init__(self, point=None, is_pass=False, is_resign=False):
        assert (point is not None) ^ is_pass ^ is_resign
        self.point = point
        self.is_play = (self.point is not None)
        self.is_pass = is_pass
        self.is_resign = is_resign

    #the reason why these functions are here is to be able to return a boolean for
    #future "if" statements
    @classmethod #cant alter object instance state
    def play(cls,point):
        return Move(point=point)

    @classmethod 
    def pass_turn(cls):
        return Move(is_pass=True)
    
    @classmethod
    def resign(cls):
        return Move(is_resign=True)


#must check if any neighbors have liberties left, and whether the neighbor's neighbor's have liberties left etc.

#viewing stone individually can be computationally overwhelming
#keeping track of groups of stones of the same color with their liberties is more effective