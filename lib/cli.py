# lib/cli.py

from helpers import (
    exit_program,
    all_trainers
)



def main():
    while True:
        menu()
        choice = input("> ")
        if choice.lower() == "a":
            from models.trainer import Trainer
            trainers = Trainer.get_all()
            all_trainers()
            trainers_menu(trainers)
        elif choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("A. View all trainers")
    print("E. Exit VS Seeker")

def trainers_menu(trainers):
    while True:
        print("\nEnter trainer's ID for additional details")
        print("      or")
        print("N. Add a new trainer")
        print("B. Back to previous menu")
        print("E. Exit VS Seeker")

        choice = input("> ")
        if choice.isdigit():
            trainer_id = int(choice)
            if trainer_id > 0 and trainer_id <= len(trainers):
                selected_trainer = trainers[trainer_id - 1]
                print(f"\nAdditional details for {selected_trainer}:")
            else:
                print("Invalid trainer ID")
        elif choice.lower() == "n":
            print("Add a new trainer option selected")
        elif choice.lower() == "b":
            return
        elif choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
