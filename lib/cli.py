# lib/cli.py

from helpers import (
    exit_program,
    all_trainers
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "A" or "a":
            all_trainers()
        elif choice == "E" or "e":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("A. View all trainers")
    print("E. Exit VS Seeker")


if __name__ == "__main__":
    main()
