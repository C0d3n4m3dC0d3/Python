#EXERCISE ON FUNCTION (2 -11- 2020)

#1.Print a sequence of even numbers between to limits using function
def printEven(start, end):
    for num in range(start, end):
        if(num % 2 == 0):
            print(num)

printEven(2, 10)
print()

#2.Write a program to print first 10 fibonacci numbers using fucntion.
#  Pass 10 as the argument

def printFibonacci(limit):
    a = 0
    b = 1
    
    print(a, b, sep="\n")
    while a+b < limit:
        c = a+b
        print(c)
        a = b
        b = c

print("Fibonacci values upto 10")
printFibonacci(10)
5
