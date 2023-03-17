from sublayers.address_book import main as address_book, Adapter
from sublayers.notebook import main as note_book


def plug():
    print('Do something')

class Handler:
    sublayers = {('1', 'ab', 'address book'): address_book,
                  ('2', 'nb', 'note book'): note_book,
                  ('3', 'sa', 'sorter assist'): plug}

    def __init__(self):
        print('Bot activated')

    def run(self, query: str):
        for keywords in self.sublayers.keys():
            if query in keywords:
                self.run_sublayer(self.sublayers[keywords])

    def run_sublayer(self, sublayer):
        print('You are in sublayer')
        back_words = ('back')
        if sublayer == address_book:
            while True:
                query = input('> ')
                if query == 'add':
                    name = input('Enter contact name: ')
                    phone = input('Enter contact phone: ')
                    email = input('Enter contact Birthday: ')
                    Adapter().add_contact(name, phone, email)
                else:
                    print('Not ready yet')

        def run_commands(*args):
            while True:
                query = input('> ')
                if query in back_words:
                    print('You are went back to main menu')
                    break
                return sublayer(*args)
            return run_commands



if __name__ == '__main__':
    handler = Handler()
    while True:
        query = input('> ')
        handler.run(query)
        print('-' * 50)