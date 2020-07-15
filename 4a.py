#Python Activity 4
# 1. Create a list with 10 items
#a. bubble sort the list

l1 = ["Hello", "TXT", "rand()", "see me?", "hELLO" , "txt" , "Rand()" , "See Me?" , "roPe" , "promise"]
size = len(l1)
for i in range(size):
    for j in range(size-i-1):
        if(l1[j] > l1[j+1]):
            l1[j], l1[j+1] = l1[j+1], l1[j]

for e in range(size):
    print(l1[e], sep = "\n")
