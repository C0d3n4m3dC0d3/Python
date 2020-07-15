#python 3 - Swap two numbers using one line of code

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
print("a = " + str(a) + " and b = " + str(b))
a,b = b, a
print("a = " + str(a) + " and b = " + str(b))
