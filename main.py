from turtle import st
from src.Student import Student
from src.Courses import Courses
from src.Enrollemt import Enrollment
from src.Database import Database

db = Database()
student_main = Student("", "", "", "", "")
courses_main = Courses("", "", 0)
enrollment_main = Enrollment(0, 0)

# student1 = Student(
#     student_name="Trần Văn Hưng",
#     birth_date="2000-01-23",
#     email="tranvanhng01@gmail.com",
#     phone_number="0126547823",
#     address="Hà Nội",
# )
# student2 = Student(
#     student_name="Nguyễn Thị Mai",
#     birth_date="2001-03-15",
#     email="mainguyen01@gmail.com",
#     phone_number="0987654321",
#     address="Hồ Chí Minh",
# )

# student3 = Student(
#     student_name="Lê Văn Phúc",
#     birth_date="2002-07-21",
#     email="phucle02@gmail.com",
#     phone_number="0978541236",
#     address="Đà Nẵng",
# )

# student4 = Student(
#     student_name="Phạm Minh Anh",
#     birth_date="1999-12-30",
#     email="minhanhpham99@gmail.com",
#     phone_number="0912345678",
#     address="Hải Phòng",
# )

# student5 = Student(
#     student_name="Đặng Quốc Bảo",
#     birth_date="2000-05-18",
#     email="quocbao2000@gmail.com",
#     phone_number="0963258741",
#     address="Cần Thơ",
# )

# student6 = Student(
#     student_name="Hoàng Thị Ngọc",
#     birth_date="2003-09-10",
#     email="ngochoang03@gmail.com",
#     phone_number="0932154789",
#     address="Nha Trang",
# )

# student7 = Student(
#     student_name="Bùi Văn Tùng",
#     birth_date="2001-11-25",
#     email="tungbui01@gmail.com",
#     phone_number="0923654785",
#     address="Huế",
# )

# student8 = Student(
#     student_name="Trịnh Thị Hạnh",
#     birth_date="2002-02-28",
#     email="hanhtrinh02@gmail.com",
#     phone_number="0908745632",
#     address="Quảng Ninh",
# )

# student9 = Student(
#     student_name="Ngô Đình Khôi",
#     birth_date="1998-06-07",
#     email="khoingo98@gmail.com",
#     phone_number="0945632187",
#     address="Vũng Tàu",
# )

# student10 = Student(
#     student_name="Dương Văn Lâm",
#     birth_date="2000-08-14",
#     email="lamduong2000@gmail.com",
#     phone_number="0987456321",
#     address="Bình Dương",
# )

# student11 = Student(
#     student_name="Trần Thị Thanh",
#     birth_date="2003-04-05",
#     email="thanhtran03@gmail.com",
#     phone_number="0974123658",
#     address="Đồng Nai",
# )


# student1.addStudent(db)
# student2.addStudent(db)
# student3.addStudent(db)
# student4.addStudent(db)
# student5.addStudent(db)
# student6.addStudent(db)
# student7.addStudent(db)
# student8.addStudent(db)
# student9.addStudent(db)
# student10.addStudent(db)
# student11.addStudent(db)

# courses1 = Courses(
#     courses_name="Toán cao cấp", describe="Môn học về đại số và giải tích", credits=3
# )

# courses2 = Courses(
#     courses_name="Lập trình Python",
#     describe="Giới thiệu về lập trình Python từ cơ bản đến nâng cao",
#     credits=4,
# )

# courses3 = Courses(
#     courses_name="Cấu trúc dữ liệu và Giải thuật",
#     describe="Học về cách tổ chức dữ liệu và các thuật toán phổ biến",
#     credits=4,
# )

# courses4 = Courses(
#     courses_name="Trí tuệ nhân tạo",
#     describe="Giới thiệu về AI, Machine Learning và Deep Learning",
#     credits=3,
# )

# courses5 = Courses(
#     courses_name="Cơ sở dữ liệu",
#     describe="Tìm hiểu về hệ quản trị CSDL như MySQL, PostgreSQL",
#     credits=4,
# )

# courses6 = Courses(
#     courses_name="Lập trình Web",
#     describe="Học về HTML, CSS, JavaScript và các framework như React",
#     credits=3,
# )

# courses7 = Courses(
#     courses_name="Mạng máy tính",
#     describe="Kiến thức về giao thức mạng, bảo mật và truyền dữ liệu",
#     credits=3,
# )

# courses8 = Courses(
#     courses_name="Hệ điều hành",
#     describe="Khám phá cách hoạt động của hệ điều hành như Windows, Linux",
#     credits=3,
# )

# courses9 = Courses(
#     courses_name="Phân tích dữ liệu",
#     describe="Các kỹ thuật phân tích dữ liệu với Pandas, NumPy",
#     credits=4,
# )

