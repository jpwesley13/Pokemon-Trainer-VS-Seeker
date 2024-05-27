#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.pokemon import Pokemon
from models.trainer import Trainer
import ipdb

def reset():
    Pokemon.drop_table()
    Trainer.drop_table()
    Trainer.create_table()
    Pokemon.create_table()

    trainer_1 = Trainer.create("Dakota", "Purgsville", 3)
    trainer_2 = Trainer.create("Dyna", "Italyton", 8)
    Pokemon.create("Rori", "Pikachu", 26, trainer_1.name)
    Pokemon.create("Ali", "Arcanine", 73, trainer_2.name)

reset()
ipdb.set_trace()
