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
    try:
        button = buttons[index]

        
        amount = button.price
        items = button.amount

        if playerBank.enoughMoney(amount, items):
            playerBank.withdraw(amount)
            button.amount += 1

    except TypeError:
        pass

