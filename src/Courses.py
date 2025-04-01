import pandas as pd
from src.Database import Database


columnsCourses = ["coursesId", "coursesName", "describe", "credits"]


class Courses:
    def __init__(self, courses_name, describe, credits, courses_id=None):
        self.courses_id = courses_id
        self.courses_name = courses_name
        self.describe = describe
        self.credits = credits

    def checkIdCourses(self, db: Database, courses_id: int) -> bool:
        query = "SELECT EXISTS(SELECT 1 FROM courses WHERE courses_id = %s)"
        values = (courses_id,)
        checkPoint = db.fetch(query, values)
        return bool(checkPoint[0][0]) if checkPoint else False

    def addCourses(self, db: Database) -> bool:
        query = "INSERT INTO courses(courses_name, course_description, credits) VALUES(%s,%s,%s)"
        values = (self.courses_name, self.describe, self.credits)
        if db.execute(query, values):
            return True
        else:
            return False

    def removeCourses(self, db: Database, courses_id: int) -> bool:
        query = "DELETE FROM courses WHERE courses_id = %s"
        values = (courses_id,)

        if db.execute(query, values):
            return True

        return False

    def displayAllCourses(self, db: Database) -> pd.DataFrame:
        query = "SELECT * FROM courses"
        values = None
        data = db.fetch(query, values)

        if not data:  # danh sach khong co du lieu
            return pd.DataFrame()

        df = pd.DataFrame(data, columns=columnsCourses)
        return df

    def displayOneCourses(self, db: Database, courses_id: int) -> pd.DataFrame:
        query = "SELECT * FROM courses WHERE courses_id = %s"
        values = (courses_id,)

        data = db.fetch(query, values)
        if not data:
            return pd.DataFrame()

        df = pd.DataFrame(data, columns=columnsCourses)
        return df

    def editCourses(
        self,
        db: Database,
        courses_id: int,
        courses_name: str,
        describe: str,
        credits: int,
    ) -> bool:
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
        if not updates:
            return False
        query = f"UPDATE courses SET {', '.join(updates)} WHERE courses_id = %s"
        values.append(courses_id)
        return db.execute(query, tuple(values))
