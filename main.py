from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade, SessionLocal

# Створення сесії для роботи з базою даних
session = SessionLocal()

# Створення нового студента
new_student = Student(name="John Doe")
session.add(new_student)
session.commit()

# Читання всіх студентів
students = session.query(Student).all()
for student in students:
    print(student.name)

# Оновлення студента
student_to_update = session.query(Student).filter(Student.id == 1).first()
if student_to_update:
    student_to_update.name = "Jane Doe"
    session.commit()

# Видалення студента
student_to_delete = session.query(Student).filter(Student.id == 1).first()
if student_to_delete:
    session.delete(student_to_delete)
    session.commit()

# Знайти 5 студентів з найбільшим середнім балом
results = session.query(
    Student.name,
    func.round(func.avg(Grade.grade), 2).label('avg_grade')
).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

for result in results:
    print(f"Student: {result.name}, Average Grade: {result.avg_grade}")

# Закрити сесію
session.close()