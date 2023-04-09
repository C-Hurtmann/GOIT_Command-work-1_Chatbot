import inquirer

from bot.sublayers.addressbook import commands as ab_commands
from bot.sublayers.notebook import commands as nb_commands
from bot.sublayers.cleaner import commands as sa_commands
from bot.sublayers.game import commands as gm_commands
from bot.sublayers.handler import Handler


main_menu = [
    inquirer.List(
        "option",
        message="You are in main menu. Please select an option:",
        choices=["Address Book", "Note Book", "Sorter Assist", "Games", "Exit"],
    )
]


def main():
    while True:
        main_choice = inquirer.prompt(main_menu)["option"]

        if main_choice == "Address Book":
            handler = Handler(ab_commands)
            handler.run()

        elif main_choice == "Note Book":
            handler = Handler(nb_commands)
            handler.run()

        elif main_choice == "Sorter Assist":
            handler = Handler(sa_commands)
            handler.run()

        elif main_choice == 'Games':
            handler = Handler(gm_commands)
            handler.run()

        elif main_choice == "Exit":
            print("Exiting program...")
            break


if __name__ == "__main__":
    main()
