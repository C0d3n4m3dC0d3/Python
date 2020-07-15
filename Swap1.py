a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")

if(isinstance(a, int)):
    n = int(a)
else:
    n = float(a)

if(isinstance(b, int)):
    m = int(b)
else:
    m = float(b)
print("n = " + str(n))
print("m = " + str(m))

n = n+m
m = n-m
n = n-m

print("n = " + str(n))
print("m = " + str(m))
