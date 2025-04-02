# Nhập các thư viện cần thiết và các lớp từ các module khác
from src.Student import Student
from src.Courses import Courses
from src.Enrollemt import Enrollment
from src.Database import Database

# Khởi tạo đối tượng cơ sở dữ liệu và các đối tượng chính cho sinh viên, khóa học, và đăng ký

db = Database() 
student_main = Student("", "", "", "", "")
courses_main = Courses("", "", 0)
enrollment_main = Enrollment(0, 0)

# Dữ liệu mẫu cho sinh viên
# listStudent = [
#     Student("Trần Văn Hưng", "2000-01-23", "tranvanhng01@gmail.com", "0126547823", "Hà Nội"),
#     Student("Nguyễn Thị Mai", "2001-03-15", "mainguyen01@gmail.com", "0987654321", "Hồ Chí Minh"),
#     Student("Lê Văn Phúc", "2002-07-21", "phucle02@gmail.com", "0978541236", "Đà Nẵng"),
#     Student("Phạm Minh Anh", "1999-12-30", "minhanhpham99@gmail.com", "0912345678", "Hải Phòng"),
#     Student("Đặng Quốc Bảo", "2000-05-18", "quocbao2000@gmail.com", "0963258741", "Cần Thơ"),
#     Student("Hoàng Thị Ngọc", "2003-09-10", "ngochoang03@gmail.com", "0932154789", "Nha Trang"),
#     Student("Bùi Văn Tùng", "2001-11-25", "tungbui01@gmail.com", "0923654785", "Huế"),
#     Student("Trịnh Thị Hạnh", "2002-02-28", "hanhtrinh02@gmail.com", "0908745632", "Quảng Ninh"),
#     Student("Ngô Đình Khôi", "1998-06-07", "khoingo98@gmail.com", "0945632187", "Vũng Tàu"),
#     Student("Dương Văn Lâm", "2000-08-14", "lamduong2000@gmail.com", "0987456321", "Bình Dương"),
#     Student("Trần Thị Thanh", "2003-04-05", "thanhtran03@gmail.com", "0974123658", "Đồng Nai"),
# ]

# for _ in listStudent:
#     if _.addStudent(db):
#         print(f"Thêm sinh viên {_.student_name} thành công!")

# Dữ liệu mẫu cho khoá học
# listCourses = [
#     Courses("Toán cao cấp", "Môn học về đại số và giải tích", 3),
#     Courses("Lập trình Python", "Giới thiệu về lập trình Python từ cơ bản đến nâng cao", 4),
#     Courses("Cấu trúc dữ liệu và Giải thuật", "Học về cách tổ chức dữ liệu và các thuật toán phổ biến", 4),
#     Courses("Trí tuệ nhân tạo", "Giới thiệu về AI, Machine Learning và Deep Learning", 3),
#     Courses("Cơ sở dữ liệu", "Tìm hiểu về hệ quản trị CSDL như MySQL, PostgreSQL", 4),
#     Courses("Lập trình Web", "Học về HTML, CSS, JavaScript và các framework như React", 3),
#     Courses("Mạng máy tính", "Kiến thức về giao thức mạng, bảo mật và truyền dữ liệu", 3),
#     Courses("Hệ điều hành", "Khám phá cách hoạt động của hệ điều hành như Windows, Linux", 3),
#     Courses("Phân tích dữ liệu", "Các kỹ thuật phân tích dữ liệu với Pandas, NumPy", 4),
#     Courses("Khoa học dữ liệu", "Tổng quan về Data Science, xử lý dữ liệu và mô hình ML", 4),
# ]

# for _ in listCourses:
#     if _.addCourses(db):
#         print(f"Thêm khoá học {_.courses_name} thành công!")

