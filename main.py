"""
BlueWall calcul modules
Multi-fonctions
H!PED Official
"""

def add(a=1, b=1):
    return a + b


def mul(a=1, b=1):
    return a * b


def div(a=1, b=1):
    return a / b

def addi(a=0, b=0):
    a = int(input("First number :\n"))
    b = int(input("Second number :\n"))
    return a + b


def muli(a=1, b=1):
    a = int(input("First number :\n"))
    b = int(input("Second number :\n"))
    return a * b


def divi(a=1, b=1):
    a = int(input("First number :\n"))
    b = int(input("Second number :\n"))
    if a == 0:
        print("Cannot divide by 0")
    elif b == 0:
        print("Cannot divide by 0")


    return a / b