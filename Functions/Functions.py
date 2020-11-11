#PYHTON_CLASS_2020 - Nov 2

#FUNCTIONS!!
'''
#simple function, with docstring
def greet():
    "Basic function for greeting users"  #docstring
    print("Welcome!")

greet()

#simple function with single argument
def greetMe(name):
    print("Hello, " + name + "! Good morning!")

name = input("Enter your name: ")
greetMe(name)


#using documentation string in functions
def docString():
    "Documentation strings are useful"  #docstring
    print(" when some error occurs in the function and the ", end="")
    print("user needs to recognise the function")

#to call the docstring
print(docString.__doc__, end="")
docString()


#simple function that accepts more than one arg, and returns something
def swapTwo(a, b):
    a = a + b
    b = a - b
    a = a - b

    return [a,b]


a = int(input("Enter first number: "))
b = int(input("Enter next number: "))

swapped = swapTwo(a, b)
print("a was" , a , "\na is now" , swapped[0])
print()
print("b was" , b , "\nb is now" , swapped[1])


#None is quivalent to null in other languages
def returnNone():
    print("Hello from inside returnNone()")
    return

print(returnNone())

#-----------------------------------------------------------------------------

def score(name, total):
    print("%s scored %d" %(name, total))

score("Siya", 43)

#different ways to call a function with arguments
score(name="Siya", total=43)
score(total=43, name="Siya")


#to find the area of a cricle
#defining a constant argument
def area(r, pi=3.14):
    area = pi * r**2
    print("Area of cirle of radius %d = %d" %(r, area))

area(10)


#function with if else statments
def absolute(num):
    if num >= 0:
        return num
    else:
        return -num

print(absolute(10))
print(absolute(-200))


#functions that return boolean values
def boolean(b):
    return bool(b)

print("2 > 0 ?", boolean(2 > 0))
print("2 > 5 ?", boolean(2 > 5))


#function that returns multiple values
#return always return values as tuples

def returnMore():
    return 'a', 'b', 12, 3.14

#not storing in any variable
print(returnMore())
print()

#storing in single variable
result = returnMore()
print(result[0])
print(result[1])
print(result[2])
print(result[3])
print()

#storing in multiple variable
a, b, c, d = returnMore()
print(a , b, c, d , sep="\n")

'''
