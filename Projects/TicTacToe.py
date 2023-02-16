import random
Random = random.randint(1,2)
if Random == 1:
        turn1 = 'X'
elif Random == 2:
        turn1 = 'O'
        # if Random = 1 X turn, if Random = 2 O turn

bruhBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in bruhBoard:
    board_keys.append(key)

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
                Bruh()

def drawBoard2(Board):
        print("========================================")

        print(Board['1'] + '|' + Board['2'] + '|' + Board['3'])
        print("-----")
        print(Board['4'] + '|' + Board['5'] + '|' + Board['6'])
        print("-----")
        print(Board['7'] + '|' + Board['8'] + '|' + Board['9'])

        print("========================================")

print("- - - - -")
print("Welcome to the TicTacToe Game by Fossa")
print("To Hear the Rules Input 1, To Start the Game Input 2 ")
print("- - - - -")

def Bruh(): 

        turn = turn1
        count = 0

        for t in range(10):
                drawBoard2(bruhBoard)
                print('it is ' + turn + '\'s turn \nPlease input a number!')

                Turn = input()

                if bruhBoard[Turn] == ' ':
                        bruhBoard[Turn] = turn
                        count += 1
                else:
                        print("That space is already occupied.\nPlease select another place.")
                        continue

                # Win conditions
                if count >= 5:
                        if bruhBoard['1'] == bruhBoard['2'] == bruhBoard['3'] != ' ':
                                drawBoard2(bruhBoard)
                                print('\n' + turn + ' wins the game')
                                break
                        elif bruhBoard['1'] == bruhBoard['5'] == bruhBoard['9'] != ' ':
                                drawBoard2(bruhBoard)
                                print('\n' + turn + ' wins the game')
                                break
                        elif bruhBoard['1'] == bruhBoard['4'] == bruhBoard['7']:
                                drawBoard2(bruhBoard)
                                print('\n' + turn + ' wins the game')
                                break
                        elif bruhBoard['2'] == bruhBoard['5'] == bruhBoard['8']:
                                drawBoard2(bruhBoard)
                                print('\n' + turn + ' wins the game')
                                break
                        elif bruhBoard['4'] == bruhBoard['5'] == bruhBoard['6']:
                                drawBoard2(bruhBoard)
                                print('\n' + turn + ' wins the game')
                                break
                        elif bruhBoard['3'] == bruhBoard['6'] == bruhBoard['9']:
                                drawBoard2(bruhBoard)
                                print('\n' + turn + ' wins the game')
                                break
                        elif bruhBoard['3'] == bruhBoard['5'] == bruhBoard['7']:
                                drawBoard2(bruhBoard)
                                print('\n' + turn + ' wins the game')
                                break
                        elif bruhBoard['7'] == bruhBoard['8'] == bruhBoard['9']:
                                drawBoard2(bruhBoard)
                                print('\n' + turn + ' wins the game')
                                break
                        if count == 9:
                                print("\nIt's a Tie!!\n")
                                
        #turn swap            
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'   


                



Invar = int(input())
if Invar == 1:
    drawBoard1()
elif Invar == 2:
    Bruh()


        
