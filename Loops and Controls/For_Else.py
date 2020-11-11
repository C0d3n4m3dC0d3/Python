fruits = ["Guava", "Apple", "Mango", "Banana", "Pineapple", "Orange"]

#here, we do not know if the loop iterates till the end even after finding the fruit,
#or stops after finding the fruit

'''know whtehter the loop stops by entering a break statement or without
encountering the break statement'''

#two methods
#1. using flag
flag = 0
for fruit in fruits:
    if fruit == "Guava":
        print("Guava here!!")
        flag=1
        break
print(flag)


#using else clause, not part of if, but part of for
for fruit in fruits:
    if fruit == "Guava":
        print("Guava here!")
        flag = 1
        break

else:   #indented to the for, hence its called as the for-else use
    print("Loop ends without encountering a break")
