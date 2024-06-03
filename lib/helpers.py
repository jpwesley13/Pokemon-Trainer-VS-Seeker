# lib/helpers.py

from models.trainer import Trainer
from models.pokemon import Pokemon

def exit_program():
    print("VS Seeker shutting down!")
    exit()

def all_trainers():
    trainers = Trainer.get_all()
    print("\nRegistered Trainers:")
    print("============\n")
    for index, trainer in enumerate(trainers, start=1):
        print(f"{index}. {trainer}")
    print("\n============")
    return trainers

def trainer_details(id_):
    trainer = Trainer.find_by_id(id_)
    pokemons = trainer.pokemons()
    print(trainer.details()) 
    print(f"\n{trainer.name}'s Pokemon:")
    print("============\n")
    for index, pokemon in enumerate(pokemons, start = 1):
        print(f"{index}. {pokemon}")
    print("\n============")
    return pokemons

def trainer_pokemon(id_):
    trainer = Trainer.find_by_id(id_)
    pokemons = trainer.pokemons()
    return pokemons

def register_trainer():
    name = input("Enter the trainer's name: ")
    hometown = input("Enter the trainer's hometown: ")
    badges = badge_validation()
    try:
        trainer = Trainer.create(name, hometown, badges)
        print(f"\n{trainer} registered to the VS Seeker!")
        return True
    except Exception as exc:
        print("Error registering trainer: ", exc)
        return False

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
        if badges != "":
            trainer.badges = badge_validation(badges)

        trainer.update()
        print(f"\n{trainer.name} has been updated!\n")
    except Exception as exc:
        print("Error updtating trainer: ", exc)

def delete_trainer(id_):
    trainer = Trainer.find_by_id(id_)
    print(trainer)
    pokemons = trainer.pokemons()
    for pokemon in pokemons:
        pokemon.delete()
    trainer.delete()
    print(f"\n{trainer.name} removed from VS Seeker!")

def new_pokemon(trainer_id):
    nickname = input("Enter the Pokemon's nickname: ")
    species = input("Enter the Pokemon's species: ")
    level = level_validation()
    trainer = Trainer.find_by_id(trainer_id)
    trainer_name = trainer.name
    try:
        pokemon = Pokemon.create(nickname, species, level, trainer_id)
        print("============\n")
        print(f"{trainer_name} caught {pokemon} the {species}!")
        print("\n============")
        return True
    except Exception as exc:
        print("Error adding new Pokemon: ", exc)
        return False

def level_validation(level=None):
    if level is not None:
        try:
            level = int(level)
        except ValueError:
            pass
    else:
        levels = input("Enter the Pokemon's level: ")
        try:
            level = int(levels)
        except ValueError:
            pass
    return level

def pokemon_details(id_):
    pokemon = Pokemon.find_by_id(id_)
    trainer = Trainer.find_by_id(pokemon.trainer)
    print(f"{trainer.name} has caught this Pokemon: ")
    print("------------")
    print(pokemon.details())
    print("------------")

def update_pokemon(id_):
    pokemon = Pokemon.find_by_id(id_)
    try:

        nickname = input("Enter the Pokemon's new nickname: ")
        species = input("Enter the Pokemon's new evolved species: ")
        level = input("Enter the Pokemon's new level: ")
        if nickname:
            pokemon.nickname = nickname
        if species:
            pokemon.species = species
        if level:
            pokemon.level = level_validation(level)

        pokemon.update()
        print(f"\n{pokemon.nickname} has been updated!\n")
    except Exception as exc:
        print("Error updtating Pokemon: ", exc)

def release_pokemon(id_):
    pokemon = Pokemon.find_by_id(id_)
    pokemon.delete()
    print(f"\n{pokemon.nickname} was released back into the wild!\n")