from Plant import Plant
from data.DataType import *


def blank_board(colum: int, row: int) -> Board:
    board = []
    for index_colum in range(colum):
        board.append([])
        for index_row in range(row):
            board[index_colum].append(None)
    return board


def pos_to_block(position: tuple[int, int], extend: int, board: Board):
    """extend position in to block

        Parameters:
            position: the given position indicating start get_row and column of the block
            extend: the given int indicating range to extend
            board: the given board containing list of lists

        Returns:
            block without go out board's boundary
        """
    center_colum, center_row = position
    position_start = [center_colum - extend, center_row - extend]
    position_end = [center_colum + extend, center_row + extend]

    colum_limit, row_limit = (len(board) - 1, len(board[0]) - 1)
    if position_start[0] < 0:
        position_start[0] = 0

    if position_start[1] < 0:
        position_start[1] = 0

    if position_end[0] > colum_limit:
        position_end[0] = colum_limit

    if position_end[1] > row_limit:
        position_end[1] = row_limit

    return tuple(position_start), tuple(position_end)


def board_sum_biomass(board: Board):
    score = 0
    for index in range(len(board)):
        for cell in board[index]:
            score += cell.mass()
    return score


def biomass_board(board: Board) -> Board:
    new_board = []
    for colum in range(len(board)):
        new_board.append([])
        for row in range(len(board[colum])):
            if type(board[colum][row]) is Plant:
                new_board[colum].append(board[colum][row].mass())
            else:
                new_board[colum].append(0)
    return new_board


def tier_board(board: Board, color_index = 100) -> Board:
    tier_map = []
    for colum in range(len(board)):
        tier_map.append([])
        for row in range(len(board[colum])):
            current_cell = board[colum][row]
            if type(current_cell) is Plant:
                current_cell: Plant
                tier_map[colum].append((current_cell.tier + 1) * color_index)
            else:
                tier_map[colum].append(0)
    return tier_map
