from objects import Button
from style import *

buttonSizes = [
    [100, 200],
    [100, 50], 
    [100, 50],
    [100, 50],
]

buttonPositions = [
    [(size[0] - buttonSizes[0][0]) / 2 , (size[1] - buttonSizes[0][1]) / 2],
    [100, 10], 
    [100, 110],
    [100, 210],
]

names = [
    "click",
    "0,33L sola",
    "0,5L sola",
    "1,5L sola",
]

buttons = []

for i in range(len(buttonPositions)):
    buttons.append(Button(i, buttonPositions[i], buttonSizes[i], images[i][0], images[i][1], names))




def drawButtons():
    for i in range(len(buttons)):
        buttons[i].draw()