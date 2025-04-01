import pandas as pd
from src.Database import Database

# Định nghĩa các cột cho DataFrame khi hiển thị danh sách khóa học
columnsCourses = ["coursesId", "coursesName", "describe", "credits"]


class Courses:
    def __init__(self, courses_name, describe, credits, courses_id=None):
        # Hàm khởi tạo lớp Courses với các thuộc tính cơ bản
        self.courses_id = courses_id
        self.courses_name = courses_name
        self.describe = describe
        self.credits = credits

    def checkIdCourses(self, db: Database, courses_id: int) -> bool:
        # Kiểm tra xem mã khóa học có tồn tại trong cơ sở dữ liệu hay không
        query = "SELECT EXISTS(SELECT 1 FROM courses WHERE courses_id = %s)"
        values = (courses_id,)
        checkPoint = db.fetch(query, values)
        return bool(checkPoint[0][0]) if checkPoint else False

    def addCourses(self, db: Database) -> bool:
        # Thêm một khóa học mới vào cơ sở dữ liệu
        query = "INSERT INTO courses(courses_name, course_description, credits) VALUES(%s,%s,%s)"
        values = (self.courses_name, self.describe, self.credits)
        return db.execute(query, values)

    def removeCourses(self, db: Database, courses_id: int) -> bool:
        # Xóa một khóa học khỏi cơ sở dữ liệu dựa trên mã khóa học
        query = "DELETE FROM courses WHERE courses_id = %s"
        values = (courses_id,)
        return db.execute(query, values)

    def displayAllCourses(self, db: Database) -> pd.DataFrame:
        # Hiển thị danh sách tất cả các khóa học trong cơ sở dữ liệu
        query = "SELECT * FROM courses"
        data = db.fetch(query, None)
        if not data:  # Nếu không có dữ liệu, trả về DataFrame rỗng
            return pd.DataFrame()
        return pd.DataFrame(data, columns=columnsCourses)

    def displayOneCourses(self, db: Database, courses_id: int) -> pd.DataFrame:
        # Hiển thị thông tin chi tiết của một khóa học dựa trên mã khóa học
        query = "SELECT * FROM courses WHERE courses_id = %s"
        values = (courses_id,)
        data = db.fetch(query, values)
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data, columns=columnsCourses)

    def editCourses(
        self,
        db: Database,
        courses_id: int,
        courses_name: str,
        describe: str,
        credits: int,
    ) -> bool:
        # Sửa thông tin của một khóa học dựa trên mã khóa học
        updates = []
        values = []
        if courses_name:
            updates.append("courses_name = %s")
            values.append(courses_name)
        if describe:
            updates.append("course_description = %s")
            values.append(describe)
        if credits is not None:
            updates.append("credits = %s")
            values.append(credits)
        if not updates:  # Nếu không có thông tin nào để cập nhật, trả về False
            return False
        query = f"UPDATE courses SET {', '.join(updates)} WHERE courses_id = %s"
        values.append(courses_id)
        return db.execute(query, tuple(values))
