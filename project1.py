print("\nWelcome to the Interactive personal Data Collactor!\n")


name = input("Please enter your name :")
age = int(input("Please enter your age:"))
height = float(input("please enter your height in meters:"))
fav_number = int(input("please enter your favourite number:"))

print("\nThank you! Here is the informaation we collacted:\n")

print("Name:", name, "(Type:", type(name), ", Memory Address:", id(name),")")
print("Age:", age, "(Type:", type(age), ", Memory Address:", id(age),")" )
print("Height:", height, "(Type:", type(height), ", Memory Address:", id(height),")")
print("Favourite Number:", fav_number, "(Type:", type(fav_number), ", Memory Address:", id(fav_number),")")


current_year =2026
birth_year = current_year - age

print("\n Your birth year is approximately:" ,birth_year )

print("\nThank you for using Personal Data Collector.  Goodbye!")