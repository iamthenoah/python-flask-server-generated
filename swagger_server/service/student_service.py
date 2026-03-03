import os
import tempfile
from functools import reduce

from tinydb import TinyDB, Query

db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "students.json")
student_db = TinyDB(db_file_path)


def add(student=None):
    queries = []
    query = Query()
    queries.append(query.first_name == student.first_name)
    queries.append(query.last_name == student.last_name)
    query = reduce(lambda a, b: a & b, queries)
    res = student_db.search(query)
    if res:
        return ('already exists', 409)

    doc_id = student_db.insert(student.to_dict())
    student.student_id = doc_id
    return doc_id


def get_all():
    all_students = student_db.all()
    for idx, student in enumerate(all_students, start=1):
        student['student_id'] = idx
    return all_students


def get_by_id(student_id=None, subject=None):
    student = student_db.get(doc_id=int(student_id))
    if not student:
        return None
    student['student_id'] = student_id
    print(student)
    return student


def delete(student_id=None):
    student = student_db.get(doc_id=int(student_id))
    if not student:
        return False
    student_db.remove(doc_ids=[int(student_id)])
    return True


def get_average_grade(student_id=None):
    """Calculate the average grade for a student.
    
    Returns the average grade or None if student not found or has no grades.
    """
    student = student_db.get(doc_id=int(student_id))
    if not student:
        return None
    
    grade_records = student.get('grade_records', [])
    if not grade_records:
        return None
    
    total = sum(record['grade'] for record in grade_records)
    average = total / len(grade_records)
    return round(average, 2)