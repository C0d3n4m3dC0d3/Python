#1.
name = input("Enter Employee Name ")
salary = input("Enter salary ")
company = input("Enter Company name ")
print("\n")
print("Printing Employee Details")
print("Name", "Salary", "Company")
print(name, salary, company)

'''
OUTPUT:
Enter Employee Name Ram
Enter salary 50000
Enter Company name JSR & Co Ltd


Printing Employee Details
Name Salary Company
Ram 50000 JSR & Co Ltd
'''

#--------------------------------------------------------------------

#2. Program to check input type in Python
number = input("Enter number ")
name = input("Enter name ")
print("\n")
print("Printing type of a input value")
print("type of number", type(number))
print("type of name", type(name))

'''
OUTPUT:
    Enter number 43
Enter name Ram


Printing type of a input value
type of number <class 'str'>
type of name <class 'str'> 
'''

#-------------------------------------------------------------------


#3. Program to calculate addition of two input numbers
first_number = int(input("Enter first number "))
second_number = int(input("Enter second number "))
print("\n")
print("First Number:", first_number)
print("Second Number:", second_number)
sum1 = first_number + second_number
print("Addition of two number is: ", sum1)


'''
OUTPUT:

Enter first number 32
Enter second number 12


First Number: 32
Second Number: 12
Addition of two number is:  44
'''

#---------------------------------------------------------------------


#4. Accept one integer and one float number from the user and
#calculate the addition of both the numbers.

num_int = int(input("Enter integer value: "))
num_float = float(input("Enter decimal number: "))

sum_num = num_int + num_float
print(num_int, " + ", num_float, " = ", sum_num)

'''
OUTPUT:
    Enter integer value: 12
    Enter decimal number: 12.5
    12  +  12.5  =  24.5
'''

#---------------------------------------------------------------------

#5. Format output strings by its positions
firstName = input("Enter First Name ")
lastName = input("Enter Last Name ")
organization = input("Enter Organization Name ")
print("\n")
print('{0}, {1} works at {2}'.format(firstName, lastName, organization))
print('{1}, {0} works at {2}'.format(firstName, lastName, organization))
print('FirstName {0}, LastName {1} works at {2}'.format(firstName, lastName, organization))
print('{0}, {1} {0}, {1} works at {2}'.format(firstName, lastName, organization))


'''
OUTPUT:
    Enter First Name Siya
Enter Last Name Ram
Enter Organization Name JSR & Co Ltd


Siya, Ram works at JSR & Co Ltd
Ram, Siya works at JSR & Co Ltd
FirstName Siya, LastName Ram works at JSR & Co Ltd
Siya, Ram Siya, Ram works at JSR & Co Ltd
'''

#---------------------------------------------------------------------------------

#6. Accessing output string arguments by name
name = input("Enter Name ")
marks = input("Enter marks ")

print("\n")
print('Student Name:  {firstName}, Marks: {percentage}%'.format(firstName=name, percentage=marks))

'''
OUTPUT:
Enter Name Ram
Enter marks 75

Student Name:  Ram, Marks: 75%
'''

#-------------------------------------------------------------------------------

#7. Output text alignment specifying a width
text = input("Enter text ")
print("\n")
# left aligned
print('{:<25}'.format(text))
# Right aligned
print('{:>25}'.format(text))
# centered
print('{:^25}'.format(text))

'''
OUTPUT:
Enter text Hello, world!


Hello, world!            
            Hello, world!
      Hello, world!
'''

#--------------------------------------------------------------------------

#8. Display output Number in various type format
number = int(input("Enter number "))
print("\n")
# 'd' is for integer number formatting
print("The number is:{:d}".format(number))
# 'o' is for octal number formatting, binary and hexadecimal format
print('Output number in octal format : {0:o}'.format(number))
# 'b' is for binary number formatting
print('Output number in binary format: {0:b}'.format(number))
# 'x' is for hexadecimal format
print('Output number in hexadecimal format: {0:x}'.format(number))


'''
OUTPUT:
Enter number 32

The number is:32
Output number in octal format : 40
Output number in binary format: 100000
Output number in hexadecimal format: 20
'''

#---------------------------------------------------------------------------

#9. Odd Or Even
num = int(input("Enter number: "))
if num%2 == 0:
    print("Even number")
else:
    print("Odd number")

#---------------------------------------------------------------------------

#10. Create a program that asks the user for a number and then prints out a list
# of all the divisors of that number.

number = int(input("Enter number: "))
divisors = [1]
for div in range(2, number):
    if number%div == 0:
        divisors.append(div)
divisors.append(number)
print("Divisors of", number, " = ", divisors)

#-----------------------------------------------------------------------------
