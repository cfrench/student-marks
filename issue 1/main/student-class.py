# student_class.py

'''The purpose of this script is to learn how to create a student class
and instances.
Each student will be added to a list called students.

'''

import datetime

print('Create a list to hold instances of students')
students = []




# Function outside the class
def display_list_of_students():
    for student in students:
        print('ID: {}, Name: {}, M/F: {}, DoB: {}'.format(student.student_id,\
    (student.lastname +', '+ student.firstname), student.gender, student.dob))

print(
'''Create a student by entering a student_id. Assuming there are other
student ids in use in the school, start at an arbitrary integer, eg 815''')



''' Now to add students interactively, finding highest number in list and
adding 1. Then getting student details from user.'''

# Function to find highest ID. Is there an easier, faster way? 



student_id = find_next_student_id()
# Validation of input omitted for brevity
print()
firstname = input('Please enter first name: ')
lastname = input('Please enter last name/ family name: ')
gender =''
while gender not in ['M', 'F']:
    gender = input('Please enter gender (M/F): ')
dob = input('Please enter dob (YYYY-mm-dd): ')

student_id = Student(student_id[3:], firstname, lastname, gender, dob)
students.append(student_id)
print('New student added\n')
# Display list again
display_list_of_students()

