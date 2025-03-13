from students import Students
from courses import Courses
from datetime import datetime
import random as rd

class Enrollment:
    def __init__(self,db, students, courses):
        self.db = db 
        self.students = students 
        self.courses = courses 


    def DKHocPhan(self, ma_sinh_vien, ma_khoa_hoc):

        # kiem tra thu tham so co nam trong db hay khong
        check_MSSV = self.db.fetch("SELECT ma_sinh_vien FROM students WHERE ma_sinh_vien = %s", values = (ma_sinh_vien,))
        check_MaKH = self.db.fetch("SELECT ma_khoa_hoc FROM courses WHERE ma_khoa_hoc = %s", values = (ma_khoa_hoc,))
        
        if not check_MaKH:
            return "Ma khoa hoc khong ton tai!"
        elif not check_MSSV:
            return "MSSV khong ton tai!"
        
        ma_dang_ki = rd.randint(100, 999)
        ngay_dang_ky = datetime.now().date()
        query = "INSERT INTO enrollment(ma_dang_ky, ma_sinh_vien, ma_khoa_hoc, ngay_dang_ky) VALUES(%s,%s,%s,%s)"
        self.db.execute(query, values = (ma_dang_ki,ma_sinh_vien,ma_khoa_hoc,ngay_dang_ky))
        return "Da dang ky mon hoc thanh cong"

        


