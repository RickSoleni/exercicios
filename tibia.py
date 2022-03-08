from fastapi import FastAPI
from aula12 import dragon, paladin

tibia = FastAPI()


@tibia.get('/creature/dragon')
async def get_creature():
    return {
        'name': dragon.name,
        'level': dragon.level,
        'current_hp': dragon.hpatual,
        'max_hp': dragon.hpmax,
        'experience': dragon.exp,
        'speed': dragon.speed,
        'armor': dragon.armor,
        'charms': dragon.charms,
        'abilities': dragon.abilities,
        'loot': dragon.loot,
    }


@tibia.get('/vocation/paladin/spells')
async def get_vocation():
    return paladin.spells
