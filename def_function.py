
data = []



def input_data():
    """Input 1D array"""
    global data
    data = list(map(int, input("Enter data for a 1D array (separated by spaces): ").split()))
    print("\nData has been stored successfully!")


def display_summary():
    """Built-in functions summary"""
    if not data:
        print("No data available!")
        return
    print("\nData Summary:")
    print("- Total elements:", len(data))
    print("- Minimum value:", min(data))
    print("- Maximum value:", max(data))
    print("- Sum of all values:", sum(data))


def factorial(n):
    """Recursive factorial"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def calculate_factorial():
    n = int(input("Enter a number: "))
    print("Factorial of", n, "is:", factorial(n))


def filter_threshold():
    if not data:
        print("No data available!")
        return
    t = int(input("Enter threshold value: "))
    result = list(filter(lambda x: x > t, data))
    print("Filtered values (>", t, "):", result)


def sort_data():
    if not data:
        print("No data available!")
        return
    print("Sorted Data:", sorted(data))


def dataset_stats():
    if not data:
        print("No data available!")
        return
    mn = min(data)
    mx = max(data)
    avg = sum(data) / len(data)
    print("\nDataset Statistics:")
    print("Minimum:", mn)
    print("Maximum:", mx)
    print("Average:", avg)




while True:
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = input("Please enter your choice: ")

    if choice == "1":
        print("\nStep 1: Input Data")
        input_data()

    elif choice == "2":
        print("\nStep 2: Display Data Summary (Built-in Functions)")
        display_summary()

    elif choice == "3":
        print("\nStep 3: Calculate Factorial (Recursion)")
        calculate_factorial()

    elif choice == "4":
        print("\nStep 4: Filter Data by Threshold (Lambda Function)")
        filter_threshold()

    elif choice == "5":
        print("\nStep 5: Sort Data")
        sort_data()

    elif choice == "6":
        print("\nStep 6: Display Dataset Statistics (Return Multiple Values)")
        dataset_stats()

    elif choice == "7":
        print("Thank you for using Data Analyzer and Transfer program. Goodbyr!")
        break

    else:
        print("Invalid choice! Please try again.")