#Check for prime
num = int(input("Enter a number:: "))
fact = 2
re = 0
for i in range(int(num/2)):
    if(num%fact == 0):
        re = -1;
        break;
    fact += 1
if(re == -1):
    print(str(num) + " is not a prime number.")
else:
    print(str(num) + " is a prime number.")
