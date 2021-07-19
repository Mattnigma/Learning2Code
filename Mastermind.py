#!/usr/bin/env python3

#importing stuff
from random import seed
from random import randint
seed()

#game rules
pegs=4
chances=10

#setup of gameboard and master code
mastercode=[0 for i in range(pegs)]
y=0
for x in mastercode:
    mastercode[y]=randint(1,6)
    y+=1
x=pegs+1
y=chances+1
gameboard=[[0 for i in range(x)] for j in range(y)]
gameboardn=gameboard
n=0
for i in range(pegs):
    gameboard[chances][n]="?"
    n+=1
n=0
for i in range(y):
    gameboard[n][pegs]="?"
    n+=1
n=0

print(mastercode)

guess=input("guess here please\n")
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

print(guesscode)

y=0
x=0
z=0
gameboardn[n]=guesscode
macop=mastercode
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
answer=[0 for i in range(y)]
y=0
for i in answer:
    if z>1:
        answer[y]="z"
    else:
        answer[y]="w"
    y+=1
















for line in gameboardn:
    print(*line)
print(answer)
print(guesscode
)