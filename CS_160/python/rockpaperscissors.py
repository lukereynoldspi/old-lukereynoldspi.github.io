import random
z = random.randint(1,3)
y = 0
print ("---------------------------------------------------------------------------------")
print  ("Rock, Paper, Scissors!")
print  ("I have made my choice. Make YOURS:")
print ("---------------------------------------------------------------------------------")
x = input()
print ("---------------------------------------------------------------------------------")
if x == "Rock":
    y = 1
if x == "Paper":
    y = 2
if x == "Scissors":
    y = 3
if x == "rock":
    y = 1
if x == "paper":
    y = 2
if x == "scissors":
    y = 3
print ("3")
print ("2")
print ("1")
print ("GO!")
print ("---------------------------------------------------------------------------------")
if z == 1:
    if y == 1:
        print ("TIE")
    if y == 2:
        print ("You lose, I chose rock :)")
    if y == 3:
        print ("You win, I chose rock :(")

if z == 2:
    if y == 1:
        print ("TIE")
    if y == 2:
        print ("You lose, I chose paper :)")
    if y == 3:
        print ("You win, I chose paper :(")

if z == 3:
    if y == 1:
        print ("TIE")
    if y == 2:
        print ("You lose, I chose scissors :)")
    if y == 3:
        print ("You win, I chose scissors :(")
