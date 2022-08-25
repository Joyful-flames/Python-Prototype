import random

from Configration import *
from data.DataType import *


class Plant(object):

    def __init__(self, plant_type: dict, position: Position, stage=0, stage_percentage=0):

        # init plant dict
        self.plant_type = plant_type

        # init position
        self.position = position
        self.colum, self.row = position

        # init plant property
        self.tier = plant_type['tier']
        self.name = plant_type['name']
        self.type_name = plant_type['type']
        self.grow_rate = plant_type['grow_rate']
        self.max_density = plant_type['max_density']
        self.spread_range = plant_type['spread_range']
        self.crowed_range = plant_type['crowed_range']

        # init grow status
        self.stage = stage
        self.stage_percentage = stage_percentage

    def delta_evolution(self, plant_tree: list[dict], delta_tier: int, board: Board) -> Board:
        """ update plant.position() on board with a last or next tier plant.

        :param: delta_tier:
        :param: plant_tree: the list of available plan in current game level.
        :param: board: current game board.
        :return: Board with updated plant, or no change if there is no available plant in current game level.
        """
        for item in plant_tree:
            if item['tier'] == self.tier + delta_tier:
                board[self.colum][self.row] = Plant(item, self.position)
        return board

    def spread(self, positions: list, board: Board) -> Board:
        """

        :param positions:
        :param board:
        :return:
        """
        if positions != []:
            colum, row = list(random.choice(positions))

            colum: int
            row: int

            board[colum][row] = Plant(self.plant_type, (colum, row))
        return board

    def grow(self) -> None:
        self.stage_percentage += self.grow_rate * grow_speed_multiplier

    def delta_stage(self) -> None:

        if self.stage_percentage > 99:

            # stage + 1 and reset stage_percentage
            if self.stage < self.tier:

                self.stage += 1
                self.stage_percentage = 0

            # Cap stage_percentage at 99
            else:
                self.stage_percentage = 99

    def is_crowded(self, ratio) -> bool:
        return self.max_density < ratio

    def is_mature(self) -> bool:
        return (self.stage == self.plant_type['mature_stage']) and (
                    self.stage_percentage > self.plant_type['mature_percentage'])

    def frame_logic(self, board: Board, location: list) -> Board:

        self.grow()
        self.delta_stage()

        final_spread_range = self.spread_range * spead_multiplier

        # get intractable range
        ob_start_colum, ob_start_row = [self.colum - final_spread_range, self.row - final_spread_range]
        ob_end_colum, ob_end_row = [self.colum + final_spread_range, self.row + final_spread_range]

        # keep intractable range in boundary
        colum_limit, row_limit = (len(board) - 1, len(board[0]) - 1)

        if ob_start_colum < 0:
            start_colum = 0
        else:
            start_colum = ob_start_colum

        if ob_start_row < 0:
            start_row = 0
        else:
            start_row = ob_start_row

        if ob_end_colum > colum_limit:
            end_colum = colum_limit
        else:
            end_colum = ob_end_colum

        if ob_end_row > row_limit:
            end_row = row_limit
        else:
            end_row = ob_end_row

        # assign lists to store positions within interaction range
        empty_cell = []
        lowertier_cell = []
        eqtier_cell = []
        uppertier_cell = []

        # append position to lists
        for colum_index in range(start_colum, end_colum + 1):
            for row_index in range(start_row, end_row + 1):
                current_cell = board[colum_index][row_index]

                if type(current_cell) is Plant:
                    current_cell: Plant

                    if current_cell.tier < self.tier:
                        lowertier_cell.append((colum_index, row_index))

                    elif current_cell.tier == self.tier:
                        eqtier_cell.append((colum_index, row_index))

                    else:
                        uppertier_cell.append((colum_index, row_index))

                elif current_cell is None:
                    empty_cell.append((colum_index, row_index))

        # environmental determination
        # determent is plant crowded
        out_intractable_cell_count = (ob_end_colum - ob_start_colum + 1) * (ob_end_row - ob_start_row + 1)
        in_intractable_cell_count = (end_colum - start_colum + 1) * (end_row - start_row + 1)
        outside_cell_count = out_intractable_cell_count - in_intractable_cell_count

        region_density = (len(uppertier_cell + eqtier_cell) + outside_cell_count + 1) / in_intractable_cell_count

        action_devolution = False
        action_evolution = False
        action_spread = False

        if debug_mode and self.tier > 0:
            print('Name:{} Type:{} Status:{}-{}% '.format(self.name,
                                                          self.type_name,
                                                          self.stage,
                                                          self.stage_percentage, ), end='')

        if self.is_mature():
            if self.is_crowded(region_density) and random.randrange(100) < remove_chance:
                action_devolution = True

            elif empty_cell + lowertier_cell != [] and (not self.is_crowded(region_density)):
                action_spread = True

            elif len(eqtier_cell) == (end_colum - start_colum + 1) * (end_row - start_row + 1):
                action_evolution = True

        if debug_mode and self.tier > 0:
            print_str = ' Density:{}/{} Crowed:{} | Devolution:{} Spread:{} Evolution:{} | {}/{}'.format(
                region_density,
                self.max_density,
                self.is_crowded(region_density),
                action_devolution,
                action_spread,
                action_evolution,
                (len(uppertier_cell + eqtier_cell) + outside_cell_count + 1),
                (end_colum - start_colum + 1) * (end_row - start_row + 1))
            print(print_str)

        if action_devolution:
            return self.delta_evolution(location, -1, board)

        elif action_spread:
            return self.spread(empty_cell + lowertier_cell, board)

        elif action_evolution:
            return self.delta_evolution(location, 1, board)

        return board
