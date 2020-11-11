#DICTIONARY_2 - 19-10-2020

#Creating empty dictionary
months = {}
print(months)
#Adding values
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
    }

print(months)

for x in months.keys():
    print("month",x,"= ", months[x])


#sorting dictionaries tempo
dictempo = {0:1, 1:2, 2:3, 3:4, 4:3, 3:2, 2:1, 1:0}
print(sorted(dictempo.items())) #to sort the dictionary based on key values

#sorts only unique keys, and the first occurance of duplicate keys

dictemp = {0:0, 1:2, 2:3, 3:4, 5:4, 4:3}
print(sorted(dictemp.items()))

#to sort the dictionary using the values
import operator
print(sorted(dictempo.items(), key=operator.itemgetter(1)))
print()
print(sorted(dictemp.items(), key=operator.itemgetter(1)))

#dictionary with square values


##############################################################################

#programt to remove duplicate values
student_data = {
    'id1' : {'name' : ['Sara'],
             'class' : ['V'],
             'subject_integration' : ['english', 'math', 'science']
            },
    'id2' : {'name' : ['David'],
             'class' : ['V'],
             'subject_integration' : ['english', 'math', 'science']
             },
    'id3' : {'name' : ['Sara'],
             'class' : ['V'],
             'subject_integration' : ['english', 'math', 'science']
             },
    'id4' : {'name' : ['Surya'],
             'class' : ['V'],
             'subject_integration' : ['english', 'math', 'science']
             }
    }

new_dict = {}

for key, value in student_data.items():
    if value not in new_dict.values():
        new_dict[key] = value

for value in new_dict.values():
    for key in value.keys():
        print(key,":",value[key])
    print()

##############################################################################

#to check if a dictionary is empty
my_dict = {}
if not bool(my_dict):
    print("Dictionary is empty!")

##############################################################################

#using sum() method in dictionary
my_dict = {'d1' : 100,
           'd2' : -9,
           'd3' : 34,
           'd4' : 200}
print(sum(my_dict.values()))

##############################################################################

#integrating dictionaries within lists

customers = [{'id': "cust_1221",
              'name' : "Oh Jun Su"
             },
             {'id': "cust_2123",
              'name' : "Gyeong Woo Yeon"
             },
             {'id': "cust_0125",
              'name' : "Lee Soo"
             }]

print("Customer ID | Customer Name")
print("---------------------------")
for customer in customers:
    print(customer['id'],"  | ", customer['name'])
    print("---------------------------")

#to add a new field, common for all
for customer in customers:
    customer['drama_of_choice', "More than friends"]

print(customers)

##############################################################################

#to build a dictionary incrementally

diction = {}
diction['some_key'] = 'some_value'

##############################################################################
