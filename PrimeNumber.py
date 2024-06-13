# Prime Number

a=int(input("Enter a number: "))

for i in range(2,a):
    if(a%i==0):
        print("The number is not Prime number");
        break
else:
    print("The number is Prime number");

