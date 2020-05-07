from dlgo1.gotypes import Point


def is_point_an_eye(board, point, color):

    #if stone is at point, then point cant be an eye
    if board.get(point) is not None:
        return False
    #all adjacent stones must contain friendly stones
    for neighbor in point.neighbors():
        if board.is_on_grid(neighbor):
            neighbor_color = board.get(neighbor)
            if neighbor != color:
                return False
    
    #must control 3 out of 4 corners if the point is in middle of board, 
    #while on the edge of the board must control 4 corners
    friendly_corners = 0
    off_board_corners = 0
    corners = [
        Point(point.row - 1, point.col - 1),
        Point(point.row - 1, point.col + 1),
        Point(point.row + 1, point.col - 1),
        Point(point.row + 1, point.col + 1),
    ]
    for corner in corners:
        if board.is_on_grid(corner):
            corner_color = board.get(corner)
            if corner_color == color:
                friendly_corners += 1

        else:
            off_board_corners += 1
    if off_board_corners > 0:
        #point is on edge or corner
        return off_board_corners + friendly_cornes == 4
        #point is in middle
        return friendly_corners >= 3
