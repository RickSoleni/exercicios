import random


class Armor:
    """Classe para definir armor."""

    def __init__(
        self,
        name: str,
        lvl: int,
        voc: str,
        slots: int,
        arm: int,
        bonus: dict,
        protection: dict,
        weight: float,
    ):
        self.name = name
        self.lvl = lvl
        self.voc = voc
        self.slots = slots
        self.arm = arm
        self.bonus = bonus
        self.protection = protection
        self.weight = weight


focus_cape = Armor(
    'Focus Cape', 0, 'Sorcerers & Druids', 0, 9, {'Magic Level': +1}, 0, 21.0
)


class Creature:
    """Classe para definir criatura"""

    def __init__(
        self,
        name: str,
        level: int,
        hpatual: int,
        hpmax: int,
        exp: int,
        speed: int,
        armor: int,
        charms: int,
        abilities: dict,
        loot: dict,
    ):
        self.name = name
        self.level = level
        self.hpatual = hpatual
        self.hpmax = hpmax
        self.exp = exp
        self.speed = speed
        self.armor = armor
        self.charms = charms
        self.abilities = abilities
        self.loot = loot

    def __str__(self) -> str:
        return f'The creature is a {self.name}, its have a {self.hp} hitpoints'

    def __gt__(self, player) -> bool:
        return self.level > player.level

    def __lt__(self, player) -> bool:
        return self.level < player.level


dragon = Creature(
    'Dragon',
    120,
    160,
    600,
    700,
    86,
    25,
    25,
    {'Phisical Damage': 300, 'Fire Wave': 200},
    {
        'Gold Coins': 12,
        'Dragon Ham': 3,
        'Crossbow': 1,
        'Steel Shield': 1,
        'Burst Arrows': 12,
        'Dragons Tail': 1,
        'Longsword': 1,
        'Broadsword': 1,
        'Steel Helmet': 1,
        'Plate Legs': 1,
        'Strong Health Potion': 2,
        'Wand of Inferno': 1,
        'Serpent Sword': 1,
        'Dragonbone Staff': 1,
        'Life Crystal': 1,
    },
)


class Vocation:
    def __init__(
        self,
        name: str,
        hpgain: int,
        managain: int,
        weightgain: float,
        spells: dict,
    ):
        self.name = name
        self.hpgain = hpgain
        self.managain = managain
        self.weightgain = weightgain
        self.spells = spells


class Player:
    """Class for players definitions, attributes and methods."""

    def __init__(
        self,
        nickname: str,
        vocation: str,
        level: int,
        hpatual: int,
        hpmax: int,
        defense: int,
        skill_sword: int,
        skill_axe: int,
        skill_club: int,
        magic_level: int,
        skill_fishing: int,
        skill_fist: int,
    ):
        self.nickname = nickname
        self.vocation = vocation
        self.level = level
        self.hpatual = hpatual
        self.hpmax = hpmax
        self.defense = defense
        self.skill_sword = skill_sword
        self.skill_axe = skill_axe
        self.skill_club = skill_club
        self.magic_level = magic_level
        self.skill_fishing = skill_fishing
        self.skill_fist = skill_fist

    def __str__(self) -> str:
        return f'{self.name}, Level {self.level}, Their a {self.vocation}'

    def __gt__(self, criatura) -> bool:
        return self.level > criatura.level

    def __lt__(self, criatura) -> bool:
        return self.level < criatura.level


Rick = Player('RickSoleni', 'Knight', 150, 455, 2000, 102, 103, 0, 0, 9, 0, 25)

paladin = Vocation(
    'Paladin',
    10,
    20,
    15.00,
    {
        'exevo infir con': 'Arrow Call',
        'exana ina': 'Cancel Invisibility',
        'exevo con': 'Conjure Arrow',
        'exevo con flam': 'Conjure Explosive Arrow',
        'exana mort': 'Cure Curse',
        'exana pox': 'Cure Poison',
        'exevo mas san': 'Divine Caldera',
        'exana amp res': 'Divine Dazzle',
        'exura san': 'Divine Healing',
        'exori san': 'Divine Missile',
        'exeta con': 'Enchant Spear',
        'exori con': 'Ethereal Spear',
        'exiva moe res': 'Find Fiend',
        'exiva"name"': 'Find Person',
        'utevo gran lux': 'Great Light',
        'utani hur': 'Haste',
        'utori san': 'Holy Flash',
        'exura gran': 'Intense Healing',
        'utura gran': 'Intense Recovery',
        'exani hur up/down': 'Levitate',
        'utevo lux': 'Light',
        'exura': 'Light Healing',
        'exura infir': 'Magic Patch',
        'exani tera': 'Magic Hope',
        'utamo mas sio': 'Protect Party',
        'utura': 'Recovery',
        'exura gran san': 'Salvation',
        'utito tempo san': 'Sharpshooter',
        'exori gran con': 'Strong Ethereal Spear',
        'utevo gran res sac': 'Summon Paladin Familiar',
        'utamo tempo san': 'Swift Foot',
        'adito grav': 'Destroy Field Rune',
        'adiro tera': 'Desintegrate Rune',
        'adori san': 'Holy Missile Rune',
    },
)


def death_message_player():
    print(
        """Alas! Brave adventurer, you have met a sad fate.
But do not despair, for the gods will bring you back
into the world in exchange for a small sacrifice.\n
Simply click on "Ok" to resume your jorneys in Tibia."""
    )


"""loots
1 - comum
2 - incomum
3 - semi raro
4 - raro
5 - muito raro
"""


def death_message_creature(criatura):
    drop = dict()
    numero_loot = random.randint(0, len(criatura.loot))
    if numero_loot == 0:
        drop['Loot'] = 'Vazio'
    else:
        for _ in range(numero_loot):
            item, quant = random.choice(list(criatura.loot.items()))
            drop[item] = quant
    print(
        f'You slain a {criatura.name}.\n'
        f'You have gained a {criatura.exp} experience.\n'
        f'Loot of {criatura.name}: {drop.items()}'
    )


def atacar_criatura(creature: Creature, player: Player):
    player_attack = player.skill_sword - creature.armor
    creature.hpatual = creature.hpatual - player_attack
    print(f'You deal {player_attack} to a {creature.name}')
    return creature.hpatual


def atacar_player(creature: Creature, player: Player):
    creat_atk = (
        creature.abilities[random.choice(list(creature.abilities.keys()))]
        - player.defense
    )
    player.hpatual = player.hpatual - creat_atk
    print(f'You lose {creat_atk} hitpoints to an attack by a {creature.name}')
    return player.hpatual


def first_encounter(creature, player):
    creature.hpatual = creature.hpmax
    player.hpatual = player.hpmax
    return creature.hpatual, player.hpatual


first_encounter(dragon, Rick)

while Rick.hpatual > 0:
    atacar_criatura(dragon, Rick)
    if dragon.hpatual <= 0:
        death_message_creature(dragon)
        break
    atacar_player(dragon, Rick)
    if Rick.hpatual <= 0:
        death_message_player()
        break

teste = Rick < dragon

print(teste)
