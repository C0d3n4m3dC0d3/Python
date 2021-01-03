#-------------------------------------------------------------------------------------------------#
  #  Program to find the longest word in a sentence, using a simple function     # 
#-------------------------------------------------------------------------------------------------#

#function definition
def findLongest(string):

    #remove all punctuations
    p = ''',.:;?!@#$&*()-_'"/'''
    clean_str = ""
    #"Welcome to the world of an iceberg!"
    for char in string:
        if char not in p:
            clean_str += char

    #find longest word
    words = clean_str.split()  #split(sep) --> split(',')
    
    max = 0
    longest = ""
    
    for word in words:
        if len(word) > max:
            max = len(word)
            longest = word

    return longest

#------------------------------------------------#

s = input("Enter a sentence: ")
#The board read, "Welcome to the world of an iceberg!"

lword=findLongest(s)
print("The longest word is : ", lword)
