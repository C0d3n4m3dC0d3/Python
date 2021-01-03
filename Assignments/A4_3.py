#3. Write a Python script to concatenate following dictionaries to create a new one

dic1 = {1 : 10, 2 : 20}
dic2 = {3 : 30, 4 : 40}
dic3 = {5 : 50, 6 : 60}

dict4 = {}

print("\n")

for key in dic1.keys():
    dict4[key] = dic1[key]

for key in dic2.keys():
    dict4[key] = dic2[key]    

for key in dic3.keys():
    dict4[key] = dic3[key]

print(dict4)
