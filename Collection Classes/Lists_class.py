################################################################################
#PYTHON CLASS 05-10-2020 (COLLECTIONS IN PYTHON #1: LISTS)
#Property 1: Lists are ordered
  #0 based - index starts from 0
x = ['a', 'b', 'c', 'd']
y = ['p','q','r','s']
print(x[0])
print(y[3])
print(x==y) #return boolean value - EQUALITY CHECKING
print(['a', 'b', 'c', 'd'] == ['p','q','r','s']) #directly using the lists
print(['p','q','r','s'] == ['p','q','r','s'])

#to check if lists are equal, use 'is' and 'is not' keywords
print(x is y)
print(x is not y)

#to check if a vlaue exists within a list, then use 'in' and 'not in' keywords
print('p' in x)
print('z' not in y)

print("\n")
#Property 2: Can contain any arbitrary objects
  #They can contain any type of data
Cars = ["BMW", "Mini Cooper"]

Scooter = ["Vespa", "Activa"]

Chocolates = ["Lindt Lindor", "Munch", "Kit Kat"]

Random = [1, 4.32, True, "Hello", False]

LIST = [Cars, Scooter, Chocolates, Random, 42.33]
print(LIST)
#[['BMW', 'Mini Cooper'], ['Vespa', 'Activa'], ['Lindt Lindor', 'Munch', 'Kit Kat'],
#[1, 4.32, True, 'Hello', False], 42.33]

print("\n")

#Property 3: List items can be accessed using the index
Chocolates = ["Lindt Lindor", "Munch", "Kit Kat", "Ferero", "Hershey's Kisses", "Bounty"]
print(Chocolates)
print(Chocolates[3])
print(Chocolates[1:4])
#Negative indexing is possible
print(Chocolates[-1])
print(Chocolates[-5:-4])

print("\n")

#Property 4: Lists are mutable
 #Can be changed
 #Strings are immutable because it must be made thread safe
 #So that the confidentiality can be maintained
 #We give the various db connections, database queries, etc in strings
Chocolates[3] = "Mars"
Chocolates[1:4] = [100, 200, 300]
print(Chocolates)
    
print("\n")

#Property 5: Lists are dynamic
#dynamically created here, hence it's said to be dynamic
New = []
n = int(input("Enter limit: "))
for i in range(n):
    elt = input("Enter element: ")
    New.append(elt) #append() used to add more elements to the list, only single value

print(New)
    
#Property 6: Lists can be nested to any arbitrary depth
L = ['a', ['bb', 'cc', ['ddd', 'eee', 'fff']], 'g', 'h']
print(L)
L[1][1] = 100
print(L)
print(L[1][2])
print("\n")

#To print the exponential terms of 2 from 1 to 15
pow = []
for i in range(15):
    pow.append(2**i)
print(pow)
print("\n")

#shortcut - List Comprehension
pow = [2 ** i for i in range(15)]
print(pow)

#extend() method is used to add more than one values to a list at a time
pow.extend([2**i for i in range(len(pow), len(pow)+5)])
print(pow)

#insert() method to insert values into the list
#to insert into a list, by squeezing it into an empty slice of a list
odd = [1, 9]
print(odd)
odd.insert(1, 3) # insert at the 1st position, the value 3
print(odd)
odd[2:2] = [5,7]
print(odd)

#deleting values from lists using del keyword
even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(even)
#delete one element
del even[2]
##print(even)
#delete multiple elements
del even[2:4] #deletes values [2], [3], [4]
print(even)
#delete entire list
del even
print("even is deleted")

#To empty a list, use clear() method
even = [2, 4, 6, 8, 10]
print(even)
even.clear()
print(even)

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
print(my_list)
#To remove an item particular item, use remove() method
my_list.remove('p')
print(my_list)
#To remove and print an item from a list, use pop() method
my_list.pop(2)
print(my_list)

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

#to count the number of times an element repeats in a list, we use count() method
count = my_list.count('p')
print("Count of 'p' in my_list : ", count)'''

################################################################################
