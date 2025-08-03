import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host = 'localhost',user='root',password='',database='hit-db-demo')
            self.mycursor = self.conn.cursor()
        except:
            print("Connected to Database")
        else:
            print('Some error occured')