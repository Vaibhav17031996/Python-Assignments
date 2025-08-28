students = {
    "Alpha": 85,
    "Beta" : 89,
    "Gamma" : 92,
    "Delta" : 74
}

name = input("Enter the student's name: ")

if(name in students):
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")