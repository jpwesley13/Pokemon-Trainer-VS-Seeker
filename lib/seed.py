#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.pokemon import Pokemon
from models.trainer import Trainer

def seed_vs_seeker():
    Pokemon.drop_table()
    Trainer.drop_table()
    Trainer.create_table()
    Pokemon.create_table()

    trainer_1 = Trainer.create("Lt. Surge", "Vermilion City", 3)
    trainer_2 = Trainer.create("Misty", "Cerulean City", 2)
    trainer_3 = Trainer.create("Blaine", "Cinnabar Island", 7)
    trainer_4 = Trainer.create("Blue", "Pallet Town", 8)
    Pokemon.create("Volty", "Pikachu", 18, trainer_1.id)
    Pokemon.create("Orbot", "Voltorb", 21, trainer_1.id)
    Pokemon.create("Raiden", "Raichu", 24, trainer_1.id)
    Pokemon.create("Stars", "Staryu", 18, trainer_2.id)
    Pokemon.create("Stripes", "Starmie", 21, trainer_2.id)
    Pokemon.create("Growlie", "Growlithe", 42, trainer_3.id)
    Pokemon.create("Tiny", "Ponyta", 40, trainer_3.id)
    Pokemon.create("Stelle", "Rapidash", 42, trainer_3.id)
    Pokemon.create("Arcane", "Arcanine", 47, trainer_3.id)
    Pokemon.create("Pidgeot", "Pidgeot", 61, trainer_4.id)
    Pokemon.create("Alakazam", "Alakazam", 59, trainer_4.id)
    Pokemon.create("Rhydon", "Rhydon", 61, trainer_4.id)
    Pokemon.create("Arcanine", "Arcanine", 61, trainer_4.id)
    Pokemon.create("Exeggutor", "Exeggutor", 63, trainer_4.id)
    Pokemon.create("Blastoise", "Blastoise", 65, trainer_4.id)

seed_vs_seeker()
print("VS Seeker seeded!")