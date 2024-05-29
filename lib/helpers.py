# lib/helpers.py

from models.trainer import Trainer
from models.pokemon import Pokemon

def exit_program():
    print("VS Seeker shutting down!")
    exit()

def all_trainers():
    trainers = Trainer.get_all()
    print("Registered Trainers:")
    for index, trainer in enumerate(trainers, start=1):
        print(f"{index}. {trainer}")