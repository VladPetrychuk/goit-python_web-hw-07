import argparse
from sqlalchemy.orm import Session
from models import Teacher, Group, Subject, Student
from sqlalchemy import create_engine

DATABASE_URL = 'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres'
engine = create_engine(DATABASE_URL)

def list_teachers(session: Session):
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f'{teacher.id}: {teacher.name}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', '-a', required=True, choices=['list'])
    parser.add_argument('--model', '-m', required=True, choices=['Teacher'])
    args = parser.parse_args()

    with Session(engine) as session:
        if args.action == 'list' and args.model == 'Teacher':
            list_teachers(session)

if __name__ == '__main__':
    main()