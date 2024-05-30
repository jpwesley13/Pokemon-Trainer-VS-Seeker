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
    pokemons = trainer.pokemons()
    print(
        trainer.details(), 
        "\n======",
        f"\n{trainer.name}'s Pokemon:\n")
    for index, pokemon in enumerate(pokemons, start = 1):
        print(f"{index}. {pokemon}")

def register_trainer():
    name = input("Enter the trainer's name: ")
    hometown = input("Enter the trainer's hometown: ")
    badges = badge_validation()
    try:
        trainer = Trainer.create(name, hometown, badges)
        print(f"{trainer} registered to the VS Seeker!")
    except Exception as exc:
        print("Error registering trainer: ", exc)
    all_trainers()

def badge_validation(badge=None):
    if badge is not None:
        try:
            badge = int(badge)
        except ValueError:
            pass
    else:
        badges = input("How many badges does the trainer have?: ")
        try:
            badge = int(badges)
        except ValueError:
            pass
    return badge

def update_trainer(id_):
    trainer = Trainer.find_by_id(id_)
    try:
        name = input("Enter the trainer's new name: ")
        badges = input("Enter the trainer's new badge count: ")
        if name:
            trainer.name = name
        trainer.badges = badge_validation(badges)

        trainer.update()
        print(f"{trainer.name} has been updated!")
    except Exception as exc:
        print("Error updtating trainer: ", exc)

def delete_trainer(id_):
    trainer = Trainer.find_by_id(id_)
    trainer.delete()
    print(f"{trainer.name} removed from VS Seeker!\n")