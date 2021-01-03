# FILES CLASS 2 - 16 - 11- 2020 #

'''
METHODS TO READ FROM A FILE:
  read()
  read(size int)
  readline()
  readlines()
  readlines(size int)
'''
'''
fo = open("Files_1.py", 'r')
print(fo.read())
print(fo.read(10))
print(fo.readline())
print(fo.readlines())
print(fo.readlines(10))


# FILES IN WRITE MODE
'''
'''
METHODS TO WRITE ONTO A FILE:
    write(string line)
    writelines(list lines / tuple lines)
'''
'''

# if file exists, then it will oepne the existing file,
# else, it will create a new file with the given name

fo = open("writeNew.txt", "w")
fo.write("Hello world!\n")
fo.write("This is the second line of the new file.")
fo.write("\nThat's it!")
fo.close()

fo = open("writeNew.txt", "r")
print(fo.read())
fo.close()

#if we open an existing file in write mode, it will overwrite the existing
#content and write the new content onto the file

fo = open("writeNew.txt", "w")
fo.write("It's new!")
fo.write("\nNew member here! I am Prips!")
fo.write("\nJoined for python!")
fo.close()

fo = open("writeNew.txt", "r")
print(fo.read())

#If we want to add more than one line at the same time, then we can use the
#writelines() method. It takes iterable objects like list, or tuples as
#arguments

fo = open("writeNew.txt", "w")
fo.writelines(["Written using writelines()!\n", "Overwritten the content!"])
fo.close()

fo = open("writeNew.txt", "r")
print(fo.read())
'''

#PRACTICE THESE!!
#append mode, rewrite mode, etc

#seek() method in association with files
#seek() method acts as a pointer for the file
#it points to a particular location/offset/address location
#Syntax of method:   seek(offset, whence)
#offset says the no of posistions or indexes to be moved forward from the
# position specified in the whence parameter

#whence tell the position from where the seek pointer should move
# has only 3 values-
          # 0 - From the starting of the file
          # 1 - From the current position
          # 2 - From the end of the file
#if we are seeking from the start, then no need to specify the whence value
          #by default it is set to 0


fo = open("writeNew.txt", "r")
print(fo.read())

fo.seek(7)
print(fo.tell())
#tell() method is used to tell the current position of the file pointer
print(fo.readline())
fo.close()
#negative indexing for file pointer is used in binary file formats
