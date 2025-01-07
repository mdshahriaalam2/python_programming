letter = '''
Dear <.name.>,
Greetings from asrn team. I am happy to tell you about your selections. 
You are selected! 
Have a great day ahead!
Thanks and regards,
Shifat

Date: <.date.>\n'''

name = input("Enter your name: ")
date= input("Enter your Date: ")
print('\n')

letter = letter.replace("<.name.>", name)
letter = letter.replace("<.date.>", date)
duble = letter.find("  ") #Find double spaces in string

print(letter)

if duble==-1:
    print("Not found")
else:
    print("Found")