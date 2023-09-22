import data
import note

def checkInList(input):
    listOfNotes = data.read_file()
    for notes in listOfNotes:  
        if input == notes.getId():
            return True