#PYTHON CLASS 05-10-2020 (COLLECTIONS IN PYTHON #2: TUPLE)
#Tuples are similar to lists.
#They are like records in a database

#Prop 1: Unlike lists, tuples are immutable
#but, they can be deleted completely, if not partially

T = (1, 2, 3, 4, 5)

print(T)
#print using index
print(T[1:3])
#print using negative indexing
print(T[-5:5])
print()
print()

#creating single element tuple, printing its type
Chokkos = ('Munch')
print(Chokkos, ' is of type: ', type(Chokkos))
Chokkos = ('Munch',)
print(Chokkos, ' is of type: ', type(Chokkos))
print()
print()

#to join two tuples, use '+'
more_Chokkos = ('KitKat', 'Galaxy', 'Bounty')
print(Chokkos+more_Chokkos)
print()
print()

#to make changes to a tuple
#then convert back

#1.convert tuple to a list
Chokkos = list(Chokkos)
more_Chokkos = list(more_Chokkos)
print(type(Chokkos))
print()

#2. make changes to it
for i in more_Chokkos:
    Chokkos.append(i)
print()

#convert it back to tuple
Chokkos = tuple(Chokkos)
more_Chokkos = tuple(more_Chokkos)
print(Chokkos)
print(more_Chokkos)
print()
print()

#1 - Create a tuple of ten fruit items and access those items by spcifying the
#range: [1:4], [-7:-1], [-4:], [5:], [:9]
fruits = ('Mango', 'Apple', 'Passion Fruit', 'Guava', 'Banana',
          'Orange', 'Grape', 'Jackfruit', 'Watermelon', 'Sapota')

print(fruits[1:4]) #('Apple', 'Passion Fruit', 'Guava')
print(fruits[7:-1]) #('Jackfruit', 'Watermelon')
print(fruits[-4:]) #('Grape', 'Jackfruit', 'Watermelon', 'Sapota')
print(fruits[5:]) #('Orange', 'Grape', 'Jackfruit', 'Watermelon', 'Sapota')
print(fruits[:9]) #('Mango', 'Apple', 'Passion Fruit', 'Guava', 'Banana', 'Orange', 'Grape', 'Jackfruit', 'Watermelon')

print()
print()

