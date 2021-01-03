'''1. Write a python function that will return true if the two given integer values
are equal or their sum or difference is 5 (use if elseif accordingly)'''

def equalitySum(num1, num2):
    s = abs(num1 + num2)
    d = abs(num1 - num2)

    if num1 == num2:
        ret = True
    elif s == 5:
        ret = True
    elif d == 5:
        ret = True
    else:
        ret = False
    return ret

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("equalitySum(", a, ", ",b, ") = ", equalitySum(a,b))

#------------------------------------------------------------------------------

#2. Write a python function to check whether a given number is prime or not

def testPrime(num):
    f = 2
    stop = num // 2 + 1
    for factor in range(2, stop):
        if num % factor == 0:
            f = 3
            break
    return f == 2

num = int(input("Enter number to check for prime: "))
print( num, "is a prime number?", testPrime(num))


#------------------------------------------------------------------------------


#3. Write a progrm using function to generate all the factors of a number.

def printFactors(num):
    print("Factors of", num,"are:")
    for factor in range(1, num+1):
        if num % factor == 0:
            print(factor, end=" ")

num = int(input("Enter number to generate factors: "))
printFactors(num)
print()

#------------------------------------------------------------------------------

'''4. Write a Python function called compare which takes two strings s1 and s2 and
an integer n as arguments.The function should return True if first n characters
of both the strings are same else thefunction should return False.'''

def compare(s1, s2, n):
    for char in range(n):
        if(s1[char] != s2[char]):
            return False
    return True

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
n = int(input("Enter number of characters: "))

result = compare(str1, str2, n)
result = " " if result == True else " not "

print("The first", n, "characters of", str1, "and", str2, "are%ssame" % result)


#------------------------------------------------------------------------------

#5. Write a Python program to find the sum of n natural numbers using recursion.

def sumRecur(n):
    if n == 1:
        return 1
    else:
        return n+sumRecur(n-1)

n = int(input("Limit: "))
print("sum of", n, "natural numbers is: ", sumRecur(n))
