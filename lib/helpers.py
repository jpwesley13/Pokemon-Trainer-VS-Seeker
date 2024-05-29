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

def trainer_details(id_):
    trainer = Trainer.find_by_id(id_)
    print(trainer.details())

def register_trainer():
    name = input("Enter the trainer's name: ")
    hometown = input("Enter the trainer's hometown: ")
    badges = input("How many badges does the trainer have?: ")
    try:
        badges = int(badges)
        trainer = Trainer.create(name, hometown, badges)
        print(f'{trainer} registered to the VS Seeker!')
    except Exception as exc:
        print("Error registering trainer: ", exc)
    all_trainers()

def delete_trainer():
    pass