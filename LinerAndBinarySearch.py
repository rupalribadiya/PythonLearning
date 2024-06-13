pos = -1

def linerSearch(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1

    return False

def binarySearch(list, n):
    list.sort()
    print(list)
    l = 0
    u = len(list)-1
    while l <= u:
        m = int((l + u) / 2)
        #m = (l + u) // 2 # int devision
        if list[m] == n:
            globals()['pos'] = m
            return True
        else:
            if list[m] > n:
                u = m - 1
            else:
                l = m + 1
    return False

list = [2,4,6,8,7,5,3,9]
n = 3


if linerSearch(list, n):
    print("Found at", pos + 1)
else:
    print("Not found")

pos = -1

if binarySearch(list, n):
    print("Found at", pos + 1)
else:
    print("Not found")
