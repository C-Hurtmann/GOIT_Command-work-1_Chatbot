import pickle
from collections import UserDict
from colorama import Fore


class NoteBook(UserDict):
    file_name = 'Notebook.bin'

    def show_all_records(self):
        return self.data

    def iterate(self, n=1):
        for key in self.data.items():
            d_list = list(self.data.values())
            for i in range(0, len(d_list), n):
                yield key, d_list[i:i + n]

    def add_record(self, record):
        self.data[record.title.value] = record

    def remove_record(self, record):
        self.data.pop(record)

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
        print(self.tag)

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

        tag = getattr(record, 'tag', '')
        if tag:
            tag_value = tag.value
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
    notebook = NoteBook()
    notebook.load_notes()
    while True:
        print(Fore.LIGHTBLUE_EX + '__________________________________________________\n'
              'You can use following commands:\n'
              '|add| - Add a new note\n'
              '|remove| - remove a note\n'
              '|find| - Find note in Notebook\n'
              '|show all| - Shows the entire Notebook\n'
              '|close, exit, goodbye or .| - Closing the program\n'
              '__________________________________________________\n')
        user_inp = input('Enter command: ').lower().strip()
        user_exit_list = ['goodbye', 'close', 'exit', '.']
        if user_inp in user_exit_list:
            print('Goodbye!\n'
                  'Your Note has been successfully saved in the Notebook!')
            break
        elif user_inp == 'hello':
            print('How can I help you?')
            continue
        elif 'add' in user_inp:
            add_handler(notebook)
        elif 'find' in user_inp:
            find_handler(notebook)
        elif 'show all' in user_inp:
            show_all_handler(notebook)
        elif 'remove' in user_inp:
            remove_handler(notebook)
        else:
            print('Choose the right command!')
            continue


def add_handler(notebook):
    user_title = input("Enter a title: ")
    title = Title(user_title)
    record = Record(title=title)
    user_text = input("Enter a text of note: ")
    text = Text(user_text)
    record.text = text
    user_tag = input("Enter a #tag: ")
    tag = Tag(user_tag)
    record.tag = tag
    notebook.add_record(record)
    notebook.save_notes()


def remove_handler(notebook):
    data = notebook.show_all_records()
    if not data:
        print('The notebook is empty.')


def show_all_handler(notebook):
    data = notebook.show_all_records()
    if not data:
        print('The notebook is empty.')
    else:
        for title, record in data.items():
            rec_data = record.formatting_record(record)
            print(
                f"\n|Title: {title}\n|Text: {rec_data['text']}\n|#tag: {rec_data['#tag']}\n")


def find_handler(notebook):
    find_user = input('Enter title or #tag: ')
    data = notebook.show_all_records()
    if not data:
        print('The notebook is empty.')
    else:
        flag = False
        for title, record in data.items():
            rec_data = record.formatting_record(record)
            if title.startswith(find_user):
                flag = True
                print(
                    f"\n|Title: {title}\n|Text: {rec_data['text']}\n|#tag: {rec_data['#tag']}\n")
            tag = getattr(record, 'tag', '')
            if tag:
                if tag.value.startswith(find_user):
                    flag = True
                    print(
                        f"\n|Title: {title}\n|Text: {rec_data['text']}\n|#tag: {rec_data['#tag']}\n")
        if not flag:
            print('Note with this title or #tag was not found.')


if __name__ == "__main__":
    main()
