#PYHTON DATABASE CONCEPTS : 25-Nov-2020
#------------------------------------

#import the pymsql interface module
   #acts as an interface between py file and the db
import pymysql

#open db connection
db = pymysql.connect("localhost", "root", "sgkrupa9", "student")

#prepare a cursor object - using cursor() method
#used for executing queries
cursor = db.cursor()

#simple query - to find out the db version
#using the execute() method of cursor obj to execute queries
cursor.execute("SELECT VERSION()")

#fetch database version information, using fetchone()
#fetchone() is used for fetching a single row of output
db_vs = cursor.fetchone()
print("The database version is :", db_vs)

#disconnect from the database
db.close()


#-------------------------------------------------------------------------------------------------#
   #                                                 CRUD Operations                                               #
#-------------------------------------------------------------------------------------------------#

#CREATE TABLE
import pymysql 

dbcon = pymysql.connect("localhost", "root", "sgkrupa9", "student")

cursor = dbcon.cursor()

sql = ''CREATE TABLE DEPARTMENT (deptID VARCHAR(10) PRIMARY KEY, deptName VARCHAR(50), deptHead VARCHAR(30) NOT NULL''

cursor.execute(sql)

print("Query Executed Successfully")


''INSERT OPERATION''
import pymysql

dbcon = pymysql.connect("localhost", "root", "sgkrupa9", "student")

cursor = dbcon.cursor()

sql = ''INSERT INTO DEPARTMENT(deptID, deptName, deptHead) VALUES ('dpt101', 'CS&IT', 'Dr. Vimina ER')''

cursor.execute(sql)

print("Inserted 1 Row Successfully")

#--------------------------------------------------------------------------------------------------'
'' READ TABLE DATA ''

import pymysql

dbcon = pymysql.connect("localhost", "root", "sgkrupa9", "student")

cursor = dbcon.cursor()

sql = ''SELECT * FROM DEPARTMENT''

cursor.execute*

#------------------------------------------------------------------------------------------------------

cursor.execute(sql)

print("Inserted 1 Row Successfully")
