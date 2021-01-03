#1. Write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
list_1 = []
list_2 = []

n = int(input("Enter size of list 1: "))
m = int(input("Enter size of list 2: "))

print("Enter values for list 1")
for i in range(n):
    a = input("Enter element: ")
    list_1.append(a)
print()
print("Enter values for list 2")
for i in range(m):
    b = input("Enter element: ")
    list_2.append(b)

com_list = []
for i in list_1:
    if i in list_2:
        if i in com_list:
            break
        else:
            com_list.append(i)

print(list_1, list_2, com_list, sep='\n')


#---------------------------------------------------------------------------

2. Ask the user for a string and print out whether this string is a palindrome or not.
#(A palindrome is a string that reads the same forwards and backwards.)Hint: Strings are lists.
s = input("Enter string: ")
string = s

s_list = list(s)
s_list.reverse()

reverse_string = "".join(s_list)

if reverse_string == string:
    print(string, " is a palindrome!")
else:
    print(string, " is not a palindrome!")

#---------------------------------------------------------------------------
    
#3. a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_a = [a[i] for i in range(1, len(a), 2)]

#---------------------------------------------------------------------------

#4. years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
#   ages = []
#   for year in years_of_birth:
#       ages.append(2014 - year)
#Rewrite the above code using list comprehension
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = [2014 - year for year in years_of_birth]

#---------------------------------------------------------------------------
