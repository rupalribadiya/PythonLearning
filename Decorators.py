# Decorators: Changing the behaviour of existing function:

def printStr(str):
    print(str)

def appendStr(func):
    def inner(str):
        return func('I am ' + str);

    return inner

func1 = appendStr(printStr);
func1('Rupal')