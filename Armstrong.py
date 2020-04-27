#Armstrong Number
a = int(input("Enter number:: "))
num = a
sum = 0
while a != 0:
    b = a%10
    sum += (b*b*b)
    a = a/10
    
if sum == num:
    print(str(num) + " is an Armstrong Number.")
else:
    print(str(num) + " is not an Armstrong Number.")
