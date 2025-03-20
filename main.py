''' 10-03-2005
    Đã kết nối db thành công
    1. thêm sinh viên vào db thành công
    2. xoá sinh viên trong db thành công
    11-03-2025
    1. Thêm, xoá, tìm, danh sách của SINH VIÊN hoàn thành
    2. Thêm, xoá, tìm KHOÁ HỌC hoàn thành, Lưu ý: Đổi thông báo từ mãKH -> tên khoá học, dễ đọc TB
    13-03-2025
    Tương đối xong students và courses (chưa có chức năng sửa)
    Cần hoàn thành enrollment (Đã xong đăng ký)
    14-03-2025
    Hoàn thành class enrollment
    '''

from database import *
from students import *
from courses import *
from enrollment import *
DatabaseName = "Lab2"
HostName = "localhost"
Port = 5432
UserName = "postgres"
Password = 2785

dataBase = Database(host = HostName, user = UserName, password = Password, port = Port, dbname = DatabaseName)
SinhVien = Students(dataBase)
KhoaHoc = Courses(dataBase)
DangKyMon = Enrollment(dataBase,SinhVien, KhoaHoc)

while True:
    print("\n=== QUẢN LÝ HỆ THỐNG ===")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Hiển thị danh sách sinh viên")
    print("4. Thêm khóa học")
    print("5. Xóa khóa học")
    print("6. Hiển thị danh sách khóa học")
    print("7. Đăng ký học phần")
    print("0. Thoát")

    choice = input("Nhập lựa chọn: ")

    match choice:
        # them sinh vien
        case "1":
            ma_sv = input("Nhập mã sinh viên: ")
            ten_sv = input("Nhập tên sinh viên: ")
            ngay_sinh = input("Nhập ngày sinh (YYYY-MM-DD): ")
            email = input("Nhập email: ")
            sdt = input("Nhập số điện thoại: ")
            dia_chi = input("Nhập địa chỉ: ")
            print(SinhVien.themSV(ma_sv, ten_sv, ngay_sinh, email, sdt, dia_chi))
        # xoa sinh vien
        case "2":
            ma_sv = input("Nhập mã sinh viên cần xóa: ")
            print(SinhVien.xoaSV(ma_sv))
        # hien thi danh sach sinh vien
        case "3":
            print(SinhVien.danhSachSV())
            # tim sinh vien
        case "4":
            ma_sinh_vien = input("Nhap ma so sinh vien muon tim: ")
            print(SinhVien.timSV(ma_sinh_vien=ma_sinh_vien))
        # them khoa hoc moi
        case "5":
            ma_kh = input("Nhập mã khóa học: ")
            ten_kh = input("Nhập tên khóa học: ")
            mo_ta = input("Nhap mo ta: ")
            so_tin = int(input("Nhap so tin chi: "))
            print(KhoaHoc.themKH(ma_kh, ten_kh, mo_ta, so_tin))
        # xoa khoa hoc 
        case "6":
            ma_kh = input("Nhập mã khóa học cần xóa: ")
            print(KhoaHoc.xoaKH(ma_kh))
        # hien thi danh sach khoa hoc
        case "7":
            print(KhoaHoc.hienThiKH())
        # tim khoa hoc
        case "8":
            ma_khoa_hoc = input("Nhap ma khoa hoc muon tim: ")
            print(KhoaHoc.timKH(ma_khoa_hoc))
        # dang ky khoa hoc 
        case "9":
            ma_sv = input("Nhập mã sinh viên: ")
            ma_kh = input("Nhập mã khóa học: ")
            print(DangKyMon.DKHocPhan(ma_sv, ma_kh))
        # xoa dang ky
        case "10":
            ma_dang_ky = input("Nhap ma dang ky: ")
            print(DangKyMon.xoaDK(ma_dang_ky))
        case "11":
            pass 
        # tim dang ky
        case "12":
            mssv = input("Nhap ma sinh vien: ")
            ma_khoa = input("Nhap ma khoa hoc: ")
            print(DangKyMon.timDK(ma_sinh_vien=mssv,ma_khoa_hoc=ma_khoa))
        case "0":
            print("Thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

        #    ✅1. nhap sinh vien    ✅2. xoa sinh vien   ✅3. danh sach sinh vien   ✅4. tim kiem sinh vien
        #    ✅5. Tao khoa hoc      ✅6. Xoa khoa hoc    ✅7. danh sach khoa        ✅8. tim kiem khoa    
        #    ✅9. Dang ky           ✅10. xoa dang ky    11. pass                    ✅12. tim dang ky    

    # ✅
    # ❌