'''Hoan thanh'''
from students import Students
from courses import Courses
from datetime import datetime
import pandas as pd

class Enrollment:
    ma_dang_ky = '99' # ma so khi dang ki mon hoc thanh cong
    def __init__(self,db, students, courses):
        self.db = db 
        self.students = students 
        self.courses = courses 
        
    # update ma so moi khi dang ki mon hoc thanh cong
    @classmethod 
    def generate_MaDK(cls):
        cls.ma_dang_ky = str(int(cls.ma_dang_ky) + 1)  # tang gia tri
        return cls.ma_dang_ky  # tra ve gia tri moi
    
    # dang ky mon hoc
    def DKHocPhan(self, ma_sinh_vien, ma_khoa_hoc):

        # kiem tra mssv co trong db khong
        check_MSSV = self.db.fetch("SELECT ma_sinh_vien FROM students WHERE ma_sinh_vien = %s", values = (ma_sinh_vien,))
        # kiem tra maKH co trong bd khong
        check_MaKH = self.db.fetch("SELECT ma_khoa_hoc FROM courses WHERE ma_khoa_hoc = %s", values = (ma_khoa_hoc,))
        
        if (not check_MaKH) or (not check_MSSV):
            return "MSSV hoac Ma khoa hoc khong ton tai!"

        # lay ngay hien tai de dua vao db
        ngay_dang_ky = datetime.now().date()

        # truy van de dua data dang ky vao data base
        query = "INSERT INTO enrollment(ma_dang_ky, ma_sinh_vien, ma_khoa_hoc, ngay_dang_ky) VALUES(%s,%s,%s,%s)"
        self.db.execute(query, values = (Enrollment.generate_MaDK(),ma_sinh_vien,ma_khoa_hoc,ngay_dang_ky))
        return "Da dang ky mon hoc thanh cong"

    def xoaDK(self, ma_dang_ky):
        # cau truy vap trong SQL
        query = "DELETE FROM enrollment WHERE ma_dang_ky = %s"
        query_check_maDK = "SELECT ma_dang_ky FROM enrollment WHERE ma_dang_ky = %s"
        if not self.db.fetch(query_check_maDK,(ma_dang_ky,)):
            return "Khong ton tai ma dang ky!"
        # ket qua truy van
        self.db.execute(query, (ma_dang_ky,))
        return f"Xoa dang ky hoc phan {ma_dang_ky} thanh cong!"

        
    def timDK(self,ma_sinh_vien, ma_khoa_hoc):
        query = "SELECT * FROM enrollment WHERE ma_sinh_vien = %s AND ma_khoa_hoc = %s"
        res = self.db.fetch(query,(ma_sinh_vien, ma_khoa_hoc,))
        if not res:
            return "Khong tim thay cac dang ky hoc phan!"
        print(f"Da tim thay khoa hoc")
        df = pd.DataFrame(res, columns = ['ma_dang_ky','ma_sinh_vien','ma_khoa_hoc','ngay_dang_ky'])
        return df