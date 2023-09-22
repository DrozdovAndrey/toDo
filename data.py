import note
import csv


def read_file():  
    with open('data.csv', encoding='utf-8') as r_file:
        r_file = csv.DictReader(r_file, delimiter = ";")
        list_of_notes = []
        for row in r_file:
            notes = note.Note(row["id"],row["заголовок"],row["текст"],row["дата"])
            list_of_notes.append(notes)
    return list_of_notes  

def write_list_to_file(list_of_notes: list[note.Note]):
    with open('data.csv', mode="w", encoding='utf-8') as w_file:
        names = ["id", "заголовок", "текст", "дата"]
        file_writer = csv.DictWriter(w_file, delimiter = ";", 
                                 lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        for i in list_of_notes:
            file_writer.writerow({"id": i.getId(), "заголовок": i.getTitle(), "текст": i.getBody(), "дата": i.getDate()})

def write_note_to_file(note: note.Note):
    with open('data.csv', mode="a", encoding='utf-8') as a_file:
        names = ["id", "заголовок", "текст", "дата"]
        file_writer = csv.DictWriter(a_file, delimiter = ";", 
                                 lineterminator="\r", fieldnames=names)
        file_writer.writerow({"id": note.getId(), "заголовок": note.getTitle(), "текст": note.getBody(), "дата": note.getDate()})

