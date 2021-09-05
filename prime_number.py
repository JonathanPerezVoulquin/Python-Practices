a = 3473


def primeNumber(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
            print(i)
    if count == 2:
        return True
    else:
        return False


print(primeNumber(a))
print(primeNumber(122))
print(primeNumber(743))  # prime_number

"""
Another way
"""


def primeNumber2(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(primeNumber2(743))
