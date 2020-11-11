#to find odd-even numbers
#while loop


num = 1
limit = int(input("Enter limit: "))

while num <= limit:
    print(num, end = " - ")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    num+=1
