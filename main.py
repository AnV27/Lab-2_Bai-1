''' 10-03-2005
    Đã kết nối db thành công
    1. thêm sinh viên vào db thành công
    2. xoá sinh viên trong db thành công
    11-03-2025
    1. Thêm, xoá, tìm, danh sách của SINH VIÊN hoàn thành
    2. Thêm, xoá, tìm KHOÁ HỌC hoàn thành, Lưu ý: Đổi thông báo từ mãKH -> tên khoá học, dễ đọc TB
    '''

from database import *
from students import *
from courses import *
DatabaseName = "Lab2"
HostName = "localhost"
Port = 5432
UserName = "postgres"
Password = 2785

db = Database(host = HostName, user = UserName, password = Password, port = Port, dbname = DatabaseName)
SinhVienA = Students(db)
KhoaHoc = Courses(db)



# print(KhoaHoc.themKH('2','Python','muoi diem',3))
print(KhoaHoc.xoaKH('1'))
# SinhVienA.themSinhVien("1", "Nguyen Van A", "10-05-2002", "nguyenvana@example.com", "0987654321", "Duong Le Loi, Quan 1, TPHCM")
# SinhVienA.themSinhVien("2", "Tran Thi B", "15-09-2003", "tranthib@example.com", "0978123456", "Duong Tran Hung Dao, Ha Noi")
# SinhVienA.themSinhVien("3", "Le Van C", "20-07-2003", "levanc@example.com", "0965123789", "Duong Nguyen Hue, Da Nang")
# SinhVienA.themSinhVien("4", "Pham Hong D", "25-12-2000", "phamhongd@example.com", "0956789123", "Duong Vo Thi Sau, Can Tho")


