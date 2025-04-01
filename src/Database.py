import configparser
import psycopg2

# Đọc file cấu hình để lấy thông tin kết nối cơ sở dữ liệu
config = configparser.ConfigParser()
config.read(
    "f:\\Document\\Tổng hợp các môn học\\Python Programming\\Lab\\Lab2\\Bài 1\\.ini"
)

# Lấy thông tin cấu hình từ file .ini
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
        # Hàm khởi tạo để kết nối với cơ sở dữ liệu PostgreSQL
        self.conn = psycopg2.connect(
            dbname=dbname, user=username, password=password, host=hostname, port=port
        )
        self.cur = self.conn.cursor()

    def execute(self, query, values=None):
        # Thực thi câu lệnh SQL (INSERT, UPDATE, DELETE)
        try:
            self.cur.execute(query, values or ())
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Database execution error: {e}")
            return False

    def fetch(self, query, values=None):
        # Thực thi câu lệnh SQL (SELECT) và trả về kết quả
        try:
            self.cur.execute(query, values or ())
            return self.cur.fetchall()  # Lấy tất cả dữ liệu từ truy vấn
        except Exception as e:
            print(f"Database fetch error: {e}")
            return []

    def close(self):
        # Đóng kết nối cơ sở dữ liệu
        self.cur.close()
        self.conn.close()
        return "Close done"
