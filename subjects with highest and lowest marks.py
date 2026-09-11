name = input("Enter student name: ")
roll_no = input("Enter roll no: ")

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

total = maths + science + english
percentage = total / 3

print("\nStudent Name:", name)
print("Roll No:", roll_no)
print("Percentage:", percentage, "%")

if maths > science and maths > english:
    print("Highest marks: Maths")
elif science > maths and science > english:
    print("Highest marks: Science")
else:
    print("Highest marks: English")

if maths < science and maths < english:
    print("Lowest marks: Maths")
elif science < maths and science < english:
    print("Lowest marks: Science")
else:
    print("Lowest marks: English")
