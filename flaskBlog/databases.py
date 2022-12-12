import sqlite3



class UsersData():
    def __init__(self) -> None:
        super().__init__()
        self.createDataBase()
        
    
    def createDataBase(self):
        self.__db = sqlite3.connect("users.sqlite", check_same_thread=False)
        
        with self.__db:

            self.__cursor =  self.__db.cursor()

            self.__cursor.execute('''CREATE TABLE IF NOT EXISTS usersdatabase
                (content_id INTEGER PRIMARY KEY,
                    username NOT NULL,
                    password NOT NULL)'''
                )
            

    def appendData(self,userName:str, password:str):
        if self.fetchallData(user_name=userName):
            self.__cursor.executemany('INSERT INTO usersdatabase(username, password) VALUES (?,?)', [(userName, password)])
            self.__db.commit()
            return True
            
        else:
            return False
            
            
    def fetchallData(self, user_name=str):
        data = self.__cursor.execute("SELECT * From usersdatabase WHERE username = ?", [user_name])
        if data.fetchone():
            return False
        else:
            return True


    def loginISTrue(self, user_name=str, password=str):
        data = self.__cursor.execute("SELECT * From usersdatabase WHERE username = ? AND password = ?", [user_name, password])
        if data.fetchone():
            return True
        else:
            return False



class AppendMkl():
    def __init__(self) -> None:
        super().__init__()
        self.createDataBase()
        
    
    def createDataBase(self):
        self.__db = sqlite3.connect("article.sqlite", check_same_thread=False)
        
        with self.__db:

            self.__cursor =  self.__db.cursor()

            self.__cursor.execute('''CREATE TABLE IF NOT EXISTS articles
                (content_id INTEGER PRIMARY KEY,
                    title NOT NULL,
                    content NOT NULL,
                    author NOT NULL)'''
                )
            

    def appendData(self,title:str, content:str , author:str):
        if self.fetchallData(title=title):
            self.__cursor.executemany('INSERT INTO articles(title, content, author) VALUES (?,?,?)', [(title, content,author)])
            self.__db.commit()
            return True
            
        else:
            return False
            
            
    def fetchallData(self, title=str):
        data = self.__cursor.execute("SELECT * From articles WHERE title = ?", [title])
        if data.fetchone():
            return False
        else:
            return True


    def getTotalContent(self):
        data = self.__cursor.execute("SELECT * From articles").fetchall()
        return data[::-1]

    def queryIdNumber(self, Id:int):
        __IdNumber = self.__cursor.execute("SELECT * From articles WHERE content_id = ?", (int(Id),)).fetchone()
        if __IdNumber != None:
            return (__IdNumber)
        
        else:
            return False