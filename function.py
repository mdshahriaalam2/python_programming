marks = [45, 25, 36, 25, 36, 26, 28, 39]


def avg(marks):
    return sum(marks)/len(marks)


def sum_marks(marks):
    return sum(marks)


print(avg(marks))
print(sum_marks(marks))


################### Fantastic functions #################################

def print_name(name="Stranger"):  # Default parameter value
    if (name == "Stranger"):
        print("Your are a " + name)
    else:
        print("Your name is : "+name)


print_name()
