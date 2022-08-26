import random
import time

import matplotlib.pyplot as plt

from Board import blank_board, tier_board, biomass_board, board_sum_biomass
from Plant import Plant
from PrintTools import print_species_count
from Configration import *
from data.DataType import *
from data.Location import *


def auto_test(board: Board, available_plants: list[dict], sum_biomass: int, plant_counter: list) -> Board:

    target_colum = random.randrange(0, len(board))
    target_row = random.randrange(0, len(board[0]))

    if sum_biomass > (map_size * map_size * 1100) and (plant_counter[2] < 5):
        board[target_colum][target_row] = Plant(available_plants[2], (target_colum, target_row))
        print(board[target_colum][target_row].__str__(), 'Dropped')
        plant_counter[2] += 1

    elif sum_biomass > (map_size * map_size * 180) and plant_counter[1] < 5:
        board[target_colum][target_row] = Plant(available_plants[1], (target_colum, target_row))
        print(board[target_colum][target_row].__str__(), 'Dropped')
        plant_counter[1] += 1

    elif plant_counter[0] < 5:
        board[target_colum][target_row] = Plant(available_plants[0], (target_colum, target_row))
        print(board[target_colum][target_row].__str__(), 'Dropped')
        plant_counter[0] += 1

    return board


def console_plt_interaction(board: Board, available_plants, sum_biomass, iteration) -> Board:
    if input_sim_mode:
        print('Iteration:', iteration, 'Biomass:', sum_biomass, ' Available: ', end='')
        for item in available_plants:
            print(item['type'], ' ', end='')
        user_input = input('\nEnter x,y,tier to insert a plant:\n')

        try:
            user_input = user_input.split(' ')
            insert_pos = int(user_input[1]), int(user_input[0])

            for item in available_plants:
                if item['tier'] == int(user_input[2]):
                    insert_plant = Plant(item, insert_pos)
                    board[insert_pos[0]][insert_pos[1]] = insert_plant
                    print(insert_plant.__str__())
                else:
                    print('Tier error')
        except:
            print('Input error')
    return board


def frame_logic(board: Board, available_plants: list[dict]):
    for index in range(len(board)):
        for cell in board[index]:
            if type(cell) is Plant:
                cell: Plant

                board = cell.frame_logic(board, available_plants)


def game_logic() -> None:
    iteration = 0
    total_time = 0
    board = blank_board(map_size, map_size)

    available_plants = [brisbane[0]]

    plant_counter = [0, 0, 0]

    # half_size = round(len(board) / 2)
    # board[half_size][half_size] = Plant(foliicolous_lichens, (half_size, half_size))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    im = ax.imshow(biomass_board(board), cmap='YlGn', vmin=0, vmax=255)
    plt.show(block=False)

    while True:

        start_time = time.time()

        frame_logic(board, available_plants)

        total_biomass = board_sum_biomass(board)

        location_tier = 0

        # Unlock new plant
        if total_biomass > (map_size * map_size * 1000):
            location_tier = 2

        elif total_biomass > (map_size * map_size * 160):
            location_tier = 1

        available_plants = brisbane[:location_tier + 1]

        end_time = time.time()

        total_time += (end_time - start_time)

        if console_log:
            print_species_count(board,available_plants)
            print('Iteration:', iteration, 'Time:', (end_time - start_time))

        # user input
        if iteration % 10 == 0 and iteration > 0:
            if input_sim_mode:
                console_plt_interaction(board, available_plants, total_biomass, iteration)
            else:
                auto_test(board, available_plants, total_biomass, plant_counter)

        try:
            # update board to heatmap
            im.set_array(tier_board(board))

            # redraw the figure
            fig.canvas.draw()
            fig.canvas.flush_events()


        except:
            print(total_time)
            quit()

        iteration += 1


game_logic()
