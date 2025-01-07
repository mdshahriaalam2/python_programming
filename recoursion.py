# This is very important for programming

# print factorial using def()

def factorial_iter(n):
    product = 1
    for i in range(n):
        product *= (i+1)
    return product

# Recursion Function

# n! = n * (n-1)!

# factorial using recursion function


def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)


# sum using recursion function
def sum_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n + sum_recursive(n-1)


print(sum_recursive(4))
