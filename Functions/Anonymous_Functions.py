#ANONYMOUS FUNCTION - (Date: 09-11-2020)
'''
 - Function without name (nameless functions)
 - returns an expression (only a single one)
 - can provide multiple arguments
 - can contian only one expression, but can do multiple operations inside it)
 - use the keyword - 'lambda'
 - used for higher order built in fns (like map, filter, reduce, sort, etc)
 - used for short functions, that lives for a short duration
'''

#Anonymous function that returns the square of the argument
#function def
square = lambda x: x*x

#usage
n = int(input("Enter a number: "))
print("Square of", n ," = ", square(n))

#---------------------------------------------------------------------------

#Passing two arguments
sum = lambda x, y: x + y

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
print(x , "+", y, "=", sum(x, y))

#--------------------------------------------------------------------------

#using the lambda expression, in higher order built in functions
#map()
ol_list = [23, 42,5, 0, 7, 95, 8]
print("Old List: ", ol_list)
new_list = list(map(lambda x : x+2, ol_list))
print("New List : ", new_list)
print()

#--------------------------------------------------------------------------

#reduce()
#inorder to use reduce(), we need to import the function tools library
import functools
ol_list = [23, 42,5, 0, 7, 95, 8]
print("List: ", ol_list)
product = functools.reduce(lambda x,y: x*y, ol_list)
print("Product of ol_list elemets: ", product)
print()

#--------------------------------------------------------------------------


#filter()
ol_list = [23, 42,5, 0, 7, 95, 8]
print("Old List: ", ol_list)
odds = list(filter(lambda x:(x%2 != 0), ol_list))
print("Odd Values from ol_list: ", odds)            
print()

#--------------------------------------------------------------------------

#sort()
users = [
          {'name': 'Mahesh', 'age' : 28},
          {'name': 'Parvati', 'age' : 12},
          {'name': 'Kiran', 'age' : 31},
          {'name': 'Pallavi', 'age' : 64},
          {'name': 'Roshan', 'age' : 34}
        ]
users.sort(reverse=True, key=lambda e: e['age'])
for user in users:
            print(user)

#--------------------------------------------------------------------------
