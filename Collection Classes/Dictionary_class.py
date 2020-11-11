#PYTHON CLASS 12-10-2020 (COLLECTIONS IN PYTHON #3: DICTIONARY)
#unordered
#similar to HashTable in C#
#store data as key value pairs

Cars = {"Brand" : "Ford",
        "Model" : "Mustang",
        "Year" : "1960"
        }

#to retrieve values from a dictionary
brand = Cars["Brand"]
print(brand)
print(Cars)

#changing value
Cars['Year'] = 2019
print(Cars)
print()

for i in Cars:
    print(Cars[i], end=" ")
print()

Cars = {"Brand" : "Ford",
        "Model" : "Mustang",
        "Year" : "1960"
        }

for i in Cars.values():
    print(i, end =" ")
print()

for i,j in Cars.items():
    print(i, j)
print()

print(len(Cars))
print()


Cars["Color"] = "Black"
print(Cars)
print()

#removing elements, use pop(), popitem(), del, clear()
Cars.pop("Year")
print(Cars)
print()

Cars.popitem()
print(Cars)
print()


del Cars["Brand"]
#print(Cars) - returns error  [NameError: name 'Cars' is not defined]
print()

#del Cars
#print(Cars)
print()

Cars = {"Color" : "Black",
        "Brand" : "Ford",
        "Model" : "Mustang",
        "Year" : "1960"
        }
print(Cars)
print()

Cars.clear()
print(Cars)
print()
