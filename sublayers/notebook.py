import pickle
from collections import UserDict
from colorama import Fore


class Notebook(UserDict):
    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    file_name = 'Notebook.bin'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_notes()

    def show_all_records(self):
        return self.data

    def iterate(self, n=1):
        for key, _ in self.data.items():
            d_list = list(self.data.values())
            for i in range(0, len(d_list), n):
                yield key, d_list[i:i + n]

    def add_record(self, record):
        self.data[record.title.value] = record

    def save_notes(self):
        with open(self.file_name, 'wb') as file:
            pickle.dump(self.data, file)
        print(f'Your notes are saved!')

    def load_notes(self):
        try:
            with open(self.file_name, 'rb') as file:
                self.data = pickle.load(file)
        except:
            return


class Record:
    def __init__(self, title=None, text=None, tag=None):
        self.title = title
        self.text = text
        self.tags = []
        if tag:
            self.tags.append(tag)

    def add_tag(self, tag):
        self.tags.append(tag)

    def create_tag(self, record, user_tag=None, update=False):
        if user_tag:
            for _ in range(10):
                tag = Tag(user_tag)
                if update:
                    record.tags = [tag]
                else:
                    record.add_tag(tag)
                    break

    def create_text(self, record, user_text):
        if user_text:
            for _ in range(10):
                text = Text(user_text)
                record.text = text
                break

    def create_title(self, record, user_title):
        if user_title:
            for _ in range(10):
                title = Title(user_title)
                record.title = title
                break

    def formatting_record(self, record):
        title = getattr(record, 'title', '')
        if title:
            title_value = title.value
        else:
            title_value = "not found"

        text = getattr(record, 'text', '')
        if text:
            text_value = text.value
        else:
            text_value = "not found"

        tags = getattr(record, 'tags', '')
        if tags:
            tag_value = [tag.value for tag in tags]
        else:
            tag_value = "not found"

        return {"title": title_value, "text": text_value, "#tag": tag_value}


class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


