
# Print Max number using own function

def maximum(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c


def print_max_number():
    m = maximum(2, 555, 60)
    print("The maximum number is "+str(m))


print_max_number()
