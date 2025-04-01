from src.Database import Database
import pandas as pd

columnsEnrollment = ["enrollmentID", "studentID", "coursesID", "enrollmentDate"]


class Enrollment:

    def __init__(
        self, student_id, courses_id, enrollment_date=None, enrollment_id=None
    ):

        self.student_id = student_id
        self.courses_id = courses_id
        self.enrollment_date = enrollment_date
        self.enrollment_id = enrollment_id

    def checkIdEnrollment(self, db: Database, enrollment_id: int) -> bool:
        query = "SELECT EXISTS(SELECT 1 FROM enrollment WHERE enrollment_id = %s)"
        values = (enrollment_id,)
        checkPoint = db.fetch(query, values)
        return bool(checkPoint[0][0]) if checkPoint else False

    # dang ky mon hoc
    def courseEnrollment(self, db: Database) -> bool:
        query = "INSERT INTO enrollment(student_id, courses_id) VALUES(%s, %s)"
        values = (self.student_id, self.courses_id)
        return db.execute(query, values)

    def removeEnrollment(self, db: Database, enrollment_id: int) -> bool:

        if self.checkIdEnrollment(db, enrollment_id):

            query = "DELETE FROM enrollment WHERE enrollment_id = %s"
            values = (enrollment_id,)

            if db.execute(query, values):
                return True

        return False

    def displayAllEnrollment(self, db) -> pd.DataFrame:
        query = "SELECT * FROM enrollment"
        values = None

        data = db.fetch(query, values)

        if not data:
            return pd.DataFrame()

        df = pd.DataFrame(data, columns=columnsEnrollment)
        return df

    def displayOneEnrollment(
        self, db: Database, student_id: int, courses_id: int
    ) -> pd.DataFrame:

        query = "SELECT * FROM enrollment WHERE student_id = %s AND courses_id = %s"
        values = (student_id, courses_id)

        data = db.fetch(query, values)
        if data:
            df = pd.DataFrame(data, columns=columnsEnrollment)

            return df

        return pd.DataFrame()
