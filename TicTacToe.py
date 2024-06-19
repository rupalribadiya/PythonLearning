import numpy as np

list = np.zeros((3,3), dtype=int)
list[0][1] = 1
print(list)

win = [[(0,0),(0,1),(0,2)]]
print(win[0][2][1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")