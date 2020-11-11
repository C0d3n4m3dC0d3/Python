#Strings are a sequence of character data
#any string/character enclosed in either single quotes or double quotes
#is treated as an object of classtype <str>

s = "Strings in Python"

print(s)
print(type(s))

char = 'c'
print(char)
print(type(char))

print()
#-------------------------------------------------------------------------
print()

#Defining string - 3 ways

#1. using double quotes
string1 = "Hello world, in double quotation!"

#2. using single quotes
string2 = 'Hello world in single quotation!'

#3. using triple quotes
string3 = """This is the new
                  Hello world!
                      Alignment"""

print("string1: ", string1)
print("string2: ", string2)
print("string3: ", string3)

print()
#-------------------------------------------------------------------------
print()

#Escape character '\'
movie_name = "Blumhouse\'s 'Mystery Island'"
print(movie_name)

string3 = """This is the new \
Hello world! \
Alignment"""
print("string3 with escape: '", string3, "'")

print()
#-------------------------------------------------------------------------
print()


#Accessing characters - 2 ways
#1 - using indexing
#index starts from 0, must be an integer
print(s[1])

#negative indexing
#-1 is the last character, -2 second last and so on
print(s[-1])

#2 - by slicing the string
#slicing operator is a colon :
print(s[3:5])
print(s[-8:-2])
print(s[:-4])

print()
#-------------------------------------------------------------------------
print()

#strings in python are immutable
s[0] = 'U'
print(s)