# Vòng lặp chính để hiển thị menu và xử lý các lựa chọn của người dùng
while True:
    # Hiển thị menu chính của hệ thống quản lý
    print("\n=== QUẢN LÝ HỆ THỐNG ===")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Tìm kiếm sinh viên")
    print("4. Hiển thị danh sách sinh viên")
    print("5. Thêm khóa học")
    print("6. Xóa khóa học")
    print("7. Tìm kiếm khoá học")
    print("8. Hiển thị danh sách khóa học")
    print("9. Đăng ký học phần")
    print("10. Huỷ đăng ký học phần")
    print("11. Tìm đăng ký theo mã sinh viên và mã khoá học")
    print("12. Sửa thông tin sinh viên")
    print("13. Sửa thông tin khoá học")
    print("0. Thoát")
    print("========================")
    choice = input("Nhập lựa chọn: ")

    match choice:
        # Thêm sinh viên mới
        case "1":
            # Nhập thông tin sinh viên từ người dùng
            student_name = input("Nhập tên sinh viên: ")
            birth_date = input("Nhập ngày sinh (YYYY-MM-DD): ")
            email = input("Nhập email: ")
            phone_number = input("Nhập số điện thoại: ")
            address = input("Nhập địa chỉ: ")

            # Tạo đối tượng sinh viên và thêm vào cơ sở dữ liệu
            newStudent = Student(
                student_name=student_name,
                birth_date=birth_date,
                email=email,
                phone_number=phone_number,
                address=address,
            )
            # Kiểm tra và thông báo kết quả thêm sinh viên
            if newStudent.addStudent(db):
                print(f"Sinh viên: {student_name} đã được thêm vào!")
            else:
                print("Thêm sinh viên thất bại")

        # Xóa sinh viên theo mã sinh viên
        case "2":
            student_id = int(input("Nhập mã sinh viên cần xóa: "))
            if student_main.removeStudent(db, student_id):
                print(f"Xoá sinh viên có mã: {student_id} thành công!")
            else:
                print(f"Xoá sinh viên ID: {student_id} thất bại")

        # Hiển thị danh sách sinh viên
        case "4":
            listStudent = student_main.displayAllStudents(db)
            if not listStudent.empty:
                print(listStudent)
                print(
                    f"Hiển thị danh sách thành công, SL: {len(listStudent)} sinh viên."
                )
            else:
                print("Danh sách sinh viên rỗng")

        # Tìm kiếm sinh viên theo mã
        case "3":
            student_id = int(input("Nhập mã sinh viên muốn tìm: "))
            if student_main.checkIdStudent(db, student_id):
                print(student_main.displayOneStudent(db, student_id))
                print("Hiển thị sinh viên cần tìm thành công")
            else:
                print(f"Không tìm thấy sinh viên ID: {student_id}")

        # Thêm khóa học mới
        case "5":
            # Nhập thông tin khóa học từ người dùng
            courses_name = input("Nhập tên khóa học: ")
            describe = input("Nhập mô tả thêm cho môn học: ")
            credits = int(input("Nhập số tín chỉ của môn học: "))
            newCourses = Courses(courses_name, describe, credits)

            # Kiểm tra và thông báo kết quả thêm khóa học
            if newCourses.addCourses(db):
                print(f"Thêm khoá học {courses_name}, {credits} tín chỉ thành công!")
            else:
                print("Thêm khoá học thất bại")

        # Xóa khóa học theo mã
        case "6":
            courses_id = int(input("Nhập mã khóa học cần xóa: "))
            if courses_main.removeCourses(db, courses_id):
                print(f"Đã xoá khoá học ID: {courses_id} thành công!")
            else:
                print(f"Không tồn tại khoá học ID: {courses_id}")

        # Hiển thị danh sách khóa học
        case "8":
            listCourses = courses_main.displayAllCourses(db)
            if not listCourses.empty:
                print(listCourses)
                print("Đã hiển thị danh sách khoá học thành công")
            else:
                print("Danh sách khoá học trống")

        # Tìm kiếm khóa học theo mã
        case "7":
            courses_id = input("Nhập mã khoá học muốn tìm: ")
            if courses_main.checkIdCourses(db, courses_id):
                print(courses_main.displayOneCourses(db, courses_id))
                print("Đã hiển thị khoá học thành công")
            else:
                print("Khoá học không tồn tại, không tìm thấy khoá học")

        # Đăng ký khóa học cho sinh viên
        case "9":
            student_id = int(input("Nhập mã sinh viên: "))
            courses_id = int(input("Nhập mã khóa học: "))

            # Kiểm tra mã sinh viên và mã khóa học có tồn tại không
            if (not student_main.checkIdStudent(db, student_id)) or (
                not courses_main.checkIdCourses(db, courses_id)
            ):
                print("Mã sinh viên hoặc mã khoá học không tồn tại")
                continue

            # Tạo đối tượng đăng ký và thêm vào cơ sở dữ liệu
            newEnrollment = Enrollment(student_id, courses_id)
            if newEnrollment.courseEnrollment(db):
                print(
                    f"Sinh viên: {student_id} đã đăng kí khoá học {courses_id} thành công!"
                )
            else:
                print("Đăng kí khoá học thất bại")

        # Xóa đăng ký khóa học
        case "10":
            enrollment_id = int(input("Nhập mã đăng ký khoá học muốn xoá: "))
            if enrollment_main.removeEnrollment(db, enrollment_id):
                print("Đã xoá đăng ký khoá học thành công!")
            else:
                print("Mã đăng ký khoá học không tồn tại")

        # Tìm đăng ký theo mã sinh viên và mã khóa học
        case "11":
            student_id = int(input("Nhập mã sinh viên cần tìm: "))
            courses_id = int(input("Nhập mã khoá học cần tìm: "))
            if (not student_main.checkIdStudent(db, student_id)) or (
                not courses_main.checkIdCourses(db, courses_id)
            ):
                print("Mã sinh viên hoặc mã khoá học không tồn tại")
                continue

            result = enrollment_main.displayOneEnrollment(db, student_id, courses_id)
            if not result.empty:
                print(result)
                print("Hiển thị thông tin đăng ký thành công!")
            else:
                print("Lỗi hiển thị thông tin đăng ký")

        # Sửa thông tin sinh viên
        case "12":
            student_id = int(input("Nhập mã sinh viên cần sửa: "))
            if student_main.checkIdStudent(db, student_id):
                print("Nhập thông tin mới (để trống nếu không muốn thay đổi):")
                student_name = input("Tên sinh viên: ")
                birth_date = input("Ngày sinh (YYYY-MM-DD): ")
                email = input("Email: ")
                phone_number = input("Số điện thoại: ")
                address = input("Địa chỉ: ")
                if student_main.editStudent(
                    db,
                    student_id,
                    student_name,
                    birth_date,
                    email,
                    phone_number,
                    address,
                ):
                    print(f"Sửa thông tin sinh viên ID: {student_id} thành công!")
                else:
                    print(f"Sửa thông tin sinh viên ID: {student_id} thất bại!")
            else:
                print(f"Không tìm thấy sinh viên ID: {student_id}")

        # Sửa thông tin khóa học
        case "13":
            courses_id = int(input("Nhập mã khoá học cần sửa: "))
            if courses_main.checkIdCourses(db, courses_id):
                print("Nhập thông tin mới (để trống nếu không muốn thay đổi):")
                courses_name = input("Tên khoá học: ")
                describe = input("Mô tả: ")
                credits = input("Số tín chỉ: ")
                credits = int(credits) if credits else None
                if courses_main.editCourses(
                    db, courses_id, courses_name, describe, credits
                ):
                    print(f"Sửa thông tin khoá học ID: {courses_id} thành công!")
                else:
                    print(f"Sửa thông tin khoá học ID: {courses_id} thất bại!")
            else:
                print(f"Không tìm thấy khoá học ID: {courses_id}")

        # Thoát chương trình
        case "0":
            print("Thoát chương trình!")
            break

        # Lựa chọn không hợp lệ
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
