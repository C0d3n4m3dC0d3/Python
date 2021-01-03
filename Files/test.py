fopen = open("Hello.txt", "w")

fopen.write("Hello from the other side!")
fopen.writelines(["I must've called a thousand times!", "To tell you I'm sorry"])
fopen.writelines(("For everything that I'd done", "but in my mind"))

fopen.close()

fopen = open("Hello.txt", "r")

string = fopen.readlines()
print(string)
fopen.close()
