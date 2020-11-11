message = "Welcome to IDLE" #global variable
print(message)

#use 'def' keyword to define the function
def myFun():
    global message
    message = "Good bye!" #local variable
    print(message)

myFun()
print(message)


#to declare a local variable as global, use 'global' keyword
