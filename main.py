# Assignment 1
# ICS3U
# <Arsalan>
# March 28, 2018

###### uncomment this when you are ready to work on it
def CtoF ():
    C = int(input('Enter your temperature in Celsius: '))
    F = (1.8)*C+32
    return round(F)

###### uncomment this when you are ready to work on it
def FtoC ():
    F = int(input('Enter your temperature in Fahrenheit: '))
    C = (0.55556)*(F-32)
    return round(C)

def Conversion ():
    M = str(input('Enter the measurment to be converted from: '))
    if M == 'Celsius':
        C = int(input('Enter your temperature in Celsius: '))
        F = (1.8)*C+32
        return round(F)
    else:
        F = int(input('Enter your temperature in Fahrenheit: '))
        C = (0.55556)*(F-32)
        return round(C)
