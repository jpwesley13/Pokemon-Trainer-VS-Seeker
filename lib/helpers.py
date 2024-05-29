# lib/helpers.py

from models.trainer import Trainer
from models.pokemon import Pokemon

def exit_program():
    print("VS Seeker shutting down!")
    exit()

def all_trainers():
    trainers = Trainer.get_all()
    for trainer in trainers:
        print(trainer)

