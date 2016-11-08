import datetime


class Student:
    """Represents a student at a school."""

    def __init__(self, student_id, first_name, last_name, gender, dob):
        if not isinstance(dob, datetime.date):
            raise TypeError("Invalid date")

        if not gender in ["male", "female"]:
            raise ValueError("Invalid gender")

        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.dob = dob

    def __str__(self):
        '''Convert this object to a string'''
        return 'ID: {student_id}, name: {first_name} {last_name}, gender: {gender}, dob: {dob}'.format(**self.__dict__)

