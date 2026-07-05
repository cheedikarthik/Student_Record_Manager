import re
import os

FILE_NAME = "students.txt"


# -----------------------------
# Email Validation
# -----------------------------
def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email)


# -----------------------------
# Add Student
# -----------------------------
def add_student():

    try:

        roll = int(input("\nEnter Roll Number : "))

        name = input("Enter Name : ")

        email = input("Enter Email : ")

        if not validate_email(email):
            raise ValueError("Invalid Email Address")

        course = input("Enter Course : ")

        marks = float(input("Enter Marks : "))

        with open(FILE_NAME, "a") as file:

            file.write(f"{roll},{name},{email},{course},{marks}\n")

        print("\nStudent Added Successfully!")

    except ValueError as e:

        print("Error :", e)


# -----------------------------
# View Students
# -----------------------------
def view_students():

    try:

        with open(FILE_NAME, "r") as file:

            records = file.readlines()

            if len(records) == 0:

                print("\nNo Records Found")

                return

            print("\n==============================")
            print("      STUDENT RECORDS")
            print("==============================")

            for student in records:

                data = student.strip().split(",")

                print(f"""
Roll Number : {data[0]}
Name        : {data[1]}
Email       : {data[2]}
Course      : {data[3]}
Marks       : {data[4]}
------------------------------------
""")

    except FileNotFoundError:

        print("\nNo Student Records Available")


# -----------------------------
# Search Student
# -----------------------------
def search_student():

    roll = input("\nEnter Roll Number : ")

    found = False

    try:

        with open(FILE_NAME, "r") as file:

            for student in file:

                data = student.strip().split(",")

                if data[0] == roll:

                    found = True

                    print("\nStudent Found\n")

                    print("Roll Number :", data[0])
                    print("Name        :", data[1])
                    print("Email       :", data[2])
                    print("Course      :", data[3])
                    print("Marks       :", data[4])

                    break

        if not found:

            print("\nStudent Not Found")

    except FileNotFoundError:

        print("\nFile Not Found")


# -----------------------------
# Update Student
# -----------------------------
def update_student():

    roll = input("\nEnter Roll Number to Update : ")

    updated = False

    records = []

    try:

        with open(FILE_NAME, "r") as file:

            for student in file:

                data = student.strip().split(",")

                if data[0] == roll:

                    updated = True

                    print("\nEnter New Details\n")

                    name = input("Name : ")

                    email = input("Email : ")

                    if not validate_email(email):
                        raise ValueError("Invalid Email")

                    course = input("Course : ")

                    marks = input("Marks : ")

                    records.append(
                        f"{roll},{name},{email},{course},{marks}\n"
                    )

                else:

                    records.append(student)

        with open(FILE_NAME, "w") as file:

            file.writelines(records)

        if updated:

            print("\nStudent Updated Successfully")

        else:

            print("\nRoll Number Not Found")

    except Exception as e:

        print(e)


# -----------------------------
# Delete Student
# -----------------------------
def delete_student():

    roll = input("\nEnter Roll Number : ")

    deleted = False

    records = []

    try:

        with open(FILE_NAME, "r") as file:

            for student in file:

                data = student.strip().split(",")

                if data[0] == roll:

                    deleted = True

                else:

                    records.append(student)

        with open(FILE_NAME, "w") as file:

            file.writelines(records)

        if deleted:

            print("\nStudent Deleted Successfully")

        else:

            print("\nRoll Number Not Found")

    except FileNotFoundError:

        print("\nFile Not Found")


# -----------------------------
# Student Count
# -----------------------------
def total_students():

    try:

        with open(FILE_NAME, "r") as file:

            print("\nTotal Students :", len(file.readlines()))

    except FileNotFoundError:

        print("\nNo Records Found")


# -----------------------------
# Highest Marks
# -----------------------------
def highest_marks():

    try:

        with open(FILE_NAME, "r") as file:

            students = []

            for student in file:

                data = student.strip().split(",")

                students.append(data)

            highest = max(students, key=lambda x: float(x[4]))

            print("\nTopper Details")

            print("--------------------")

            print("Roll :", highest[0])

            print("Name :", highest[1])

            print("Marks :", highest[4])

    except:

        print("\nNo Records Available")


# -----------------------------
# Main Menu
# -----------------------------
while True:

    print("""
======================================
      STUDENT RECORD MANAGER
======================================

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Total Students
7. Highest Marks
8. Exit

======================================
""")

    choice = input("Enter Choice : ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        update_student()

    elif choice == "5":

        delete_student()

    elif choice == "6":

        total_students()

    elif choice == "7":

        highest_marks()

    elif choice == "8":

        print("\nThank You!")

        break

    else:

        print("\nInvalid Choice")