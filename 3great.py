#python 4- Accept 3 numbers from user and check which one is greatest among the three
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if(a>b and a>c):
    print(str(a) + " is the greatest among the three")
elif(b>c):
    print(str(b) + " is the greatest among the three")
else:
    print(str(c) + " is the greatest among the three")
