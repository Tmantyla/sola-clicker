from objects import Button, Account
from style import *

buttonSizes = [
    [buttonWidth * 0.4, buttonHeight // 0.375],
    [buttonWidth, buttonHeight], 
    [buttonWidth, buttonHeight],
    [buttonWidth, buttonHeight],
    [buttonWidth, buttonHeight],
]

buttonPositions = [
    [(size[0] - buttonSizes[0][0]) / 2 , (size[1] - buttonSizes[0][1]) / 2],
    [gap, gap], 
    [gap, 2 * gap + buttonHeight],
    [gap, 3 * gap + 2* buttonHeight],
    [gap, 4 * gap + 3 * buttonHeight],
]

names = [
    "click",
    "0,33L sola",
    "0,5L sola",
    "1,0L sola",
    "1,5L sola",
]

prices = [
    0,
    100,
    10000,
    1000000,
    100000000,
]

types = [
    "clicker",
    "clickUpgrade",
    "clickUpgrade",
    "clickUpgrade",
    "clickUpgrade",
]

buttons = []

for i in range(len(buttonPositions)):
    buttons.append(Button(i, 
    buttonPositions[i], 
    buttonSizes[i], 
    images[i][0], 
    images[i][1], 
    prices[i], 
    types[i],
    names
))




def drawButtons():
    for i in range(len(buttons)):
        buttons[i].draw()