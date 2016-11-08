# student_class.py

'''The purpose of this script is to learn how to create a student class
and instances.
Each student will be added to a list called students.

'''

import datetime

print('Create a list to hold instances of students')
students = []

class Student():
    
    def __init__(self, student_id, firstname, lastname, gender, dob):
        '''Create instance of student'''

        self.student_id = student_id
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.dob = dob
        
    def display(self):
        '''Displays data for a specific instance'''

        print('ID: {}, name: {} {}, gender: {}, dob: {}'.format(self.student_id,\
              self.lastname, self.firstname, self.gender, self.dob))


# Function outside the class
def display_list_of_students():
    for student in students:
        print('ID: {}, Name: {}, M/F: {}, DoB: {}'.format(student.student_id,\
    (student.lastname +', '+ student.firstname), student.gender, student.dob))

print(
'''Create a student by entering a student_id. Assuming there are other
student ids in use in the school, start at an arbitrary integer, eg 815''')

id_815 = Student('815', 'Marion', 'Webster', 'F', '2001-12-30')
# Display details of student, using function inside the class
print('\nDisplaying details of student using function inside the class.')
Student.display(id_815)

print('Add student to list')
students.append(id_815)
# Repeat to add another student
print('Creating another student')
id_816 = Student(816, 'Daniel', 'Cheung', 'M', '2002-02-27')
Student.display(id_816)
print('and add to the list')
students.append(id_816)
# Display contents of list - two student objects
print('\nDisplay contents of list - two student objects')
print(students)
print()
# Display details of student in list
print('Iterate through the list, displaying each student')
display_list_of_students()

''' Now to add students interactively, finding highest number in list and
adding 1. Then getting student details from user.'''

# Function to find highest ID. Is there an easier, faster way? 
def find_next_student_id():        
    last_id = 0
    for student in students:
        if int(student.student_id) > last_id:
            last_id = int(student.student_id)

    student_id = last_id + 1
    student_id = 'id_' + str(student_id)
    return student_id    


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

