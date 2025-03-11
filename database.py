import psycopg2 
import pandas as pd 

class Database:
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        """Kết nối với PostgreSQL"""
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.cur = self.conn.cursor()
    
    # chi dung dung de gui truy van den database
    def execute(self, query, values = None):
        self.cur.execute(query, values or ())
        self.conn.commit()

    # gui truy van den db va lay du lieu tu db ve
    def fetch(self, query, values =None):
        self.cur.execute(query,values or None)
        return self.cur.fetchall() # lay tat ca cac du lieu tu truy van
    



    