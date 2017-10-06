import random
import math

# Myles D
# config
default_low = 1
default_high = 100



# helper functions
def show_start_screen():
    print("""
    ********************************************************************************************
    ################################### Myles Daniels ##########################################
    ********************************************************************************************

    """)



    
    

def show_credits():
    print()
    print("""
    """)

def find_limit(current_high, current_low):
    limit = math.ceil(math.log((current_high - current_low) + 1, 2))
    return limit
    
def get_guess(current_low, current_high):
    guess = ( current_high + current_low)//2
    return guess

def decide_number(default_low,default_high):
    print()
    decide_1 = input("Hello " + str(name) + ", would you like to pick the numbers for your game? ")
    decide_1 = decide_1.lower()
    if decide_1 in ["Yes","yes","yeah","y", ]:
        print()
        low = input("what is the lowest number? ")
        low = int(low)
        print()
        high = input("What is the highest number? ")
        high = int(high)
        
    else:
        print("That's ok we will just use other settings.")
        print()
        low = default_low
        high = default_high

    return low,high

def pick_number (current_low, current_high):
    print()
    print (name + " think of a number between " + str(current_low) + " and " + str(current_high) + ".")
    print("Press 'enter' when done.")
    useless_1 = input ()
  

def check_guess(guess,tries,limit):
    print("The number is....")
    print(str(guess) + "?")
    print("I have guessed " + str(tries) + "/" + str(limit) + " times")
    test = input("Tell me if the number is too high, too low, or if I guessed correct, " + name + ". " )
    test = test.lower()
    print()
    
    if test in ["low", "higher","too low", "l"]:
        check = 1
        return check
    if test in ["high", "lower", "too high", "h"]:
        check = -1
        return check
    if test in ["correct", "Correct", "yes", "Yes", "y" "Y"]:
        check = 0
        return check
    else:
        print("Eneter a correct repsponse or it makes you a loser.")
      

def show_result(guess,tries,limit):
    print()
    print("I guessed your number in only " + str(tries) + "/" + str(limit) + " tries.")
    print()
    print("got you" + str(guess) + " was such an easy number to guess.")
    print("You're crazy " + name + ", You suck")
 

def play_again(name):
    while True:
        print()
        decision = input("Would you like to play again " + name + "? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            print()
            return True
        elif decision == 'n' or decision == 'no':
            print()
            print("alright, goodbye. Good luck " + name + " if you play another game, you will need it.")
            return False
        else:
            print("Not valid. Please enter 'y' or 'n'.")

def play(name):
    current_low, current_high = decide_number(default_low,default_high)
    check = -1
    tries = 1

    pick_number(current_low, current_high)
    limit = find_limit(current_high,current_low)
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess,tries,limit)

        if check == -1:
            current_high = guess
         
        elif check == 1:
            current_low = guess

        tries +=1

    show_result(guess,tries,limit)


# Game starts running here
show_start_screen()

playing = True

while playing:
    name = input("Hello, welcome to Guess a Number A.I. What is your name? ")
    play(name)
    playing = play_again(name)

show_credits()
