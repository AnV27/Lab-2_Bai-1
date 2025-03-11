from students import Students
from courses import Courses
import database 
class Enrollment:
    def __init__(self, ma_dang_ky, Students, Courses, ngay_dang_ky):
        self.ma_dang_ky = ma_dang_ky
        self.Students = Students
        self.Courses = Courses 
        self.ngay_dang_ky = ngay_dang_ky 