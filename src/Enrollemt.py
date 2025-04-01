from src.Database import Database
import pandas as pd

# Định nghĩa các cột cho DataFrame khi hiển thị danh sách đăng ký
columnsEnrollment = ["enrollmentID", "studentID", "coursesID", "enrollmentDate"]


class Enrollment:
    def __init__(
        self, student_id, courses_id, enrollment_date=None, enrollment_id=None
    ):
        # Hàm khởi tạo lớp Enrollment với các thuộc tính cơ bản
        self.student_id = student_id
        self.courses_id = courses_id
        self.enrollment_date = enrollment_date
        self.enrollment_id = enrollment_id

    def checkIdEnrollment(self, db: Database, enrollment_id: int) -> bool:
        # Kiểm tra xem mã đăng ký có tồn tại trong cơ sở dữ liệu hay không
        query = "SELECT EXISTS(SELECT 1 FROM enrollment WHERE enrollment_id = %s)"
        values = (enrollment_id,)
        checkPoint = db.fetch(query, values)
        return bool(checkPoint[0][0]) if checkPoint else False

    def courseEnrollment(self, db: Database) -> bool:
        # Đăng ký một khóa học cho sinh viên
        query = "INSERT INTO enrollment(student_id, courses_id) VALUES(%s, %s)"
        values = (self.student_id, self.courses_id)
        return db.execute(query, values)

    def removeEnrollment(self, db: Database, enrollment_id: int) -> bool:
        # Xóa một đăng ký khóa học dựa trên mã đăng ký
        if self.checkIdEnrollment(db, enrollment_id):
            query = "DELETE FROM enrollment WHERE enrollment_id = %s"
            values = (enrollment_id,)
            return db.execute(query, values)
        return False

    def displayAllEnrollment(self, db) -> pd.DataFrame:
        # Hiển thị danh sách tất cả các đăng ký trong cơ sở dữ liệu
        query = "SELECT * FROM enrollment"
        data = db.fetch(query, None)
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data, columns=columnsEnrollment)

    def displayOneEnrollment(
        self, db: Database, student_id: int, courses_id: int
    ) -> pd.DataFrame:
        # Hiển thị thông tin chi tiết của một đăng ký dựa trên mã sinh viên và mã khóa học
        query = "SELECT * FROM enrollment WHERE student_id = %s AND courses_id = %s"
        values = (student_id, courses_id)
        data = db.fetch(query, values)
        if data:
            return pd.DataFrame(data, columns=columnsEnrollment)
        return pd.DataFrame()
