import pandas as pd
from src.Database import Database
from datetime import datetime


columnsStudent = [
    "StudentID",
    "StudentName",
    "BirthDate",
    "Email",
    "PhoneNumber",
    "Address",
]


class Student:
    # khoi tao constructor
    def __init__(
        self,
        student_name: str,
        birth_date: str,
        email: str,
        phone_number: str,
        address: str,
        student_id: int = None,
    ):
        self.student_id = student_id
        self.student_name = student_name
        self.birth_date = birth_date
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def checkIdStudent(self, db: Database, student_id: int) -> bool:

        query = "SELECT EXISTS(SELECT 1 FROM student WHERE student_id = %s)"
        values = (student_id,)

        checkPoint = db.fetch(query, values)
        return bool(checkPoint[0][0]) if checkPoint else False

    def addStudent(self, db: Database) -> bool:

        self.birth_date = datetime.strptime(
            self.birth_date, "%Y-%m-%d"
        ).date()  # chuyen tu str ve date
        # cau lenh de them du lieu vao table

        query = "INSERT INTO student (student_name, birth_date, email, phone_number, address) VALUES(%s, %s, %s, %s, %s)"
        values = (
            self.student_name,
            self.birth_date,
            self.email,
            self.phone_number,
            self.address,
        )

        if db.execute(query, values):
            return True

        return False

    def removeStudent(self, db: Database, student_id: int) -> bool:
        if self.checkIdStudent(db, student_id):

            query = "DELETE FROM student WHERE student_id = %s"
            values = (student_id,)

            if db.execute(query, values):
                return True

        # truong hop khong tim thay student_id thi out func -> return False
        return False

    def displayAllStudents(self, db: Database) -> pd.DataFrame:

        query = "SELECT * FROM student"
        values = None

        data = db.fetch(query, values)

        if not data:
            # tra ve empty dataframe neu khong co du lieu trong db
            return pd.DataFrame()

        df = pd.DataFrame(data, columns=columnsStudent)

        return df

    def displayOneStudent(self, db: Database, student_id: int) -> pd.DataFrame:

        if not self.checkIdStudent(db, student_id):
            # tra ve empty dataframe neu khong co du lieu trong db
            return pd.DataFrame()

        query = "SELECT * FROM student WHERE student_id = %s"
        values = (student_id,)

        data = db.fetch(query, values)
        # tra ve kieu dataframe de ng dung truc quan hoa (dang bang)
        df = pd.DataFrame(data, columns=columnsStudent)

        return df

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
