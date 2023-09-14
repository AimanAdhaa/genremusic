#!/usr/bin/env python

import random

def main():
    """Start a genre guessing game."""
    print("Guess the genre!")

    genre = [
        "pop",
        "hip hop",
        "rock",
        "rhythm and blues",
        "soul",
        "reggae",
        "funk"
        ]

       
    x = random.choice(genre)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What genre am I thinking of? "))
    
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
            print("You Have 3 chance to guessed that genre!.Please try again!".format(guess))
            
        guess = str(input("What genre am I thinking of? "))
    
        if x == guess:
            print("You guessed {}.Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
            print("You Have 2 chance to guessed that genre!.Please try again!".format(guess))
        
        guess = str(input("What genre am I thinking of? "))
        
        if x == guess:
            print("You guessed {}.Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
            print("You Have 1 chance to guessed that genre!.Please try again!".format(guess))
            
        guess = str(input("What genre am I thinking of? "))  
        
        if x == guess:
            print("You guessed {}.Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
            print("You Have NO chance to guessed that genre!.Thank you for try to answer this genre !".format(guess))
            print("Time is over:)")
        
main()