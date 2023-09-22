import data
import note
from colorama import Fore, Style

def add(input_note):
    listOfNotes = data.read_file()
    for notes in listOfNotes:
        if input_note.getId == notes.getId():
            input_note.setId()
    data.write_note_to_file(input_note)
    print(Fore.GREEN + "Заметка добавлена")
    print(Style.RESET_ALL)    
    
def showAllById():
    listOfNotes = data.read_file()
    if len(listOfNotes) > 0:   
        for notes in listOfNotes:
            print('id: ' + notes.getId())
    else:
        print (Fore.RED + '\nНет ни одной задачи\n')
        print(Style.RESET_ALL)  


def show():
    listOfNotes = data.read_file()
    if len(listOfNotes) > 0:
        for notes in listOfNotes:
            print(notes.forShow())
    else:
        print (Fore.RED + '\nНет ни одной задачи\n')
        print(Style.RESET_ALL)  

def showByDate(input):
    isEmpty = True
    listOfNotes = data.read_file()
    for notes in listOfNotes:  
        if input in notes.getDate() :
            print(notes.forShow())
            isEmpty =False
    if isEmpty == True:
        print(Fore.RED + "Задач не найдено")
        print(Style.RESET_ALL)  


def showById(input):
    isEmpty = True
    listOfNotes = data.read_file()
    for notes in listOfNotes:  
       if input == notes.getId():
            print(notes.forShow())
            isEmpty = False
    if isEmpty == True:
        print(Fore.RED + "Задач не найдено")
        print(Style.RESET_ALL)  


def delete(input):
    isDeleted = False
    listOfNotes = data.read_file()
    for notes in listOfNotes:  
        if input == notes.getId() :
            isDeleted = True
            listOfNotes.remove(notes)
            print(Fore.GREEN + "Заметка удалена")
            print(Style.RESET_ALL)  
    data.write_list_to_file(listOfNotes)
    if isDeleted == False :
        print(Fore.RED + 'Такой заметки нет. Возможно вы ввели неверный id')
        print(Style.RESET_ALL)  


def edit(input, newTitle, newBody):
    listOfNotes = data.read_file()
    for notes in listOfNotes:  
        if input == notes.getId():
            notes.setTitle(newTitle)
            notes.setBody(newBody)
            notes.setDate()
            print(Fore.GREEN + 'Заметка изменена')
            print(Style.RESET_ALL)  
    data.write_list_to_file(listOfNotes)