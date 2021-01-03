#unit 4
'''
Python File Operations: Reading files, Writing files in python, Understanding read functions,
read(), readline(), readlines(). Understanding write functions, write() and writelines()
Manipulating file pointer using seek Programming, using file operations.
Database Programming: Connecting to a database, Creating Tables,INSERT, UPDATE,
DELETE and READ operations, Transaction Control,Disconnecting from a database,
Exception Handling in Databases.
'''

# Savepoint 1 ~ FILES
'''
- Files are named locations in memory to peramanently store data
Methods associated with file programming
    : open("filename", "mode")  ----------- eg: open("Filex.txt", "r")
    : read()  ------------ eg: file_object.read()
    : read( int numChar) ------------- eg: file_object.read(15) >> reads 15 characters from current pointer position
    : readline() ------------- eg: file_object.readline() >> reads a single line from the file
    : readlines() ---------------- eg: file_object.readlines() >> read
    : readlines(int numLine) -------------- eg: file_object.readlines(3) >> reads 3 lines from cpp
    : close() ------------ eg: file_object.close()
    : write(line) - writes a single line onto the file
    : writelines(list/tuple) - write a list of lines onto the file; takes iterable objects as arguments
    : seek(offset, whence) - points to a particular location/offset/address
        whence - starting point for the seek
        offset, no of positions to move pointer to the actual desired location
        whence has only 3 value - 0 (starting of the file), 1 (current position), 2 (ending of the file)
    : tell() - tells the current position of the file pointer

Properties associated with files
    : name - name of the file
    : closed - true if closed, false if open
    : mode - read mode, write mode, append mode, read&write mode etc
'''

# Savepoint 2 ~ DATABASE PROGRAMMING
'''
Steps
    1. import pymysql interface module
            # import pymysql
    2. open the database connection
            # db = pymysql.connect("localhost/127.0.0.0", "user", "password", "dbname")
    3. prepare a cursor object - used for executing queries
            #cursor = db.cursor()
    4.  execute a query
            #cursor.execute("SELECT VERSION()")
            #cursor.execute("CREATE TABLE DEPARTMENT (col type constraint, . . )")
            #cursor.execute("INSERT INTO DEPARTMENT VALUES (val 1, val  2, ...)")
            #cursor.execute("UPDATE DEPARTMENT SET colname = value WHERE id = key")
            #cursor.execute("DELETE FROM DEPARTMENT WHERE id = key")
            #cursor.execute("SELECT * FROM DEPARTMENT")
    5. use methods to extract output values
            #var = cursor.fetchone()  --> used for fetching a single row of output
            #var = cursor.fetchall() --> used for fetching all rows of output
    6. close the connection
            #db.close()
'''

# Savepoint 3 ~ EXCEPTION HANDLING
'''
using keywords
try:
    error_causing_code
    
except:
    print_error
    
finally:
    anycode to execute after all
'''
