class Handler:
    sublayers = {('1', 'ab', 'address book'): 'Address Book',
                  ('2', 'nb', 'note book'): 'Note Book',
                  ('3', 'sa', 'sorter assist'): 'Sorter Assist'}

    def __init__(self):
        print('Bot activated')

    def run(self, query: str):
        for keywords in self.sublayers.keys():
            if query in keywords:
                self.run_sublayer(self.sublayers[keywords])
        else:
            print('Wrong command')

    def run_sublayer(self, sublayer):
        print(f'You are in {sublayer}')
        stop_words = ('back')
        def run_command():
            while True:
                query = input('> ')
                if query not in stop_words:
                    print(f'Some {sublayer} command')
                else:
                    print('You are in main menu')
                    break
        return run_command()


if __name__ == '__main__':
    handler = Handler()
    while True:
        query = input('> ')
        handler.run(query)
        print('-' * 50)