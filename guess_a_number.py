import random
import math
import string
# config
low = 1
high = 10
limit = math.ceil((math.log(high-low+1, 2)))

# helper functions
def show_start_screen():
    print("""
 _______  __   __  _______  _______  _______   _______   __    _  __   __  __   __  _______  _______  ______    __  
|       ||  | |  ||       ||       ||       | |   _   | |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |  |  | 
|    ___||  | |  ||    ___||  _____||  _____| |  |_|  | |   |_| ||  | |  ||       || |_|   ||    ___||   | ||  |  | 
|   | __ |  |_|  ||   |___ | |_____ | |_____  |       | |       ||  |_|  ||       ||       ||   |___ |   |_||_ |  | 
|   ||  ||       ||    ___||_____  ||_____  | |       | |  _    ||       ||       ||  _   | |    ___||    __  ||__| 
|   |_| ||       ||   |___  _____| | _____| | |   _   | | | |   ||       || ||_|| || |_|   ||   |___ |   |  | | __  
|_______||_______||_______||_______||_______| |__| |__| |_|  |__||_______||_|   |_||_______||_______||___|  |_||__| 
         """)

def show_credits():
    print("googbye made by Myles Daniels")
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +". You will get " + str(limit) + " tries to guess the right answer!")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print("You win!")
    else:
        print("You are such a loser! The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ").lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.").lower()

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        print()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()
print()
print()
playing = True

while playing:
    play()
    playing = play_again()
print()
print()
show_credits()
