# Jose Duran
# Program Status - Complete
# This program runs a loop that displays class details unless
# prompted not to.

# Define the main function.
def main():
    # Initialize choice input variable.
    choice = 0

    # Initialize loop that ends with Enter.
    while choice != '':
       choice = get_menu_choice()
       if choice == 'CS101':
           display('CS101')
       elif choice == 'CS102':
           display('CS102')
       elif choice == 'CS103':
           display('CS103')
       elif choice == 'NT110':
           display('NT110')
       elif choice == 'CM241':
           display('CM241')
       elif choice != '':
           print(choice, 'is an invalid course number.')

# Define the get_menu_choice function.
def get_menu_choice():
    # Display menu.
    print()
    print('Course Numbers and Details')
    print('---------------------------')

    # Prompt user to enter choice.
    choice = str(input('Enter a course number or press enter to stop: '))

    # Return the choice to the main function.
    return choice

# Define the display function.
def display(course):
    # Assign the dictionaries for the course details.
    room = {'CS101': '3004', 'CS102': '4501',
            'CS103': '6755', 'NT110': '1244', 'CM241': '1411'}
    instructor = {'CS101': 'Haynes', 'CS102': 'Alvarado',
            'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
    time = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.',
            'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}
    # Display the course.
    print('The details for course', course, 'are:')

    # Retrive values for each dictionary according to course choice.
    course_room = room.get(course)
    course_instructor = instructor.get(course)
    course_time = time.get(course)

    # Display the course details.
    print('Room:', course_room)
    print('Instructor:', course_instructor)
    print('Time:', course_time)

# Callback the main function.
main()
