#FUNCTIONS CLASS - 07-11-2020
#-----------------------------------------------------------------------------
'''Function returning more than one values to the calling function
def arithmetic(a, b):
    sum = a+b
    dif = a-b
    mul = a*b
    div = a/b
    return sum, dif, mul, div

in order to accept n return values, we need n variables to store them
in the calling function, in the same order

#Main calling function
a = int(input("Enter a: "))
b = int(input("Enter b: "))

s, df, m, dv = arithmetic(a,b)
print(a,"+",b,"=", s)
print(a,"-",b,"=", df)
print(a,"x",b,"=", m)
print(a,"/",b,"=", dv)
#-----------------------------------------------------------------------------
TYPES OF ARGUMENTS IN PYTHON
1. Reuqired
2. Keyword
3. Default
4. Variable Length

#-----------------------------------------------------------------------------

#REQUIRED ARGUMENTS
def valueChange(a):
    a = 10
    print("Inside, the value of a is",a)

#Calling code
a = int(input("Enter a: "))
valueChange(a)
print("Outside the function, the value of a is", a)
valueChange() #if the function is not called using an argument
#will generate error, therefore it is a required argument

#-----------------------------------------------------------------------------
'''
'''
#KEYWORD ARGUMENTS
def stdInfo(rno, name, course):
    print("Roll no:", rno)
    print("Name:", name)
    print("Course:", course)

stdInfo(rno=12, course="Int MCA", name="Kanika") 
'''
#----------------------------------------------------------------------------
'''
#DEFAULT ARGUMENTS
#initialising the variable/argument with a default value
def chocolates(cNo, cName, cBrand="Cadbury"):
    print("ChocoNum :", cNo)
    print("ChocoName :", cName)
    print("ChocoBrand :", cBrand)

chocolates(1, "Silk")
'''
#----------------------------------------------------------------------------

#VARIABLE LENGTH ARGUMENTS
def varLen(*arg):
    print("Result: ")
    for i in arg:
        print(i)


varLen(10, "Hello", 12, "World", 14, "!")
