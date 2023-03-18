from sublayers.address_book import main as address_book
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
        return sublayer()


if __name__ == '__main__':
    handler = Handler()
    while True:
        query = input('> ')
        handler.run(query)
        print('-' * 50)