'''1. Given different scored marks of students. We need to find grades.
The test score is an average of the respective marks scored in
    assignments,
    tests and
    lab-works.

The final test score is assigned using below formula.

10 % of marks scored from submission of Assignments
70 % of marks scored from Test
20 % of marks scored in Lab-Works

Grade will be calculated according to :
1. score >= 90 : "A"
2. score >= 80 : "B"
3. score >= 70 : "C"
4. score >= 60 : "D"
USE if-elif-else statement.'''


#storing student marks in dictionary
RNo1 = {"Name" : "Ananya",
        "Assignment" : [10, 9],
        "Test" : [18, 19, 19.5],
        "Lab" : [8, 9]}
RNo2 = {"Name" : "Brinda",
        "Assignment" : [8],
        "Test" : [17, 15, 16],
        "Lab" : [7, 8]}
RNo3 = {"Name" : "Cheryl",
        "Assignment" : [8, 8.5],
        "Test" : [19, 19],
        "Lab" : [6.8, 7]}
RNo4 = {"Name" : "Drishya",
        "Assignment" : [7.4, 8.2],
        "Test" : [16, 17.3],
        "Lab" : [8.5, 8]}
RNo5 = {"Name" : "Essa",
        "Assignment" : [10, 10],
        "Test" : [18, 18.4, 18.7],
        "Lab" : [8.4, 8.7]}


#calculating the test score of each student

Roll = [RNo1, RNo2, RNo3, RNo4, RNo5]
fScore = [0,0,0,0,0]
for i in range(len(Roll)):
    RNo = Roll[i]
    #find total of scores
    assign = float(sum(RNo["Assignment"]))
    test = float(sum(RNo["Test"]))
    lab = float(sum(RNo["Lab"]))

    #finsding their averages
    tfa = assign/2
    tft = test/3
    tfl = lab/2

    #finding final score
    fScore[i] = (.1*tfa)+(0.7*tft)+(0.2*tfl)

for i in range(len(fScore)):
    if fScore[i] >= 18:
        print("A")
    elif fScore[i] >= 16:
        print("B")
    elif fScore[i] >= 14:
        print("C")
    elif fScore[i] >= 12:
        print("D")
    else:
        print("E")
        
        
def getDetail():
	student["Name"] = input("Enter name: ")
	n = int(input("Enter no of Assignments: "))
	print("Enter marks for assignment: ")
	for i in range(n):
		student["Assign"[i]] = float(input())
	n = int(input("Enter no of Tests: "))
	print("Enter marks for tests:")
	for i in range(n):
		student["Test"[i]] = float(input())
	n = int(input("Enter no of Labs: "))
	print("Enter lab marks: ")
	for i in range(n):
		student["Lab"[i]] = float(input())
	return student
	
#-------------------------------------------------------------------------------------------------

#2. Using nested for loop print the following pattern:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
#6 6 6 6 6 6
#7 7 7 7 7 7 7
#8 8 8 8 8 8 8 8
#9 9 9 9 9 9 9 9 9
#10 10 10 10 10 10 10 10 10 10

for i in range(11):
    for j in range(i):
        print(i, end = " ")

    print()
	
student = getDetail()
print(student)
print(type(student))

#-------------------------------------------------------------------------------------------------
