# Snake, Water, Gun Game
import random
rint = random.randint(1, 3)

# Function for validating the user and the computer
def game(rint, usr):
    if rint == 1:
        com = 's'
    elif rint == 2:
        com = 'w'
    else:
        com = 'g'
    
    # check the conditions of the game
    if com == usr:
        return True
    elif com != usr:
        return False
    else:
        pass

def check_input(user):
    if any(char in user for char in ('s', 'g', 'w')):
        return True
    else:
        return False

# Take input from the User
def get_input():
    user = input("Your Turn: Snake(s) Water(w) Gun(g) ?")
    return user

if check_input(get_input())   == True:
    if game(rint, get_input()):
        print("Hurray!!! You won the game")
    else:
        print("Ohh No! You Lose the game")
else:
    print("Invalid Input Please try again.")
    get_input()
    