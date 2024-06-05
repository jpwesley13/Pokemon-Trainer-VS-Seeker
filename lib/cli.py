# lib/cli.py

from helpers import (
    main_menu,
    sub_menu_trainers,
    sub_menu_trainer,
    sub_menu_pokemon,
    exit_program,
    all_trainers,
    register_trainer,
    trainer_details,
    trainer_pokemon,
    delete_trainer,
    update_trainer,
    new_pokemon,
    pokemon_details,
    update_pokemon,
    release_pokemon
)



def main():
    while True:
        main_menu()
        
        choice = input("> ")
        if choice.lower() == "a":
            trainers_menu()
        elif choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice")

def trainers_menu():
    while True:
        trainers = all_trainers()
        sub_menu_trainers()

        choice = input("> ")
        if choice.isdigit():
            trainer_num = int(choice)
            if trainer_num > 0 and trainer_num <= len(trainers):
                trainer = trainers[trainer_num - 1]
                print()
                trainer_details_menu(trainer.id)
            else:
                print("Invalid trainer ID")
        elif choice.lower() == "n":
            register_trainer()
        elif choice.lower() == "b":
            return
        elif choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice")

def trainer_details_menu(id_):
    while True:
        trainer_details(id_)
        sub_menu_trainer()

        choice = input("> ")
        if choice.isdigit():
            pokemon_id = int(choice)
            pokemons = trainer_pokemon(id_)
            if pokemon_id > 0 and pokemon_id <= len(pokemons):
                pokemon = pokemons[pokemon_id - 1]
                print()
                pokemon_details_menu(pokemon.id)
            else:
                print("Invalid Pokemon ID")
        elif choice.lower() == "n":
            new_pokemon(id_)
        elif choice.lower() == "u":
            update_trainer(id_)
        elif choice.lower() == "d":
            delete_trainer(id_)
            return
        elif choice.lower() == "b":
            return
        elif choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice")

def pokemon_details_menu(pokemon_id):
    while True:
        pokemon_details(pokemon_id)
        sub_menu_pokemon()

        choice = input("> ")
        if choice.lower() == "u":
            update_pokemon(pokemon_id)
        elif choice.lower() == "r":
            release_pokemon(pokemon_id)
            return
        elif choice.lower() == "b":
            return
        elif choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
