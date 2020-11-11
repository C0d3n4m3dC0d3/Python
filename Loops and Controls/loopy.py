'''Looping constructs in Python '''

#for loop
#for loop can be used to loop through certain data types


#range data type
#it is used to store a sequence of values
#other data types of the same kind are: list and tuple
for i in range (10):
    print(i, end =" ") #prints space-separated values

print("\n")

for i in range(10):
    print(i) #prints nos in new line
    
print()

#range() can take parameters
#range(startval, endval, step)
for i in range(10, 20):
    print(i, end = " " )

print()

for i in range(5, 50, 5):
    print(i, end = " ")

print("\n")

'''Python program for Sequence data types: Lists, and Tuples.'''

#list []
fruits = ["Papaya", "Mango", "Orange"]
for fruit in fruits:
    print(fruit, end= " ")
print("\n")


#tuple ()
veggies = ("Cabbage", "Cauliflower", "Bell Peppers")
for veggie in veggies:
    print(veggie, end= " ")
print("\n")

#strings
for char in "This is a string!":
    print(char, end = "   ")
print("\n")
