import os
import datetime
import re
import zipfile
import pdb


# create the main class for the note taking
class NoteApp:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content):
        # create and append note contents to the array
        note = {
            'id': title + str(datetime.datetime.now()),
            'title': title,
            'content': content,
            'created_at': datetime.datetime.now()
        }
        self.notes.append(note)

    def save_notes(self):
        # get the contents of the created array and create system file for each of the item
        with open('notes.txt', 'w') as file:
            for note in self.notes:
                file.write(f"ID: {note['id']}\n")
                file.write(f"Title: {note['title']}\n")
                file.write(f"Content: {note['content']}\n")
                file.write(f"Created At: {note['created_at']}\n")
                file.write('-' * 30 + '\n')

    def list_notes(self):
        print("LIST OF NOTES")
        if len(self.notes) > 0:
            for note in self.notes:
                print(f"ID: {note['id']}")
                print(f"Title: {note['title']}")
                print(f"Created At: {note['created_at']}")
                print('-' * 30)
        else:
            print("You have not created any notes!!!!")

    def search_notes(self, keyword):
        print(f"Searching of '{keyword}' in notes:")
        pattern = re.compile(keyword, re.IGNORECASE)
        for note in self.notes:
            if pattern.search(note['title']) or pattern.search(note['content']):
                print(f"Title: {note['title']}")
                print(f"Title: {note['content']}")
                #print(f"Title: {note['title']}")
                print('-' * 30)

    def zip_notes(self):
        with zipfile.ZipFile('notes.zip', 'w') as zipf:
            zipf.write('notes.txt')

    def unzip_notes(self):
        with zipfile.ZipFile('notes.zip', 'r') as zipf:
            zipf.extractall('unzipped_notes')


if __name__ == "__main__":
    app = NoteApp()
    app.create_note("Meeting", "Discuss project details.")
    app.create_note("Ideas", "Write a new blog post about Python.")
    app.save_notes()
    
    app.list_notes()
    
    app.search_notes("python")

    #app.zip_notes()
    app.unzip_notes()
