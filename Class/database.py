import os
import mysql.connector

class Database:
    def __init__(self):
        host = os.environ.get("db_host", "10.10.1.54")
        user = "root"
        password = os.environ.get("db_password", "")
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
        return [ dict(line) for line in [zip([ column[0] for column in mycursor.description], row) for row in mycursor.fetchall()] ]
        
        
