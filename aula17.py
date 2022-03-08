import random

loot = {
    'items': {
        'Gold Coin': 12,
        'Dragon Ham': 3,
        'Burst Arrow': 12,
        'Steel Shield': 1,
        'Crossbow': 1,
        'Dragons Tail': 2,
        'Longsword': 1,
        'Broadsword': 1,
        'Steel Helmet': 1,
        'Plate Legs': 1,
        'Strong Health Potion': 1,
        'Wand of Inferno': 1,
        'Serpent Sword': 1,
        'Dragonbone Staff': 1,
        'Life Crystal': 1,
    },
    'raridades': {
        'comum': {
            'loots': ['Gold Coin', 'Dragon Ham', 'Burst Arrow'],
            'percentage': 0.8,
        },  # 80%
        'incomum': {
            'loots': [
                'Steel Shield',
                'Crossbow',
                'Dragons Tail',
                'Broadsword',
            ],
            'percentage': 0.4,
        },  # 40%
        'semi-raro': {
            'loots': ['Steel Helmet', 'Plate Legs', 'Strong Health Potion'],
            'percentage': 0.3,
        },  # 30%
        'raro': {
            'loots': ['Wand of Inferno', 'Serpent Sword'],
            'percentage': 0.1,
        },  # 10%
        'muito-raro': {
            'loots': ['Dragonbone Staff', 'Life Crystal'],
            'percentage': 0.01,
        },  # 1%
    },
}


def random_drops(monster_loot):
    drops = []

    for raridade in monster_loot['raridades']:
        for item in monster_loot['raridades'][raridade]['loots']:
            if (
                random.random()
                <= monster_loot['raridades'][raridade]['percentage']
            ):
                item_qty = random.randint(1, loot['items'][item])
                drops.append((item, item_qty))
    return drops


drops_do_dragao = random_drops(loot)

print(drops_do_dragao)
