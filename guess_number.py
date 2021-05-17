"""
write a program in which asks user to enter a number between 1, 99
and at the same time program will think of a number
if both the numbers are same then the program will end 
otherwise it wii ask user for a number to enter
"""

import random

def main():
    # getting the guesses
    user_guess = get_user_guess()
    ai_guess = get_ai_guess()
    # validating the guess
    count = checking_guess(user_guess,ai_guess)
    # declaring the result
    declaring_result(count)

def get_user_guess():
    print("I'm expecting a number between 1 and 99")
    guess = int(input("enter the guess: "))
    return guess

def get_ai_guess():
        return random.randint(1, 99)

def checking_guess(user_guess,ai_guess):
    count = 1
    # while the user input and the random number is not equal
    # we have to tell that whether the guess number is higher or lower than the random number generated
    while user_guess != ai_guess :
        if user_guess > ai_guess :
            print("That is high")
            count += 1
        elif ai_guess > user_guess :
            print("That is low")
            count += 1
        print("")
        # we have to call user_guess function again to take the user guess
        user_guess = get_user_guess()
    return count

def declaring_result(count):
    print("congrats you have made right guess!")
    print("You took "+str(count)+" chance to make the correct guess!")

# telling python to call main when program starts
if __name__ == '__main__' :
    main()

