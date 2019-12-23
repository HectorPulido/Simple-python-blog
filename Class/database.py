import mysql.connector

class Database:
    def __init__(self):
        host = "localhost"
        user = "root"
        password = ""
        db = "blogtest"

        self.con = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=db
            )


    def insert(self, query, values):
        mycursor = self.con.cursor()
        mycursor.execute(query, values)
        self.con.commit()

    def select(self, query, values):
        mycursor = self.con.cursor()
        mycursor.execute(query, values)
        return mycursor.fetchall()
        
        