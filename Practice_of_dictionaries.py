

def Student_registration(Student):
    Student['Name'] = input("Enter your name: ")
    Student['Age']= input("Enter your age: ")
    Student['Contact']= str(input('Enter your Contact number: '))
    Student['Email']=input('Enter your email address: ')
    print('======================================')
    print('Courses offered:')
    for i in range(0, len(Courses_offered)):
        
        print(f'{i+1}. {Courses_offered[i]}')
    print('======================================')
    Courses_taken = input('Choose the courses you want from these courses (Type the names separated by a comma e.g. AI, IoT, Metaverse): ')
    Courses_taken = Courses_taken.replace(" ", "")
    Courses_taken = Courses_taken.split(",")

    Student['Courses Taken'] = Courses_taken

    return Student

print('======================================')
print('Student Registeration system.')
print('======================================')
Students = []

Courses_offered = ('AI', 'IoT', 'CNC', 'Metaverse', 'Blockchain')

operation = 0
while(operation!=3):
    operation = int(input('\nWhat do you want to do?\n1. Register a student.\n2. See records.\n3. Exit the program.\n'))
    if operation == 1:
        Student = {}
        Students.append(Student_registration(Student))
        print("Registeration Completed.")
    elif operation == 2:

        print('Registered Students:\n')
        try:
            for student in Students:
                print (student['Name'])
        except:
            print("No Data available.")
        selected_student = input("Type the name of the student you want to see. ")
        print('Printing Records of ', selected_student)
        
        try:
            for student in Students:
                if student['Name'] == selected_student:
                    print(student)
                    break
        except:
            print("No Data available.")
    else:
        print("Program exited by the user.")
        break


