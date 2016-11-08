import unittest
import datetime
from student import Student


class TestStudent(unittest.TestCase):
    """Validate the behavior of the class"""

    def test_student_to_string(self):
        s = Student(1, "Salim", "Fadhley", "male", datetime.date(1975,4,4))
        self.assertEqual(str(s), 'ID: 1, name: Salim Fadhley, gender: male, dob: 1975-04-04')

    def test_that_invalid_dates_are_rejected(self):
        with self.assertRaises(TypeError):
            Student(1, "Salim", "Fadhley", "male", "xxxx")

    def test_that_invalid_genders_are_rejected(self):
        with self.assertRaises(ValueError):
            Student(1, "Salim", "Fadhley", "dunno", datetime.date(1975,4,4))