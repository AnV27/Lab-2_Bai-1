import pandas as pd
class Courses:
    def __init__(self, db):
        self.db = db 
    
    def themKH(self,ma_khoa_hoc,ten_khoa_hoc, mo_ta,so_tin_chi):
        query = "INSERT INTO courses VALUES(%s,%s,%s,%s)"
        values = (ma_khoa_hoc,ten_khoa_hoc, mo_ta,so_tin_chi)
        try:
            self.db.execute(query, values)
            return f"Da them khoa hoc: {ma_khoa_hoc}, thanh cong!"
        
        except Exception as e:
            return f"ERROR: {e}"
        

    def xoaKH(self,ma_khoa_hoc):
        query_del = "DELETE FROM courses WHERE ma_khoa_hoc = %s"
        query_search = "SELECT * FROM courses WHERE ma_khoa_hoc = %s"
        values = (ma_khoa_hoc,)

        if not self.db.fetch(query_search, values):
            return f"Ma hoc hoc: {ma_khoa_hoc}, khong co trong danh sach!"
        
        self.db.execute(query_del, values)
        return f"Da xoa ma khoa hoc {ma_khoa_hoc}, thanh cong!"
    
    def timKH(self, ma_khoa_hoc):
        query = "SELECT * FROM courses WHERE ma_khoa_hoc = %s"
        values = (ma_khoa_hoc,)
        
        khoaHoc = self.db.fetch(query, values)
        if not khoaHoc:
            return f"Khong tim thay khoa hoc {ma_khoa_hoc}!"
        print(f"Da tim thay khoa hoc, MaKHoa = {ma_khoa_hoc}")
        return pd.DataFrame(khoaHoc,columns = ['MaKhoaHoc','TenKhoaHoc','MoTa','SoTinChi']).set_index('MaKhoaHoc')