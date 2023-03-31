import math

def Menu():
    print('===============================================')
    print('1 for Km to M, 2 for Reverse')
    print('3 for M to cm, 4 for Reverse')
    print('5 for cm to mm, 6 for Reverse')
    print('7 for Celcius to Fahrenheit, 8 for Reverse')
    print('9 for Period of a pendulum')
    print('10 for Length of a pendulum')
    print('===============================================')

def KMtM():
    print('You selected Km to m')
    num = float(input('Enter value km: '))
    num1 = round(num*1000, 1)
    print('{}m' .format(num1))
    num = ''

def MtKM():
    print('You selected m to Km')
    num2 = float(input('Enter value m: '))
    num3 = round(num2/1000, 1)
    print('{}km' .format(num3))
    num2 = ''

def MtCM():
    print('You selected m to cm')
    num4 = float(input('Enter value m: '))
    num5 = round(num4*100, 1)
    print('{}cm' .format(num5))
    num4 = ''

def CMtM():
    print('You selected cm to m')
    num6 = float(input('Enter value cm: '))
    num7 = round(num6/100, 1)
    print('{}m' .format(num7))
    num6 = ''

def CMtMM():
    print('You selected cm to mm')
    num8 = float(input('Enter value cm: '))
    num9 = round(num8*10, 1)
    print('{}mm' .format(num9))
    num8 = ''

def MMtCM():
    print('You selected mm to cm')
    num10 = float(input('Enter value mm: '))
    num11 = round(num10/10, 1)
    print('{}cm' .format(num11))
    num10 = ''

def CtF():
    print('You selected Celcius to Fahrenheit')
    num12 = float(input('Enter value C: '))
    num13 = round((num12*1.8)+32, 1)
    print('{} Fahrenheit' .format(num13))
    num12 = ''

def FtC():
    print('You selected Fahrenheit to Celcius')
    num14 = float(input('Enter value F: '))
    num15 = round((num14/1.8)-32, 1)
    print('{} Celcius' .format(num15))
    num14 = ''

def pendulum():
    print('You selected Period of a Pendulum')
    g = 9.8
    d = float(input('Enter length of Pendulum in Meters '))
    T = round(2*math.pi*(math.sqrt(d/g)), 2)
    print('{} seconds' .format(T))
    d = ''

def pendulum2():
    print('You selected Length of a Pendulum')
    g = 9.8
    T = float(input('Enter Period of the Pendulum in Seconds '))
    L = round(g*(T/(2*math.pi))**2, 2)
    print('{} Meters' .format(L))

def Ifstates():
    if input1 == 1:
        KMtM()
    if input1 == 2:
        MtKM()
    if input1 == 3:
        MtCM()
    if input1 == 4:
        CMtM()
    if input1 == 5:
        CMtMM()
    if input1 == 6:
        MMtCM()
    if input1 == 7:
        CtF()
    if input1 == 8:
        FtC()
    if input1 == 9:
        pendulum()
    if input1 == 10:
        pendulum2()
    if input1 >= 11:
        print('Unidentified Number Please Try Again')
    

Menu()
input1 = int(input())
Ifstates()
