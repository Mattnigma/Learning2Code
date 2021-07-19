#!/usr/bin/env python3

#importing stuff
from random import seed
from random import randint
seed()
highnumber=10
chances=3

print("Guess the number between 1 and "+str(highnumber)+"!")
guessvar = randint(1,highnumber)

def get_valid_input():
    stab=input(str(chances)+" chances left!\n")
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
            print("you lose")
        elif stab>guessvar:
            print("Too high!")
        else:
            print("Too low!")
        print("Try again!")