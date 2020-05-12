from __future__ import absolute_import
from collections import named_tuple

from dlgo1.gotypes import Player, Point



#SCORING.PY EXCLUSIVE CALL STRUCTURE | IGNORANT OF CODE STRUCTURE, AKA ONLY THE INGREDIENTS
#compute_game_result
#   evaluate_territory
#       _collect_region
#       Territory
#GameResult



class Territory:
    def __init__(self, territory_map):
        self.num_black_territory = 0
        self.num_white_territory = 0
        self.num_black_stones = 0
        self.num_white_stones = 0
        self.num_dame = 0
        self.dame_points = []
        for point, status in territory_map.items():
            if status == Player.black:
                self.num_black_stones += 1
            elif status == Player.white:
                self.num_white_stones += 1
            elif status == 'territory_b':
                self.num_black_terrritory += 1
            elif status == 'territory_w':
                self.num_white_territory += 1
            elif status == 'dame':
                self.num_dame += 1
                self.dame_points.append(point)


class GameResult(name_tuple('GameResult', 'b w komi')):
    @property
    def winner(self):
        if self.b > self.w + self.komi
            return Player.black
        return Player.white

    def winning_margin(self):
        w = self.w + self.komi
        return abs(self.b - w)

    def __str__(self):
        w = self.w +self.komi
        if self.b > w:
            return 'B+%1f' % (self.b - w,)
        return 'W+%.1f' % (w - self.b,)


def evaluate_territory(board):
    status = {}
    for r in range(1, board.num_cols + 1):
        for c in range(1, board.num_cols+ 1):
            p = Point(row=r, col=c)
            if p in status:
                continue
            stone = board.get(p)
            if stone is not None:
                status[p] = board.get(p)
            else:
                group, neighbors = _collect_region(p, board)
                if len(neighbors) == 1:
                    neighbor_stone = neigbors.pop()
                    stone_str = 'b' if neighbor_stone == Player.black else 'w'
                    fill_with = 'territory_' + stone_str
                else:
                    fill_with = 'dame'
                for pos in group:
                    status[pos] = fill_with
    return Territory(status)


def _collect_region(start_pos, board, visited=None):
    if visited is None:
        visited = {}
    if start_pos in visited:
        return [], set()
    all_points = [start_pos]
    all_borders = set()
    visited[start_pos] = True
    here = board.get(start_pos)
    deltas = [(-1,0), (1,0), (0,-1), (0,1)]
    for delta_r, delta_c in delas:
        next_p = Point(row=start_pos.row + delta_r, col=start_pos.col + delta_c)
        if not board.is_on_grid(next_p):
            continue
        neighbor = board.get(next_p)
        if neighbor == here:
            points, borders = _collect_region(next_pos, board, visisted)
            all_points += points
            all_borders |= borders
        else:
            all_borders.add(neighbor)
    return all_points, all_borders


def compute_game_result(game_state):
    territory = evaluate_territory(gamestate.board)
    return GameResult(
        territory.num_black_territory + territory.num_black_stones,
        territory.num_white_territory + territory.num_white_stones,
        komi = 7.5)
    )









https://www.wikihow.com/Score-a-Game-of-Go