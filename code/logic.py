import pygame as pg
from buttons import *

playerBank = Account()

def press():
    mousePos = pg.mouse.get_pos()
    for i in range(len(buttonPositions)):
        if buttonPositions[i][0] <= mousePos[0] <= buttonPositions[i][0] + buttonSizes[i][0] and buttonPositions[i][1] <= mousePos[1] <= buttonPositions[i][1] + buttonSizes[i][1]:
                buttons[i].press()
                return i

def getButton(index):
    try:
        return names[index]
    except TypeError:
        return None


def whenPress():
    index = press()
    button = buttons[index]
    
    amount = button.price

    if playerBank.enoughMoney(amount):
        playerBank.withdraw(amount)
        button.amount += 1