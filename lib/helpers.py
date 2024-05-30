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
    return trainers

def trainer_details(id_):
    trainer = Trainer.find_by_id(id_)
    pokemons = trainer.pokemons()
    print(
        trainer.details(), 
        "\n======",
        f"\n{trainer.name}'s Pokemon:\n")
    for index, pokemon in enumerate(pokemons, start = 1):
        print(f"{index}. {pokemon}")
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
        print(f"{trainer} registered to the VS Seeker!")
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
        print(f"{trainer.name} has been updated!")
    except Exception as exc:
        print("Error updtating trainer: ", exc)

def delete_trainer(id_):
    trainer = Trainer.find_by_id(id_)
    trainer.delete()
    print(f"{trainer.name} removed from VS Seeker!\n")

def new_pokemon(trainer_id):
    nickname = input("Enter the Pokemon's nickname: ")
    species = input("Enter the Pokemon's species: ")
    level = level_validation()
    trainer = Trainer.find_by_id(trainer_id)
    trainer_name = trainer.name
    try:
        pokemon = Pokemon.create(nickname, species, level, trainer_name)
        print(f"{trainer_name} caught {pokemon} the {species}!")
        return True
    except Exception as exc:
        print("Error adding new Pokemon: ", exc)
        return False

def level_validation(current, level=None):
    if level is not None:
        try:
            level = int(level)
            if level < current:
                raise ValueError("New level must not be lower than the current level")
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
    print(pokemon.details())

def update_pokemon(id_):
    pokemon = Pokemon.find_by_id(id_)
    try:
        current = pokemon.level
        nickname = input("Enter the Pokemon's new nickname: ")
        species = input("Enter the Pokemon's new evolved species: ")
        level = input("Enter the Pokemon's new level: ")
        if nickname:
            pokemon.nickname = nickname
        if species:
            pokemon.species = species
        if level:
            pokemon.level = level_validation(current, level)

        pokemon.update()
        print(f"{pokemon.nickname} has been updated!")
    except Exception as exc:
        print("Error updtating Pokemon: ", exc)