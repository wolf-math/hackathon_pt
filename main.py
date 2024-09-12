from student import Student
from tabulate import tabulate

def get_user_menu_choice():
    print("Welcome to student data getter")
    print("What would you like to do?")
    choice = input("""
    1. Get all student data
    2. insert student data
    3. Get specific student data
    4. Delete a student
    5. Update a student
    6. Exit
    > """)
    return choice

def main():
    student = Student()
    student.create_table()

    while True:
        choice = get_user_menu_choice()
        if choice == "1":
            student_list = student.view_all_students()
            print(tabulate(student_list, headers=["id", "first_name", "last_name", "birthdate", "tz", "favorite_color"]))
            print('\n')

        elif choice == "2":
            student.insert_student()
            print("data inserted successfully")

        elif choice == "3":
            stud_id = input("Choose student id: ")
            student_info = student.view_student(stud_id)
            print(tabulate(student_info, headers=["id", "first_name", "last_name", "birthdate", "tz", "favorite_color"]))

        elif choice == "4":
            stud_id = input("Choose student id: ")
            print("Are you sure you want to delete this student?")
            print(student.view_student(stud_id))
            yes_no = input("y/N")
            if yes_no == "y" or "yes":
                student.delete_student(stud_id)

        elif choice == "5":
            stud_id = input("Choose student id: ")
            student.update_student(stud_id)
            student_info = student.view_student(stud_id)
            print(tabulate(student_info, headers=["id", "first_name", "last_name", "birthdate", "tz", "favorite_color"]))

        else:
            break

        # requires input to continue
        input()


if __name__ == "__main__":
    main()
