from sqlalchemy import func
from sqlalchemy.orm import Session
from models import Student, Grade  # Припустимо, що у вас є ці моделі

def select_1(session: Session):
    return session.query(
        Student.name, 
        func.round(func.avg(Grade.grade).cast('numeric'), 2).label('avg_grade')
    )\
    .join(Grade, Grade.student_id == Student.id)\
    .group_by(Student.id)\
    .order_by(func.avg(Grade.grade).desc())\
    .limit(5)\
    .all()