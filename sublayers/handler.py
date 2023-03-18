import difflib

from address_book import AddressBook, commands, help


class Handler:
    def __init__(self, help, commands, database=None):
        self.database = database
        self.commands = commands
        self.help = help

    def get_command_suggestion(self, query):
        return difflib.get_close_matches(query, self.commands.keys(), n=1, cutoff=0.6)
    
    def run(self):
        print(self.help)
        while True:
            query = input('> ')
            try:
                self.commands[query](self.database)
            except KeyError:
                suggestion = self.get_command_suggestion(query)
                if suggestion:
                    print(f'Did you mean {suggestion[0]}?')
                else:
                    print('ERROR: Invalid command')
                    print(self.help)



if __name__ == '__main__':
    handler = Handler(help=help, commands=commands, database=AddressBook())
    handler.run()