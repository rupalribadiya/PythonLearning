import csv

# Mode:
# r: read char
# w: write char
# a: append char
# rb: read binary
# wb: write binary

def get_students(students):
    # for student in sorted(students, key=get_name, reverse=True):
    for student in sorted(students, key=lambda student: student["name"], reverse=True):
        print(f"{student['name']} is from {student['location']}")

def read_file():
    students = []
    with open('Public/name.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            student = {"name": row["name"], "location": row["location"]}
            students.append(student)
    return students

def write_file(student):
    with open('Public/name.csv', 'a', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "location"])
        writer.writerow(student)

def main():

    name = input("What is your name? ")
    location = input("What is your location? ")
    write_file({"name": name, "location": location})

    students = read_file()
    get_students(students)

main()