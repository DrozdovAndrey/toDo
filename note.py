from datetime import datetime
import uuid


class Note:
    def __init__(self, id = str(uuid.uuid1())[0:3],  title = "текст", body = 'текст', date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.__id = id
        self.__title = title
        self.__body = body
        self.__date = date

    def getId(self):
        return self.__id

    def getDate(self):
        return self.__date    

    def setId(self):
        self.__id = str(uuid.uuid1())[0:3]

    def setTitle(self, title):
        self.__.title = title

    def setBody(self, body):
        self.__body = body

    def setDate(self):
        self.__date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))        


    def toString(self):
        return self.__id +','+ self.__title + ',' + self.__body + ',' + self.__date
        
    def forShow(self):
         return 'id' +': '+ self.__id +'\n'+ 'Заголовок'+': '+ self.__title + '\n' + 'Тело заметки'+': '+ self.__body + '\n'+ 'Дата публикации'+': '+ self.__date +"\n"