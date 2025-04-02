CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(255),
    birth_date DATE,
    email VARCHAR(255),
    phone_number VARCHAR(15),
    address VARCHAR(255)
);

CREATE TABLE courses (
    courses_id SERIAL PRIMARY KEY,
    courses_name VARCHAR(255),
    course_description VARCHAR(255),
    credits INTEGER
);

CREATE TABLE enrollment (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    courses_id INTEGER NOT NULL,
    -- Để mặc định là ngày hiện tại
    enrollment_date DATE DEFAULT CURRENT_DATE,
    -- Khoá phụ
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    CONSTRAINT fk_courses FOREIGN KEY (courses_id) REFERENCES courses(courses_id) ON DELETE CASCADE
);