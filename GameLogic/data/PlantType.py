speed_multiplier = 1
spead_multiplier = 1
remove_multiplier = 1 # %

# All Plant Type
foliicolous_lichens = {
    'name': 'Foliicolous',
    'type': 'Lichens',
    'level': 0,
    'terran': (),
    'spread_range': 2,
    'grow_rate': 30,
    'max_density': 1.0,
    'bio_mass': 1,
    'stage_condition': {
        0: {'hardness': (0, 10),
            'humidity': (0, 100)},
    },
}

adiantum_hispidulum = {
    'name': 'Maidenhair Fern',
    'type': 'Fern',
    'level': 1,
    'terran': (),
    'seed_range': 2,
    'grow_rate': 10,
    'max_density': 0.9,
    'bio_mass': 10,
    'stage_condition': {
        0: {'hardness': (0, 10),
            'humidity': (0, 100)},
        1: {'hardness': (0, 10),
            'humidity': (0, 100)}
    }
}

eucalyptus_tereticornis = {
    'name': 'Forest red gum',
    'type': 'Wood',
    'level': 2,
    'terran': (),
    'seed_range': 1,
    'grow_rate': 1,
    'max_density': 0.3,
    'bio_mass': 70,
    'stage_condition': {
        0: {'hardness': (0, 10),
            'humidity': (0, 100)},
        1: {'hardness': (0, 10),
            'humidity': (0, 100)},
        2: {'hardness': (0, 10),
            'humidity': (0, 100)}
    }
}

brisbane = [foliicolous_lichens, adiantum_hispidulum, eucalyptus_tereticornis]
