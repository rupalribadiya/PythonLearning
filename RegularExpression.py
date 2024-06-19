import re

email = input("Enter your email: ").rstrip()

if re.search(r"^\w+@\w+\.com$", email):
    print("Valid")
else:
    print("Invalid")