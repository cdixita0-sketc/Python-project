import uuid
while True:
    print("=========================\nWelcome to Multi-Utility Toolkit\n=========================\n")
    print("Choose an option:")
    print("1. DateTime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit\n=======================")

    choice = input("Enter your choise:")
    if choice == "1":
        while True:
            print("\nDatetime and Time Operations:")
            print("1. Display current date and time")
            print("2. Calculate diffrence between two dates/times ")
            print("3. Formate date into custom format")
            print("4. Stopwatch")
            print("5. Countdown Timer")
            print("6. Back to Main Menu")

            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                from datetime import datetime
                print("Current Date and Time:", datetime.now())

            elif sub_choice == "2":
                from datetime import datetime

                d1 = input("Enter first date (YYYY-MM-DD): ")
                d2 = input("Enter second date (YYYY-MM-DD): ")

                date1 = datetime.strptime(d1, "%Y-%m-%d")
                date2 = datetime.strptime(d2, "%Y-%m-%d")

                diff = abs(date2 - date1)
                print("Difference:", diff.days, "days")
            

            elif sub_choice == "3":
                from datetime import datetime

                d = input("Enter date (YYYY-MM-DD): ")
                date_obj = datetime.strptime(d, "%Y-%m-%d")

                print("Formatted Date:", date_obj.strftime("%d-%m-%Y"))

            elif sub_choice == "4":
                import time

                input("Press ENTER to start stopwatch...")
                start = time.time()

                input("Press ENTER to stop...")
                end = time.time()

                print("Elapsed Time:", round(end - start, 2), "seconds")
            elif sub_choice == "5":
                import time

                seconds = int(input("Enter seconds: "))

                while seconds > 0:
                    print("Time left:", seconds)
                    time.sleep(1)
                    seconds -= 1

                print("Time's up!")

            elif sub_choice == "6":
                break
        

    elif choice == "2":
        while True:
            print("\nMathematical Operations:")
            print("1. Calculate Factorial")
            print("2. Solve Compound Intrest")
            print("3. Trigonometric Calculations")
            print("4. Area Of Geometric Shapes")
            print("5. Back To Main Menu")

            sub_choice = input("Enter your choice:")

            if sub_choice == "1":
                n = int(input("Enter your choise: "))
                fact = 1

                for i in range(1, n + 1):
                    fact *= i

                print("Factorial:", fact)
            elif sub_choice == "2":
                p = float(input("Enter principal: "))
                r = float(input("Enter rate (%): "))
                t = float(input("Enter time (years): "))

                ci = p * (1 + r/100) ** t
                print("Compound Interest:", round(ci, 2))

            elif sub_choice == "3":
                import math

                angle = float(input("Enter angle in degrees: "))
                rad = math.radians(angle)

                print("sin:", math.sin(rad))
                print("cos:", math.cos(rad))
                print("tan:", math.tan(rad))  

            elif sub_choice == "4":
                print("1. Circle")
                print("2. Rectangle")

                shape = input("Choose shape: ")

                if shape == "1":
                    r = float(input("Enter radius: "))
                    print("Area:", 3.14 * r * r)

                elif shape == "2":
                    l = float(input("Enter length: "))
                    b = float(input("Enter breadth: "))
                    print("Area:", l * b) 

            elif sub_choice == "5":
                break
    elif choice == "3":
            while True:
                print("\nRandom Data Generation:")
                print("1. Generate Random Number")
                print("2. Generate Random List")
                print("3. Create Random Password")
                print("4. Generate Random OTP")
                print("5. Back to Main Menu")

                sub_choice = input("Enter your choise: ")

                if sub_choice == "1":
                    import random
                    print("Random Number:", random.randint(1, 100))

                elif sub_choice == "2":
                    import random
                    size = int(input("Enter list size: "))
                    rand_list = [random.randint(1, 100) for _ in range(size)]
                    print("Random List:", rand_list)
                
                elif sub_choice == "3":
                    import random
                    import string

                    length = int(input("Enter password length: "))
                    chars = string.ascii_letters + string.digits + string.punctuation

                    password = ''.join(random.choice(chars) for _ in range(length))
                    print("Password:", password)     

                elif sub_choice == "4":
                    import random
                    otp = random.randint(1000, 9999)
                    print("OTP:", otp)           

                elif sub_choice == "5":
                    break        
    


    elif choice == "4":
        print("\nGenerate Unique Identifiers:")
        print("Generated UUID:", uuid.uuid4())
        input("\nPress Enter to go back to Main Menu...")


    elif choice == "5":
        while True:
            print("\nFile Operation: ")
            print("1. Create a new file")
            print("2. Write to a file ")
            print("3. Read from a file")
            print("4. Append to a file")
            print("5. Back to Main Menu")

            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                filename = input("Enter file name: ")
                with open(filename, "w") as f:
                     print("File created successfully!")

            elif sub_choice == "2":
                filename = input("Enter file name: ")
                content = input("Enter content: ")
                with open(filename, "w") as f:
                    f.write(content)
                print("Content written successfully!")

            elif sub_choice == "3":
                filename = input("Enter file name: ")
                try:
                    with open(filename, "r") as f:
                        print("\nFile Content:\n", f.read())
                except:
                    print("File not found!")

            elif sub_choice == "4":
                filename = input("Enter file name: ")
                content = input("Enter content to append: ")
                with open(filename, "a") as f:
                        f.write("\n" + content)
                print("Content appended successfully!")

            elif sub_choice == "5":
                break

            else:
                print("Invalid choice!")


    elif choice == "6":
        module_name = input("Enter module name (like math, random): ")

        try:
            module = __import__(module_name)
            print("\nAvailable functions:\n", dir(module))
        except:
            print("Module not found!")

    elif choice == "7":
        print("Exit")
        break

    else:
        print("invalid")

        
    

        