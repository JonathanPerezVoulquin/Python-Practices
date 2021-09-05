for i in "academia":
    for e in i:
        print(i.split())


#list and numbers
numbers = [52, 44, 105, 34, 17, 97, 45, 2, 78, 66]
print(numbers)
#reverse numbers
newList = numbers[::-1]
print(newList)


#find the index of a number from a list
file = 52

for j in range(len(numbers)):
    if numbers[j] == file:
       print("the number", file, "is in the position:", j)