# courses10 = Courses(
#     courses_name="Khoa học dữ liệu",
#     describe="Tổng quan về Data Science, xử lý dữ liệu và mô hình ML",
#     credits=4,
# )


# courses1.addCourses(db)
# courses2.addCourses(db)
# courses3.addCourses(db)
# courses4.addCourses(db)
# courses5.addCourses(db)
# courses6.addCourses(db)
# courses7.addCourses(db)
# courses8.addCourses(db)
# courses9.addCourses(db)
# courses10.addCourses(db)


while True:
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
        # them sinh vien
        case "1":

            student_name = input("Nhập tên sinh viên: ")
            birth_date = input("Nhập ngày sinh (YYYY-MM-DD): ")
            email = input("Nhập email: ")
            phone_number = input("Nhập số điện thoại: ")
            address = input("Nhập địa chỉ: ")
            # điều kiện mã sinh viên không trùng

            # tạo đối tượng sinh viên để thêm vào db
            newStudent = Student(
                student_name=student_name,
                birth_date=birth_date,
                email=email,
                phone_number=phone_number,
                address=address,
            )
            # thêm sinh viên vào1
            # db và hiển thị thông báo cho ng dùng
            if newStudent.addStudent(db):
                print(f"Sinh viên: {student_name} đã được thêm vào!")
            else:
                print("Thêm sinh viên thất bại")

        # case xoá thông tin sinh viên
        case "2":
            student_id = int(input("Nhập mã sinh viên cần xóa: "))
            if student_main.removeStudent(db, student_id):
                print(f"Xoá sinh viên có mã: {student_id} thành công!")
            else:
                print(f"Xoá sinh viên ID: {student_id} thất bại")

        # hien thi danh sach sinh vien
        case "4":
            listStudent = student_main.displayAllStudents(db)

            if not listStudent.empty:
                print(listStudent)
                print(
                    f"Hiển thị danh sách thành công, SL: {len(listStudent)} sinh viên."
                )
            else:
                print("Danh sách viên viên rỗng")

        case "3":
            student_id = int(input("Nhập mã sinh viên muốn tìm: "))
            if student_main.checkIdStudent(db, student_id):
                print(student_main.displayOneStudent(db, student_id))
                print("Hiển thị sinh viên cần tìm thành công")
            else:
                print(f"Không tìm thấy sinh viên ID: {student_id}")

        # them khoa hoc moi
        case "5":

            courses_name = input("Nhập tên khóa học: ")
            describe = input("Nhập mô tả thêm cho môn học: ")
            credits = int(input("Nhập số tín chỉ của môn học: "))
            newCourses = Courses(courses_name, describe, credits)
            if newCourses.addCourses(db):
                print(f"Thêm khoá học {courses_name}, {credits} tín chỉ thành công!")
            else:
                print("Thêm khoá học thất bại")

        # xoa khoa hoc
        case "6":
            courses_id = int(input("Nhập mã khóa học cần xóa: "))
            if courses_main.removeCourses(db, courses_id):
                print(f"Đã xoá khoá học ID: {courses_id} thành công!")
            else:
                print(f"Không tồn tại khoá học ID: {courses_id}")

        case "8":
            listCourses = courses_main.displayAllCourses(db)
            if not listCourses.empty:
                print(listCourses)
                print("Đã hiển thị danh sách khoá học thành công")
            else:
                print("Danh sách khoá học trống")

        case "7":
            courses_id = input("Nhập mã khoá học muốn tìm: ")
            if courses_main.checkIdCourses(db, courses_id):
                print(courses_main.displayOneCourses(db, courses_id))
                print("Đã hiển thị khoá học thành công")

            else:
                print("Khoá học không tồn tại, không tìm thấy khoá học")

        # dang ky khoa hoc
        case "9":
            student_id = int(input("Nhập mã sinh viên: "))
            courses_id = int(input("Nhập mã khóa học: "))
            if (not student_main.checkIdStudent(db, student_id)) or (
                not courses_main.checkIdCourses(db, courses_id)
            ):

                print("Mã sinh viên hoặc mã khoá học không tồn tại")
                continue

            newEnrollment = Enrollment(student_id, courses_id)

            if newEnrollment.courseEnrollment(db):
                print(
                    f"Sinh viên: {student_id} đã đăng kí khoá học {courses_id} thành công!"
                )
            else:
                print("Đăng kí khoá học thất bại")

        # xoa dang ky
        case "10":
            enrollment_id = int(input("Nhập mã đăng ký khoá học muốn xoá: "))
            if enrollment_main.removeEnrollment(db, enrollment_id):
                print("Đã xoá đăng ký khoá học thành công!")
            else:
                print("Mã đăng ký khoá học không tồn tại")
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
                print("Lỗi hiênt thị thông tin đăng ký")
        case "12":  # Edit student information
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

        case "13":  # Edit course information
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

        case "0":
            print("Thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
