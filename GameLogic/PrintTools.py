from data.DataType import *
from Plant import Plant
from Board import count_plant


def read_board(board: Board) -> None:
    for index in range(len(board)):
        print('|', end='')
        for item in board[index]:
            if type(item) is Plant:
                print(item.plant_type['type'][0], end='|')
            else:
                print(" |", end='')
        print()


def print_board(board: Board) -> None:
    """

    Parameters:
        board:

    Returns:

    """
    p_board = []
    for index in range(len(board)):
        for item in board[index]:
            if type(item) is Plant:
                if item.get_grow < 10:
                    print_str = str(item.get_grow) + '% ' + item.plant_type['type'][0] + item.str_stage()
                    p_board.append(print_str)
                else:
                    print_str = str(item.get_grow) + '%' + item.plant_type['type'][0] + item.str_stage()
                    p_board.append(print_str)
            else:
                p_board.append('     ')

        print(p_board, end=' ')
        p_board = []
        print()
    print('------------------------------------------------------------------------------------------')


def print_species_count(board: Board, plant_list) -> None:
    for item in count_plant(board, plant_list):
        print('{}:{}'.format(item[0],[item[1]]), end='')
    print()