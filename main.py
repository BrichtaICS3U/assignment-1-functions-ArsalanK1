# Assignment 1
# ICS3U
# <Arsalan. K>
# March 28, 2018


M = str(input('Converting from Celcius or Fahrenheit: '))
if M == 'Celcius':
    print (CtoF ())
else:
    print (FtoC ())


def CtoF ():
    C = int(input('Enter your temperature in Celsius: '))
    while C > -273.15:
        F = (1.8)*C+32
        return round(F)
        break
    else:
        C = int(input('The entered value is invalid. Please enter a different value: ')

def FtoC ():
    F = int(input('Enter your temperature in Fahrenheit: '))
    while F > -459.67:
        C = (0.55556)*(F-32)
        return round(C)
        break
    else:
        F = int(input('The entered value is invalid. Please enter a different value: ')
