"""
encontrar los números repetidos de una lista
"""

num = [2,3,1,4,6,7,8,5,4,9,3]

repeated = []
file = []

for n in num:
    if n not in file:
        file.append(n)
    else:
        repeated.append(n)

print("the repeated numbers are:", repeated)
print("", file)
print("")

