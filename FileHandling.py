# Mode:
# r: read char
# w: write char
# a: append char
# rb: read binary
# wb: write binary

f = open('Public/input.txt','r')
# print(f.read())

f1 = open('Public/output.txt','w')

for data in f:
    f1.write(data)
