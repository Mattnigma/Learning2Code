#!/usr/bin/env python3

#importing stuff
from math import factorial
from random import seed
from random import randint
seed()

#game rules
pegs=4
chances=10

def number2color(number):
    CRED  = '\33[91m'
    CGRE  = '\33[32m'
    CYLW  = '\33[33m'
    CBLU  = '\33[34m'
    CPNK  = '\33[35m'
    CWTE  = '\33[37m'
    CEND  = '\33[00m'
    number_color_map={
        0: ".",
        1: CRED+"R"+CEND,
        2: CGRE+"G"+CEND,
        3: CYLW+"Y"+CEND,
        4: CBLU+"B"+CEND,
        5: CPNK+"P"+CEND,
        6: CWTE+"W"+CEND,
        "x": CRED+"X"+CEND,
        "z": CWTE+"O"+CEND,
    }
    return number_color_map.get(number) or number

def welcome():
    print("Welcome to Mastermind! Please enter a guess, or type \"help\" for help!\nYou have "+str(chances)+
    " chances to guess a series of "+str(pegs)+" pegs of any of 6 colors!")

def print_board(_board):
    print("")
    rendered_board=[]
    board=_board.copy()
    board.append(["?" for i in range(pegs)])
    index2=0
    for row in board:
        rendered_row=[]
        # row = [1, 2, 3, 4]
        index=0
        for item in row:
            rendered_row.append(number2color(item))
            if index== pegs-1  and index2<chances:
                rendered_row.append("|")
            index+=1
            # TODO if on peg-th - 1 item, append a '|' after
        index2+=1
        rendered_board.append(" ".join (rendered_row))
    rendered_board.reverse()
    for row in rendered_board:
        print(row)  

def check_win():
    if x==4:
        print("Game over! You win!")
        return(1)
    elif n==chances:
        print("Game over! You lose!")
        return(1)
    else:
        return(0)

def test_input(guess):
    test=True
    if len(guess)==4:
        coded_test=codify_guess(guess)
        for color in coded_test:
            if color==0:
                test=False
                break
    else:
        test=False
    if test== True:
        return True
    else:
        return False

def get_valid_input():
    guess=input("\n"+guiding_letters+"\n\n")
    while test_input(guess)==False:
        if guess=="help" or guess=="Help" or guess=="HELP":
            print(help_message)
            guess=input("\n"+guiding_letters+"\n\n")
        else:
            guess=input("Invalid input, please try again\n\n")
    return guess

def codify_guess(guess):
        # guess = "rgby"
    y=0
    guesscode=[0 for i in range(pegs)]
    for i in guess:
        if i =="r" or i=="R":
            guesscode[y]=1
        elif i=="g" or i=="G":
            guesscode[y]=2
        elif i=="y" or i=="Y":
            guesscode[y]=3
        elif i=="b" or i=="B":
            guesscode[y]=4
        elif i=="p" or i=="P":
            guesscode[y]=5
        elif i=="w" or i=="W":
            guesscode[y]=6
        y+=1
    # guesscode = [1, 2, 4, 3]
    return(guesscode)

help_message="\nMastermind is a famous strategic guessing game. In this solitaire version, you are challenged to guess \n\
a randonly generated sequence of pegs (represented here by letters), from 6 colors: Red, Yellow, Green, Blue, Purple, \n\
and White. You can start by guessing any 4 colors by entering in four letters that correspond to the six colors. \n\
When you hit \"enter,\"you will see an updated gameboard that shows all your guesses so far along with a response \n\
for each guess. The response will contain a red \"X\" for each time you guessed the correct colored peg in the correct \n\
space, and a white \"O\" for every time you guess a correctly collored peg in the wronng spot. Multiple answer pegs will \n\
never correspond to one of your guessing pegs, and if one of your peg can be thought of as both in the correct and \n\
incorrect locations, it will always be marked as fully correct. The code you're trying to guess could be four  of the \n\
same color, four diferent colors, or anything inbetween. Remember to always question your assumptions! Good Luck!"




#setup of gameboard and master code
mastercode=[0 for i in range(pegs)]
y=0
endgame=0
for x in mastercode:
    mastercode[y]=randint(1,6)
    y+=1
x=pegs+2
x2=pegs+1
y=chances+1
gameboard=[[0 for i in range(pegs)] for j in range(chances)]
n=0
guiding_numbers=[1,2,3,4,5,6]
guiding_letters=""
for number in guiding_numbers:
    guiding_letters+=number2color(number)


welcome()
for chance in range(chances):
    guess=get_valid_input()
    guesscode=codify_guess(guess)
    y=0
    x=0
    z=0
    gameboard[n]=guesscode.copy()
    macop=mastercode.copy()
    for i1 in guesscode:
        if guesscode[y]==macop[y]:
            x+=1
            macop[y]=0
            guesscode[y]=-1
        y+=1

    y1=0
    for i1 in guesscode:
        y2=0
        for i2 in macop:
            if guesscode[y1]==macop[y2]:
                z+=1
                macop[y2]=0
                guesscode[y1]=-1
            y2+=1
        y1+=1

    y=x+z
    correct_guess=x
    answer=[0 for i in range(y)]
    y=0
    for i in answer:
        if correct_guess>0:
            answer[y]="x"
            correct_guess-=1
        else:
            answer[y]="z"
        y+=1

    gameboard[n].extend(answer)
    n+=1


    print_board(gameboard)

    endgame=check_win()
    if endgame==1:
        break