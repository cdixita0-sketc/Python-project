print("=========Welcome to the Student Data Organizer!=======\n")

students_list = []
subjects_set = set()

while True:
    print("\nSelect an option")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter student details:")

        sid = int(input("Student ID: "))
        dob = input("Date of Birth (YYYY-MM-DD): ")

        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")

        subs_input = input("Subjects: ")
        subjects = [s.strip() for s in subs_input.split(",")]

        for s in subjects:
            subjects_set.add(s)

        student = {
            "id_dob": (sid, dob),
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students_list.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if not students_list:
            print("No student records found.")
        else:
            print("\n--- All Students ---")
            for s in students_list:
                sid, dob = s["id_dob"]
                print(f"ID: {sid} | Name: {s['name']} | Age: {s['age']} | "
                      f"Grade: {s['grade']} | DOB: {dob} | "
                      f"Subjects: {', '.join(s['subjects'])}")

    elif choice == "3":
        sid = int(input("Enter Student ID to update: "))
        found = False

        for s in students_list:
            if s["id_dob"][0] == sid:
                found = True
                print("Leave blank to keep old value")

                new_age = input("New Age: ")
                new_grade = input("New Grade: ")

                if new_age:
                    s["age"] = int(new_age)
                if new_grade:
                    s["grade"] = new_grade

                print("Student updated!")
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        sid = int(input("Enter Student ID to delete: "))
        found = False

        for i, s in enumerate(students_list):
            if s["id_dob"][0] == sid:
                del students_list[i]
                found = True
                print("Student deleted.")
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        if not subjects_set:
            print("No subjects available.")
        else:
            print("\nSubjects Offered:")
            for sub in subjects_set:
                print("-", sub)

    elif choice == "6":
        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice.")
