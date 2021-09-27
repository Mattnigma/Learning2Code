#!/usr/bin/env python3

#importing stuff
from random import seed
from random import randint
seed()
highnumber=1000
chances=10

print("Guess the number between 1 and "+str(highnumber)+"! You have "+str(chances)+" chances!")
guessvar = randint(1,highnumber)

def get_valid_input():
    stab=input("\n")
    while stab.isdigit() == False:
        stab=input("Invalid input, please try again\n")
    return int(stab)


while chances > 0:
    stab=get_valid_input()
    chances-=1
    if guessvar==stab:
        print("YOU WIN")
        chances=0
    else:
        if chances==0:
            print("\nYou lose. The number was "+str(guessvar)+".")
            break
        elif stab>guessvar:
            print("\nToo high!")
        else:
            print("\nToo low!")
        if chances==1:
            print("\nLast chance!")
        else:
            print("Try again! You have "+str(chances)+" tries left!")