#python 2 - Accept two numbers from user and do division and floor division
a = input("Enter 1st number: ")
b = input("Enter 2nd number:")

if(isinstance(a, int)):
    n = int(a)
else:
    n = float(a)

if(isinstance(b, int)):
    m = int(b)
else:
    m = float(b)

#division - normal division - return answer as it is
c = n/m
print("The result of division(" + a + "/" + b +") = " + str(c))
#floor-division - integer division - returns the answer (if containing decimal part) rounded off to the nearest integer
c = n//m
print("The result of floor division(" + a + "//" + b +") = " + str(c))
