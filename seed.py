from faker import Faker
from sqlalchemy.orm import Session
from models import Base, Group, Student, Teacher, Subject, Grade
from sqlalchemy import create_engine
import random

engine = create_engine('postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres')
Base.metadata.create_all(engine)

fake = Faker()
with Session(engine) as session:
    # Додавання груп
    groups = [Group(name=f'Group {i}') for i in range(1, 4)]
    session.add_all(groups)

    # Додавання викладачів
    teachers = [Teacher(name=fake.name()) for _ in range(4)]
    session.add_all(teachers)

    # Додавання предметів
    subjects = [Subject(name=fake.word().capitalize(), teacher=random.choice(teachers)) for _ in range(6)]
    session.add_all(subjects)

    # Додавання студентів
    students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(40)]
    session.add_all(students)

    # Додавання оцінок
    grades = [Grade(
        student=random.choice(students),
        subject=random.choice(subjects),
        grade=random.uniform(60, 100),
        date=fake.date_this_year()
    ) for _ in range(800)]
    session.add_all(grades)

    session.commit()