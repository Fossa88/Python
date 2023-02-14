    # Example page learning from https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874

import random
Random = random.randint(1,2)
        # if Random = 1 X turn, if Random = 2 O turn

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

def drawBoard1():
        print("Player 1 will be playing as X's and player 2 will be playing as O's. The first move will be randomly selected at the start of the game.")
        print("To input a move you will be prompted to type in a number corrisponding to the grid. That will then input your symbol into that spot.")
        print("========================================")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print("========================================")
        Y = int(input("Input 1 to start the game: "))
        if Y == 1:
                drawBoard2()

def drawBoard2(Board):
        print("========================================")

        print(Board['1'] + '|' + Board['2'] + '|' + Board['3'])
        print("--------")
        print(Board['4'] + '|' + Board['5'] + '|' + Board['6'])
        print("--------")
        print(Board['7'] + '|' + Board['8'] + '|' + Board['9'])

        print("========================================")

print("- - - - -")
print("Welcome to the TicTacToe Game by Fossa")
print("To Hear the Rules Input 1, To Start the Game Input 2 ")
print("- - - - -")

Invar = int(input())
if Invar == 1:
    drawBoard1()
elif Invar == 2:
    drawBoard2()

def Bruh(): 

        if Random == 1:
                turn = 'X'
        elif Random == 2:
                turn = 'O'

        if turn == 'X':
                
