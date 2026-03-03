import connexion
from swagger_server.models.student import Student
from swagger_server.service.student_service import *
from swagger_server.service.student_service import add, get_by_id, get_all, delete, get_average_grade


def add_student(body=None):  # noqa: E501
    """Add a new student

    Adds an item to the system # noqa: E501

    :param body: Student item to add
    :type body: dict | bytes

    :rtype: float
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
        student_id = add(body)
        return student_id, 200

    return 'Invalid input', 400


def get_student_by_id(student_id):  # noqa: E501
    """Get student by ID

    Returns a single student # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int

    :rtype: Student
    """
    student = get_by_id(student_id)
    if student:
        return student, 200

    return 'Student not found', 404


def get_students():  # noqa: E501
    """Get all students

    Returns a list of all students # noqa: E501

    :rtype: List[Student]
    """
    students = get_all()
    if students:
        return students, 200

    return 'No students found', 404


def delete_student(student_id):  # noqa: E501
    """Deletes a student

    Delete a single student by ID # noqa: E501

    :param student_id: ID of student to delete
    :type student_id: int

    :rtype: None
    """
    result = delete(student_id)
    if result:
        return 'Student deleted successfully', 200

    return 'Student not found', 404


def get_student_average_grade(student_id):  # noqa: E501
    """Get average grade for a student

    Returns the average grade of a student # noqa: E501

    :param student_id: ID of student
    :type student_id: int

    :rtype: float
    """
    average = get_average_grade(student_id)
    if average is not None:
        return average, 200

    return 'Student not found or has no grades', 404