class Title(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if len(value) >= 20:
            raise ValueError


class Text(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if len(value) >= 150:
            raise ValueError


class Tag(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if len(value) >= 5:
            raise ValueError


def main():
    notebook = Notebook()
    print(Fore.LIGHTBLUE_EX + '-' * 52)
    print('|You can use following commands:\n'
          '|add - add a new note in Notebook\n'
          '|del - delete a note from Notebook\n'
          '|change - change a note in Notebook\n'
          '|find - find note in Notebook\n'
          '|tag sort - sorts notes by tags in Notebook\n'
          '|show all - shows the entire Notebook\n'
          '|close, exit, goodbye or . - closing the program\n')
    print('-' * 52)
    while True:
        user_inp = input('Enter command: ').lower().strip()
        user_exit_list = ['goodbye', 'close', 'exit', '.']
        if user_inp in user_exit_list:
            print('Goodbye!\n'
                  'Your Notebook has been successfully saved!')
            break
        elif user_inp == 'hello':
            print('How can I help you?')
            continue
        elif 'add' in user_inp:
            CommandsHandler.add_note(notebook)
        elif 'del' in user_inp:
            CommandsHandler.remove_note(notebook)
        elif 'change' in user_inp:
            CommandsHandler.change_note(notebook)
        elif 'find' in user_inp:
            CommandsHandler.find_note(notebook)
        elif 'tag sort' in user_inp:
            CommandsHandler.sort_notes_by_tag(notebook)
        elif 'show all' in user_inp:
            CommandsHandler.show_all_notes(notebook)
        else:
            print('Choose the right command!')
            continue


class CommandsHandler:
    notebook = Notebook()

    def add_note(self):
        user_title = input("Enter a title: ")
        title = Title(user_title)
        #record.title = title
        record = Record(title=title)
        record.create_title(record=record, user_title=user_title)
        user_text = input("Enter a text of note: ")
        text = Text(user_text)
        record.text = text
        record.create_text(record=record, user_text=user_text)
        user_tag = input("Enter a #tag: ")
        tag = Tag(user_tag)
        record.tag = tag
        record.create_tag(record=record, user_tag=user_tag)
        self.notebook.add_record(record)
        self.notebook.save_notes()

    def show_all_notes(self):
        data = self.notebook.show_all_records()
        if not data:
            print('The notebook is empty.')
        else:
            for title, record in data.items():
                rec_data = record.formatting_record(record)
                print(f"|Title: {title}\n"
                      f"|Text: {rec_data['text']}\n"
                      f"|Tag: {rec_data['#tag']}\n")

    def find_note(self):
        find_user = input('Enter title or #tag: ')
        data = self.notebook.show_all_records()
        if not data:
            print('The notebook is empty.')
        else:
            flag = False
            for title, record in data.items():
                rec_data = record.formatting_record(record)
                if title.startswith(find_user):
                    flag = True
                    print(f"|Title: {title}\n"
                          f"|Text: {rec_data['text']}\n"
                          f"|Tag: {rec_data['#tag']}\n")
                tag = getattr(record, 'tag', '')
                if tag:
                    if tag.value.startswith(find_user):
                        flag = True
                        print(f"|Title: {title}\n"
                              f"|Text: {rec_data['text']}\n"
                              f"|Tag: {rec_data['#tag']}\n")
            if not flag:
                print('Note with this title or #tag was not found.')

    def sort_notes_by_tag(notebook):
        #notebook.notes = sorted(notebook.notes, key=lambda x: x.tags)
        pass

    def change_note(self):
        change_user = input('Enter title of note: ')
        data = self.notebook.show_all_records()
        if not data:
            print('The Notebook is empty.')
        else:
            flag = False
            for title, record in data.items():
                rec_data = record.formatting_record(record)
                if title.startswith(change_user):
                    flag = True
                    print("-"*50)
                    print(f"|add tag - press 1|\n"
                          f"|change title - press 2|\n"
                          f"|change text - press 3|\n"
                          f"|change tag - press 4")
                    print("-" * 50)
                    change = int(input('Enter your choice: '))
                    if change == 1:
                        tag_add = input('Enter a tag: ')
                        record.create_tag(record=record, user_tag=tag_add,
                                          update=False)
                        print(f'In note {title} append '
                              f'{[tag.value for tag in record.tags]}')
                    elif change == 2:
                        new_title = input('Enter a new title: ')
                        record.title = Title(new_title)
                        print(f'In note title {title} was changed to '
                              f'{record.title.value}')
                    elif change == 3:
                        text = input('Enter a new text: ')
                        record.create_text(
                            record=record, user_text=text)
                        print(f'In note {title} change text '
                              f'{record.text.value}')
                    elif change == 4:
                        tag_add = input('Enter a tag: ')
                        record.create_tag(record=record, user_tag=tag_add,
                                          update=True)
                        print(f'In note {title} update '
                              f'{[tag.value for tag in record.tags]}')
                    else:
                        print(f'{change} invalid choice')
                        return
            self.notebook.save_notes()

    def remove_note(self):
        print('|del - Delete note|\n'
              '|del all - Clean Noteook|')
        remove_date = input('Enter your choice: ')
        if remove_date == 'del':
            remove_note = input('Enter a title of the note to be deleted: ')
            self.notebook.data.pop(remove_note)
            print(f'Note {remove_note} deleted.')
        elif remove_date == 'del all':
            print(f'Are you sure you want to clear the Notebook?')
            question = input('Y or N: ').lower().strip()
            if question == 'n':
                print('non')
                return
            elif question == 'y':
                print('lol')
                self.notebook.data.clear()
        self.notebook.save_notes()


# ------------------------------------------------ADAPTER-------------------------------------------------------
help = ('|You can use following commands:\n'
        '|add - add a new note in Notebook\n'
        '|del - delete a note from Notebook\n'
        '|change - change a note in Notebook\n'
        '|find - find note in Notebook\n'
        '|tag sort - sorts notes by tags in Notebook\n'
        '|show all - shows the entire Notebook\n'
        '|back - Closing the sublayer\n')

commands = {'add': CommandsHandler().add_note,
            'del': CommandsHandler().remove_note,
            'change': CommandsHandler().change_note,
            'find': CommandsHandler().find_note,
            'tag sort': CommandsHandler().sort_notes_by_tag,
            'show all': CommandsHandler().show_all_notes,
            'back': ...}

CONFIG = ({'help': help,
           'commands': commands
           })


if __name__ == "__main__":
    main()
