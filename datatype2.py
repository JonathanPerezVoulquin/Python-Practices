# Implicit Type Conversion
num_int = 127
num_float = 12.05
print(num_int)
print("datatype of num_int:", type(num_int))
print(num_float)
print("datatype of num_float:", type(num_float))

new_num = num_int + num_float
print(type(new_num))

print("datatype of new_num:", type(new_num))

print("---------------0---------------")

# Addition of string (higher) data type and integer (lower) datatype
num_int = 124
num_str = "456"
print(num_int, num_str)
print("data type of num_int:", type(num_int), "num:", num_int)
print("data type of num_str:", type(num_str), "num:", num_str)

# print(num_int + num_str) ERROR, NO SE PUEDE CONCATENAR UN INT CON UN STR #convertirlo.
concat = print(num_int + int(num_str))
print("data type of concat is:", type(concat))
print("--------------0------------------")

# Explicit Type Conversion IMPORTANT
num_int = 123
num_str = "456"

print(type(num_int))
print(type(num_str))

num_str = int(num_str)  # Converting string to int
print("Data type of num_str after Type Casting:", type(num_str))

num_sum = num_int + num_str

print("sum of num_int and num_str:", num_sum)
print("Data type of the sum is:", type(num_sum))
