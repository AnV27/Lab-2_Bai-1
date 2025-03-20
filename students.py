import pandas as pd 
from datetime import datetime
class Students:
    # khoi tao constructor
    def __init__(self, db):
        self.db = db 

    def themSV(self, ma, ten, ngaySinh,email,soDienThoai, diaChi):
        ngaySinh = datetime.strptime(ngaySinh, "%Y-%m-%d").date() # chuyen tu str ve date
        # cau lenh de them du lieu vao table
        query = "INSERT INTO students(ma_sinh_vien, ten_sinh_vien, ngay_sinh,email,so_dien_thoai, dia_chi) VALUES(%s,%s,%s,%s,%s,%s)"
        values = (ma,ten, ngaySinh,email, soDienThoai, diaChi)
        try:
            self.db.execute(query, values)
            return f"Da them MSSV: {ma} vao danh sach sinh vien!"
        
        except Exception as e:
            return f"ERROR: {e}"
            

    def xoaSV(self, ma_sinh_vien):
        # cau lenh de xoa du lieu vao table
        query = " DELETE FROM students WHERE ma_sinh_vien = %s"
        try:
            self.db.execute(query,values = (ma_sinh_vien,)) # ham de truy van 
            return f"MSSV: {ma_sinh_vien}, Da xoa thanh cong!"
        
        except Exception as e:
            return f"ERROR: {e}"
    

    def danhSachSV(self):
        query = "SELECT * FROM students"
        listSinhVien = self.db.fetch(query)
        if not listSinhVien:
            return "Danh sach RONG"
        return pd.DataFrame(listSinhVien, columns = ['MSSV','HoTen','NgaySinh','Email','SDT','DiaChi'])
    
    def timSV(self,ma_sinh_vien):
        query = "SELECT * FROM students WHERE ma_sinh_vien = %s"
        values = (ma_sinh_vien,)
        sinh_vien = self.db.fetch(query, values)

        if not sinh_vien:
            return f"MSSV: {ma_sinh_vien}, khong ton tai!"
        
        print(f"Tim thay MSSV: {ma_sinh_vien}")
        return pd.DataFrame(sinh_vien,columns = ['MSSV','HoTen','NgaySinh','Email','SDT','DiaChi'])


    '''can cap nhat chuc nang'''
    def suaSV(self,ma_sinh_vien:str):
        if not self.timKiemSinhVien(ma_sinh_vien):
            print("Khong co sinh vien trong danh sach!")
            return
        pass

      
    
        

        
    
        






    
