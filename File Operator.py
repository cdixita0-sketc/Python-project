class JournalManager:

    def __init__(self):
        self.file = "journal.txt"


    def add_entry(self):

        entry = input("Enter your journal entry: ")

        f = open(self.file, "a")
        f.write(entry + "\n\n")
        f.close()

        print("Entry added successfully!")


    def view_entries(self):

        try:
            f = open(self.file, "r")
            data = f.read()

            if data.strip() == "":
                print("No journal entries found.")
            else:
                print("\nYour Journal Entries:")
                print("----------------------")
                print(data)

            f.close()

        except:
            print("No journal entries found.")


    def search_entry(self):

        word = input("Enter keyword or date to search: ")

        try:
            f = open(self.file, "r")

            found = False

            for line in f:
                if word.lower() in line.lower():
                    print(line.strip())
                    found = True

            if not found:
                print("No entries found.")

            f.close()

        except:
            print("File not found.")


    def delete_entries(self):

        choice = input("Are you sure you want to delete all entries? (yes/no): ")

        if choice.lower() == "yes":
            f = open(self.file, "w")
            f.write("")
            f.close()

            print("All journal entries deleted.")

        else:
            print("Deletion cancelled.")



j = JournalManager()

while True:

    print("\nWelcome to Personal Journal Manager")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    ch = input("Please select an option: ")

    if ch == "1":
        j.add_entry()

    elif ch == "2":
        j.view_entries()

    elif ch == "3":
        j.search_entry()

    elif ch == "4":
        j.delete_entries()

    elif ch == "5":
        print("Thank you for using Personal Journal Manager. Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option.")