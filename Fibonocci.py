#Fibonocci Series
n = int(input("Enter no of terms:: "))
a = 0
b = 1
print(str(a) + "\n" + str(b))
for i in range(2, n):
    c = a+b
    print(c)
    a = b
    b = c
