'''
Python program for if-else, if-elif-else, statements
'''

a = 100
b = 200
c = 350

#method 1
if a > b:
        print(str(a) + " is greater")
else:
        print(str(b) + " is greater")

#method 2
print(a) if a > b else print(b)

#method 3
if a > b and a > c:
    print(str(a) + " is the greatest")
elif b > c:
    print(str(b) + " is the greatest")
else:
    print(str(c) + " is the greatest")

print("These were three ways of using the control statements!")


