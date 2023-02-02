print("- - - - - - - - - - - - - - - - - - - - - - - - -")
print("Computer Plays Rock Paper Scissors Against Itself")
print("=================================================")

import random
Ranblue = random.randint(1,3)
Ranred = random.randint(1,3)
Ranblue1 = ""
Ranred1 = ""

if Ranblue == 1:
    Ranblue1 = "Scissors"
elif Ranblue == 2:
    Ranblue1 = "Paper"
elif Ranblue == 3:
    Ranblue1 = "Rock"

if Ranred == 1:
    Ranred1 = "Scissors"
elif Ranred == 2:
    Ranred1 = "Paper"
elif Ranred == 3:
    Ranred1 = "Rock"

blue = Ranblue
red = Ranred

print('Blue team has ' + Ranblue1)
print('Red team has ' + Ranred1)
if Ranblue1 == Ranred1:
    print("The game is a tie")

if Ranblue1 == "Scissors":
    if Ranred1 == "Rock":
        print("The red team wins the game")
    elif Ranred1 == "Paper":
        print("The blue team wins the game")

if Ranblue1 == "Rock":
    if Ranred1 == "Paper":
        print("The red team wins the game")
    elif Ranred1 == "Scissors":
        print("The blue team wins the game")

if Ranblue1 == "Paper":
    if Ranred1 == "Scissors":
        print("The red team wins the game")
    elif Ranred1 == "Rock":
        print("The blue team wins the game")

print("=================================================")
