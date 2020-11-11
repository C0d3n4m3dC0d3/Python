for no in range (2, 10):
    for factor in range(2, no):
        if(no%factor == 0):
            print(factor, " x ", no//factor, " = ", no)
            break
    else:
        print(no, " is prime!")
