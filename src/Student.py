import pandas as pd
from src.Database import Database
from datetime import datetime

# Định nghĩa các cột cho DataFrame khi hiển thị danh sách sinh viên
columnsStudent = [
    "StudentID",
    "StudentName",
    "BirthDate",
    "Email",
    "PhoneNumber",
    "Address",
]

class Student:
    def __init__(
        self,
        student_name: str,
        birth_date: str,
        email: str,
        phone_number: str,
        address: str,
        student_id: int = None,
    ):
        # Hàm khởi tạo lớp Student với các thuộc tính cơ bản
        self.student_id = student_id
        self.student_name = student_name
        self.birth_date = birth_date
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def checkIdStudent(self, db: Database, student_id: int) -> bool:
        # Kiểm tra xem mã sinh viên có tồn tại trong cơ sở dữ liệu hay không
        query = "SELECT EXISTS(SELECT 1 FROM student WHERE student_id = %s)"
        values = (student_id,)
        checkPoint = db.fetch(query, values)
        return bool(checkPoint[0][0]) if checkPoint else False

    def addStudent(self, db: Database) -> bool:
        # Thêm một sinh viên mới vào cơ sở dữ liệu
        self.birth_date = datetime.strptime(
            self.birth_date, "%Y-%m-%d"
        ).date()  # Chuyển đổi từ chuỗi sang kiểu ngày
        query = "INSERT INTO student (student_name, birth_date, email, phone_number, address) VALUES(%s, %s, %s, %s, %s)"
        values = (
            self.student_name,
            self.birth_date,
            self.email,
            self.phone_number,
            self.address,
        )
        return db.execute(query, values)

    def removeStudent(self, db: Database, student_id: int) -> bool:
        # Xóa một sinh viên khỏi cơ sở dữ liệu dựa trên mã sinh viên
        if self.checkIdStudent(db, student_id):
            query = "DELETE FROM student WHERE student_id = %s"
            values = (student_id,)
            return db.execute(query, values)
        return False

    def displayAllStudents(self, db: Database) -> pd.DataFrame:
        # Hiển thị danh sách tất cả sinh viên trong cơ sở dữ liệu
        query = "SELECT * FROM student"
        data = db.fetch(query, None)
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data, columns=columnsStudent)

    def displayOneStudent(self, db: Database, student_id: int) -> pd.DataFrame:
        # Hiển thị thông tin chi tiết của một sinh viên dựa trên mã sinh viên
        if not self.checkIdStudent(db, student_id):
            return pd.DataFrame()
        query = "SELECT * FROM student WHERE student_id = %s"
        values = (student_id,)
        data = db.fetch(query, values)
        return pd.DataFrame(data, columns=columnsStudent)

    def editStudent(
        self,
        db: Database,
        student_id: int,
        student_name: str,
        birth_date: str,
        email: str,
        phone_number: str,
        address: str,
    ) -> bool:
        # Sửa thông tin của một sinh viên dựa trên mã sinh viên
        updates = []
        values = []
        if student_name:
            updates.append("student_name = %s")
            values.append(student_name)
        if birth_date:
            updates.append("birth_date = %s")
            values.append(datetime.strptime(birth_date, "%Y-%m-%d").date())
        if email:
            updates.append("email = %s")
            values.append(email)
        if phone_number:
            updates.append("phone_number = %s")
            values.append(phone_number)
        if address:
            updates.append("address = %s")
            values.append(address)
        if not updates:
            return False
        query = f"UPDATE student SET {', '.join(updates)} WHERE student_id = %s"
        values.append(student_id)
        return db.execute(query, tuple(values))
