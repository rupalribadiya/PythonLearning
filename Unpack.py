def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100,50,25]
print(total(*coins), "knuts")

coinDict = {"galleons":100, "sickles": 50, "knuts":25}
print(total(**coinDict), "knuts")

def f(*args, **kwargs):
    print("Positional:", args)
    print("Name:", kwargs)

f(100,50,25,5, galleons=100, sickles=50, knuts=25)

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

yell("Rupal", "is", "web", "developer")

students = [
    {'name':'Rupal', 'location':'Surat'},
    {'name': 'Nishant', 'location': 'Surat'},
    {'name': 'Chand', 'location': 'Ahmedabad'},
    {'name': 'Sagar', 'location': 'Navsari'}
]

suratLoc = [
    student["name"] for student in students if student["location"] == "Surat"
]

print(suratLoc)
stds = filter(lambda s: s["location"] == "Surat", students)
print(list(stds))

for i, student in enumerate(students):
    print(i + 1, student["name"], student["location"])