#FILES IN PYTHON - DATE: 09-11-2020
'''
 - named location to store data
'''

# to open a file in read mode and display it
fopen = open("Files_2.py", "r")
print(fopen.read())

#to read a specific number of characters
print(fopen.read(15))
'''Reads the first 15 characters from where the pointer stops'''

#to read a line from the file
print(fopen.readline())
print(fopen.readline())
print(fopen.readline())

#METHODS ASSOCIATED WITH FILES
fo = open("Files_2.py", "r+")
print("Name of the File: ", fo.name)
print("Closed or Not: ", "Closed" if fo.closed else "Open")

fo.close()

print("Closed or Not: ", "Closed" if fo.closed else "Open")
print("Opening mode of File:", fo.mode)
