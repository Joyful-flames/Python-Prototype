# Brisbane Plants

# All Plant Type
foliicolous_lichens = {
    'name': 'Foliicolous',
    'type': 'Lichens',
    'tier': 0,
    'terran': (),
    'crowed_range': 2,
    'spread_range': 2,
    'mature_stage': 0,
    'mature_percentage': 80,
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
    'tier': 1,
    'terran': (),
    'crowed_range': 2,
    'spread_range': 2,
    'mature_stage': 1,
    'mature_percentage': 80,
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
    'tier': 2,
    'terran': (),
    'crowed_range': 1,
    'spread_range': 1,
    'mature_stage': 2,
    'mature_percentage': 80,
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
