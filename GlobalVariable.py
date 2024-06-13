# Use Of Global Variables

a = 10

def something():
    print(__name__)
    a=15
    print(a)
    x = globals()['a']
    globals()['a'] = 20
    print(globals()['a'])
    print(x)

print(__name__)
something()
print(a)