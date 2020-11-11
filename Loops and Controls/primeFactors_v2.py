#program to find factors and check if a number is prime

choice = 'y'
#to allow the user to input as many numbers as they wish
while(choice == 'y' or choice == 'Y'):
    #accept number
    num = int(input("Enter number: "))
    #print factors
    print("Factors of ", num, " : 1", num,end =" ")
    for f in range(2, (num//2)+1):
        if num%f == 0:
            print(f, sep = " ")
            break
        f+=1
    else:
        #if number is prime, print prime
        print("***PRIME***")
    choice = input("Continue(y/n)? ")
