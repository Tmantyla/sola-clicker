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

        if button.type == 'clicker':
            amount = button.clickerAmount
            
            playerBank.balance += amount

        elif button.type == "idle":
            price = button.price
            
            if playerBank.enoughMoney(price):
                button.amount += 1
                playerBank.withdraw(price)
                button.increasePrice()
                
            

        elif button.type == 'upgrade':
            price = button.price
            
            if playerBank.enoughMoney(price):
                if button.amount <= 1:
                    button.amount = 1
                    buttons[0].clickerAmount *= 32
                    playerBank.withdraw(price)
                    button.price *= 'n'

        

    except TypeError:
        pass

def calcIncr():
    increase = ( 
        buttons[5].amount * 1
        + buttons[6].amount * 200
        + buttons[7].amount * 40000
        + buttons[8].amount * 8000000
    )
        
    return increase

def drawInfo():
    pg.draw.rect(screen, (255, 0, 0), ((size[0] - buttonWidth * 0.5) // 2, size[1] // 24, buttonWidth * 0.5, buttonHeight // 2))
    
    clickPower = buttons[0].clickerAmount
    clickPowerStr = f"Click Power: {clickPower:,}"
    clickPower = font.render(clickPowerStr, True, BLACK)
    
    solaPerSecond = 30 * calcIncr()
    solaPerSecondStr = f"SPS: {solaPerSecond:,}"
    solaPerSecond = font.render(f"SPS: {solaPerSecondStr}", True, BLACK)

    screen.blit(clickPower, ((size[0] - buttonWidth * 0.5) // 2, size[1] // 24))
    screen.blit(solaPerSecond, ((size[0] - buttonWidth * 0.5) // 2, size[1] // 13))
    