# Write a program to create a dictionary of hindi language

'''
myDict = {
    "pakha": "fan",
    "bari": "House",
    "khata": "paper",
}
print("Your options are: {}".format(myDict.keys()))


## Another Question
bangla = input("Enter the word: ")
print("The meaning of the word is: ", myDict.get(bangla))

num = set()

for i in range(0, 8):
    num.add(int(input("Enter the {} number of words: ".format(i+1))))

print(num)
'''
sub1 = int(input("Enter first subject marks: "))
sub2 = int(input("Enter second subject marks: "))
sub3 = int(input("Enter third subject marks: "))

if (sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("\nYou are fail because you have less than 33% in one of the subjects")
elif (sub3+sub2+sub1)/3 < 40:
    print("\nYou are fail due to total percentage less than 40")
else:
    print("\nCongratulations!! \n\t\tYou passed th exam")
