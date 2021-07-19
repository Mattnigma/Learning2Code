#!/usr/bin/env python3

#importing stuff
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

def print_board(_board):
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

#setup of gameboard and master code
mastercode=[0 for i in range(pegs)]
y=0
for x in mastercode:
    mastercode[y]=randint(1,6)
    y+=1
x=pegs+2
x2=pegs+1
y=chances+1
gameboard=[[0 for i in range(pegs)] for j in range(chances)]
n=0




for chance in range(chances):
    guess=input("guess here please\n")
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

    print(x,z)

    y=x+z
    answer=[0 for i in range(y)]
    y=0
    for i in answer:
        if x>0:
            answer[y]="x"
            x-=1
        else:
            answer[y]="z"
        y+=1

    gameboard[n].extend(answer)
    n+=1


        




    print_board(gameboard)
