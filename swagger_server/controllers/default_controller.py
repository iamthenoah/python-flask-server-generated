import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util


def add_student(body):  # noqa: E501
    """Add a new student

    Adds a student item to the system # noqa: E501

    :param body: Student item to add
    :type body: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_student(student_id):  # noqa: E501
    """Deletes a student

    Delete a single student by ID # noqa: E501

    :param student_id: ID of student to delete
    :type student_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_student_by_id(student_id):  # noqa: E501
    """Get student by ID

    Returns a single student # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int

    :rtype: Student
    """
    return 'do some magic!'


def get_students():  # noqa: E501
    """Get all students

    Returns a list of all students # noqa: E501


    :rtype: List[Student]
    """
    return 'do some magic!'
