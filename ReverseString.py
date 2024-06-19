
# This program will reverse your entier string
s = input("Enter a String:")

# Option 1
for i in range(len(s)-1, -1, -1):
    print(s[i], end='')
print()

# Option 2
print(s[::-1]) # s[start : stop : steps] Step -1 will start reading a string from end

# Option 3
rev = reversed(s) # it is a iterator
# print(next(rev))
for i in rev:
    print(i, end='')
print()

# Below program will reverse the sequence if string
s = input("Enter a String:")
spaces = s.split(' ')
for i in range(len(spaces)-1, -1, -1):
    print(spaces[i], end=' ')