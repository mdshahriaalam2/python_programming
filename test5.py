# While loop
# i = 0

# while i < 10:
#     print("Yes "+str(i+1))
#     i += 1
# print("Done")

# for loop

# l = [1, 7, 8, 9, 4]
# l = set(l)
# for i in l:
#     print(i)


# print factorial

num = int(input("enter the number of factorial: "))

fact = 1
sum = 0
for i in range(1, num+1):
    fact *= i
    sum += i
print(f"Factorial of {num} is " + str(fact) + "\n")
print(f"Summation of {num} is " + str(sum))
