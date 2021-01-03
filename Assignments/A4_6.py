#6. Write a python script to generate and print a dictionary that contains a
#number (between 1 and n) in the form (x: x*x)

def generate_dict(n):
    gen_dict = {}
    for x in range(1, n+1):
        gen_dict[x] = x*x

    return gen_dict

print(generate_dict(5))
