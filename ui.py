import keyboard
import note
from colorama import Fore, Style 
import uuid
from datetime import datetime

def createNote():
    notes = editNote()   
    return note.Note(id = str(uuid.uuid1())[0:3],title = notes[0], body = notes[1], date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S")))

def editNote():
    title = ''
    body = ''
    while len(title)<=5:
        print('<Заголовок должен быть больше 5 символов>\n')
        title = input('Введите ЗАГОЛОВОК заметки: ')
    while len(body)<=5:
        print('<Заметка должен быть больше 5 символов>\n')
        body = input('\rВведите ОПИСАНИЕ заметки: ')
    return (title, body)


def menu():
    print('\n' * 50)
    print(Fore.LIGHTBLUE_EX + 'Добро пожаловать в программу "Заметки"')
    print(Style.RESET_ALL) 
    print(Fore.YELLOW + "\n1 - для вывода всех заметок\n2 - для добавления заметки\n3 - для удаления заметки\n4 - для редактирования заметки\n5 - для выборки по дате\n6 - показать элемент по id\n7 - для выхода\n")
    print(Style.RESET_ALL)  

def continueWork():
    print('Нажмите пробел для продолжения...')
    keyboard.wait('space')