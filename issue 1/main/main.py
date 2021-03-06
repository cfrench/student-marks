import datetime
import time
import logging
from student import Student
from typing import List

log = logging.getLogger(__name__)


def display_list_of_students(list_of_students: List[Student]):
    # Print out all the students
    for s in list_of_students:
        print(s)


def find_next_student_id(list_of_students: List[Student])->int:
    # Find the next available ID for a student
    return max(list_of_students, key=lambda s:s.student_id).student_id + 1


def main():
    # Create a list to hold all students
    students = []

    id_815 = Student(815, 'Marion', 'Webster', 'female', datetime.date(2001,12,30))
    # Display details of student, using function inside the class
    log.info('\nDisplaying details of student using function inside the class.')
    log.info(id_815)

    log.info('Add student to list')
    students.append(id_815)
    # Repeat to add another student
    log.info('Creating another student')
    id_816 = Student(816, 'Daniel', 'Cheung', 'male', datetime.date(2000,4,29))
    log.info(id_816)
    log.info('and add to the list')
    students.append(id_816)
    # Display contents of list - two student objects
    log.info('\nDisplay contents of list - two student objects')
    print(students)
    # Display details of student in list
    log.info('Iterate through the list, displaying each student')
    display_list_of_students(students)

    student_id = find_next_student_id(students)
    # Validation of input omitted for brevity
    print()
    firstname = input('Please enter first name: ')
    lastname = input('Please enter last name/ family name: ')
    gender =''

    while gender not in ['male', 'female']:
        gender = input('Please enter gender (male/female): ')

    dob = datetime.date(*time.strptime(input('Please enter dob (YYYY-mm-dd): '), "%Y-%m-%d")[:3])

    student_id = Student(student_id, firstname, lastname, gender, dob)
    students.append(student_id)
    print('New student added\n')
    # Display list again
    display_list_of_students(students)

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger("").setLevel(logging.INFO)
    main()