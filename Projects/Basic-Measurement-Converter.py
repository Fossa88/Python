def Menu():
    print('===============================================')
    print('1 for Km to M, 2 for Reverse')
    print('3 for M to cm, 4 for Reverse')
    print('5 for cm to mm, 6 for Reverse')
    print('7 for Celcius to Fahrenheit, 8 for Reverse')
    print('===============================================')

def KMtM():
    num = int(input())
    num1 = num/1000
    print(num1 + 'M')
    num = ''

def MtKM():
    num = int(input())
    num1 = num*1000
    print(num1 + 'Km')
    num = ''

def MtCM():
    num = int(input())
    num1 = num/100
    print(num1 + 'cm')
    num = ''

def CMtM():
    num = int(input())
    num1 = num*100
    print(num1 + 'M')
    num = ''

def CMtMM():
    num = int(input())
    num1 = num/10
    print(num1 + 'mm')
    num = ''

def MMtCM():
    num = int(input())
    num1 = num*10
    print(num1 + 'Km')
    num = ''

def CtF():
    num = int(input())
    num1 = (num*1.8)+32
    print(num1 + ' Fahrenheit')
    num = ''

def FtC():
    num = int(input())
    num1 = (num/1.8)-32
    print(num1 + ' Celcius')
    num = ''


Menu()
input = int(input())
print(input)


if input == 1:
        KMtM()
elif input == 2:
        MtKM()
elif input == 3:
        MtCM()
elif input == 4:
        CMtM()
elif input == 5:
        CMtMM()
elif input == 6:
        MMtCM()
elif input == 7:
        CtF()
elif input == 8:
        FtC()