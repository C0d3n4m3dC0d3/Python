#PYTHON CLASS 07-10-2020 (MORE METHOD FOR/ON LISTS)
#These methods work on homogeneos lists

Cars = ["BMW", "Mini Cooper", "Sedan", "Nissan", "Ford"]
'''
#sort() to sort the list: changes are permanent
Cars.sort()
print(Cars)

#to print the reverse of the list, use reverse(): changes are permanent
Cars.reverse()
print(Cars)

print("\n")

#to temporarily sort the list, wwe can use sorted() method
Fruits = ["Pomegranate", "Apple", "Mango", "Guava", "Passion Fruit", "Grapes"]

print(sorted(Fruits))
print(Fruits)

print("\n")

#to search for an element in a list, use the index() method
#it returns the index position of the item (if it exists)
print(Cars.index("Sedan"))
Cars[Cars.index("Ford")] = "Fiesta"
print(Cars)

for car in Cars:
    print(Cars.index(car), car, sep=' - ')


#these methods can be used on a number list also
numbers = [100, 300, 500, 50, 20, 900]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

#to join values from a list, use join() method: not permanent
concat = ", ".join(Cars)
print(concat)
print()
print(Cars)

#slice operator is used to choose a sublist, it can be copied to another variable
newCars = Cars[2:5]
print(newCars)

#sum() method is used to sum up values
print(sum(numbers))


s = [1, 2, 3, 'a', 'b', 'c']
for i in range(len(s)):
    if(type(s[i]) == int):
       s[i]+=10
print(s)

print()

for i in s:
    if(type(i) == int):
        s[s.index(i)]-=10
print(s)
################################################################################
