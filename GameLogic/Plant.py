from data.DataType import *

class Plant(object):

    def __init__(self, plant_type: dict, position: Position, stage = 0, stage_percentage = 0):
        self.plant_type = plant_type
        self.tier = plant_type['tier']
        self.name = plant_type['name']
        self.grow_rate = plant_type['grow_rate']