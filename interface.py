import inquirer

from sublayers.address_book import CONFIG as ab_config
from sublayers.handler import Handler


main_menu = [
    inquirer.List('option',
                  message='You are in main menu. Please select an option:',
                  choices=[
                      'Address Book',
                      'Note Book',
                      'Sorter Assist',
                      'Exit'
                  ])
]

if __name__ =='__main__':
    while True:
        main_choice = inquirer.prompt(main_menu)['option']

        if main_choice == 'Address Book':
            handler = Handler(**ab_config)
            handler.run()

        elif main_choice == 'Note Book':
            print('Not ready yet')

        elif main_choice == 'Sorter Assist':
            print('Not reay yet')
        
        elif main_choice == 'Exit':
            print("Exiting program...")
            break
