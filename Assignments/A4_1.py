#1. Write a python script to sort (ascending and decending) a dictionary by value

d_one = {"Value 1" : 3,
         "Value 2" : 1,
         "Value 3" : 9,
         "Value 4" : 2,
         "Value 5" : 4,
         "Value 6" : 6,
         "Value 7" : 0}
import operator
d_one_sorted = sorted(d_one.items(), key=operator.itemgetter(1))
print(d_one_sorted)
print()
d_one_sorted.reverse()
print(d_one_sorted)
