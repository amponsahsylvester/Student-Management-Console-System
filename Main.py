# importing modules
from console_color import *
from students import Student

# creating database
student_database = []


#  welcome Screen menu
def welcome_screen():
    print(YELLOW, '**** Welcome To NIIT Student Management System ****')
    user_input = int(input('1. Add Student\n'
                           '2. View all Student Details\n'
                           '3. Search for Student Info\n'
                           '4. Delete Student Info\n'
                           '5. Update Student Info\n'
                           '6 About System\n'
                           '7. Exit Application\n\n'
                           'Please provide your request : '))
    user_options(user_input)


def user_options(user_input):
    if user_input == 1:
        response = 'yes'
        while response == 'yes':
            student_info = add_student_info()
            user_ans = input(GREEN + 'Do you want to save info? (y/n) : ').lower()
            if user_ans == 'y':
                student_database.append(student_info)
                print(BLUE, f'{student_info.get_first_name()} '
                            f'{student_info.get_middle_name()} '
                            f'{student_info.get_last_name()} '
                            f'has been saved successfully.')
            elif user_ans == 'n':
                user_ans = input('Do you want to cancel (y/n) : ').lower()
                if user_ans == 'y':
                    welcome_screen()
                else:
                    student_database.append(student_info)
            else:
                welcome_screen()
            response = input('Is there another student? (y/n) : ').lower()
        welcome_screen()

    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
    elif user_input == 5:
        pass
    elif user_input == 6:
        about_Us()
    elif user_input == 7:
        close_program()
    else:
        invalid_request()


#  about_us function
def about_Us():
    print('***** This System Keep Track Of Student Details ******')
    welcome_screen()


#  close_program function
def close_program():
    print(WHITE, '**** Thank You For Using NIIT SMS')
    exit(2)


#   Invalid_request function
def invalid_request():
    print('Invalid Request, Please Try Again. Thank You')


# add new student
def add_student_info():
    print(PURPLE, '**** Fill Details Below To Add Student ****')
    sid = input('Provide Student ID : ')
    f_name = input('Provide First Name : ')
    mid_name = input('Provide Middle Name : ')
    l_name = input('Provide Last Name : ')
    dob = input('Provide DOB (dd/mm/yyyy) : ')
    course = input('Provide Course : ')
    period = input('Provide Period : ')

    #     creating student object
    student_info = Student(sid, f_name, mid_name, l_name, dob, course, period)
    return student_info


#  calling function
welcome_screen()
