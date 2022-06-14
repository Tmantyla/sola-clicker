from objects import Button, Account
from style import *

buttonSizes = [
    [buttonWidth * 0.4, buttonHeight // 0.375],
    [buttonWidth, buttonHeight], 
    [buttonWidth, buttonHeight],
    [buttonWidth, buttonHeight],
    [buttonWidth, buttonHeight],
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
    [size[0] - (gap + buttonWidth), gap], 
    [size[0] - (gap + buttonWidth), 2 * gap + buttonHeight],
    [size[0] - (gap + buttonWidth), 3 * gap + 2* buttonHeight],
    [size[0] - (gap + buttonWidth), 4 * gap + 3 * buttonHeight],
]

names = [
    "click",
    "0,5L Sola™",
    "1,0L Sola™",
    "1,5L Sola™",
    "2,0L Sola™",
    "Sola™-pyörä",
    "Sola™-mobiili",
    "Sola™-rekka",
    "Sola™-laiva"
]

prices = [
    0,
    100,
    10000,
    1000000,
    100000000,
    10,
    10000,
    10000000,
    10000000000
]

buttons = []

for i in range(len(buttonPositions)):
    buttons.append(Button(i, 
    buttonPositions[i], 
    buttonSizes[i], 
    images[i][0], 
    images[i][1], 
    prices[i], 
    names
))

buttons[0].type = "clicker"

for i in range(4):
    buttons[i + 1].type = "upgrade"

for i in range(4):
    buttons[i + 5].type = "idle"


def drawButtons():
    for i in range(len(buttons)):
        buttons[i].draw()