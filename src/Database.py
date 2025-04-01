import configparser
import psycopg2

# Đọc file cấu hình .ini
config = configparser.ConfigParser()
config.read(
    "f:\\Document\\Tổng hợp các môn học\\Python Programming\\Lab\\Lab2\\Bài 1\\.ini"
)

db = config["database"]["dbName"]
hostname = config["database"]["hostName"]
password = config["database"]["password"]
username = config["database"]["userName"]
port = config.getint("database", "port")


class Database:
    def __init__(
        self,
        dbname=db,
        username=username,
        password=password,
        hostname=hostname,
        port=port,
    ):
        """Kết nối với PostgreSQL"""
        self.conn = psycopg2.connect(
            dbname=dbname, user=username, password=password, host=hostname, port=port
        )
        self.cur = self.conn.cursor()

    # chi dung dung de gui truy van den database
    def execute(self, query, values=None):
        try:
            self.cur.execute(query, values or ())
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database execution error: {e}")
            return False

    # gui truy van den db va lay du lieu tu db ve
    def fetch(self, query, values=None):
        try:
            self.cur.execute(query, values or ())
            return self.cur.fetchall()  # lay tat ca cac du lieu tu truy van
        except Exception as e:
            print(f"Database fetch error: {e}")
            return []

    def close(self):
        self.cur.close()
        self.conn.close()
        return "Close done"
