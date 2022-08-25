import time

import matplotlib.pyplot as plt

from Board import blank_board, tier_board
from Plant import Plant
from Configration import *
from data.DataType import *
from data.Location import *

def frame_logic(board: Board):
    for index in range(len(board)):
        for cell in board[index]:
            if type(cell) is Plant:
                cell: Plant

                board = cell.frame_logic(board, brisbane)


def game_logic() -> None:
    iteration = 0
    total_time = 0
    board = blank_board(50, 50)

    half_size = round(len(board) / 2)
    board[half_size][half_size] = Plant(foliicolous_lichens, (half_size, half_size))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    im = ax.imshow(tier_board(board), cmap='YlGn', vmin=0, vmax=255)
    plt.show(block=False)

    while True:

        start_time = time.time()

        frame_logic(board)

        end_time = time.time()

        total_time += (end_time - start_time)

        if debug_mode:
            print('Iteration:', iteration)

        try:

            # update board to heatmap
            im.set_array(tier_board(board))

            # redraw the figure
            fig.canvas.draw()
            fig.canvas.flush_events()

            time.sleep(0.1)

        except:
            print(total_time)
            quit()

        iteration += 1

game_logic()
