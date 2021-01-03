#8. Write a python script to merge two dictionaries

def merge(d1, d2):
    for key in d2.keys():
        d1[key] = d2[key]
    return d1

lilAscii = {'a' : 97, 'b' : 98, 'c' : 99, 'd' : 100} 
lilAscii_2 = {'e' : 101, 'f' : 102, 'g' : 103, 'h' : 104}

lilAscii = merge(lilAscii, lilAscii_2)

print(lilAscii)


