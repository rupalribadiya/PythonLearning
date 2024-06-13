a = 5
b = 0 # ZeroDivisionError
b = 'P' # TypeError

try:
    b = int(input("Enter a number: ")) # ValueError
    print(a/b)

except ZeroDivisionError as e:
    print('You cannot divide by zero')

except ValueError as e:
    print('Invalid Input')

except Exception as e:
    print('Something went wrong')

finally:
    print("All resourses are closed..")

print('Bye')