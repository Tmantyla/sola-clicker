import pygame as pg
import sys

from style import *
from logic import *

while True:
    screen.fill((BLACK))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            index = press()
            name = getButton(index)
            pressEvent = True
            
    if pressEvent:
        whenPress()
        pressEvent = False

    drawButtons()
    drawInfo()
    playerBank.drawBalance()
    playerBank.tick(calcIncr())

    clock.tick(30)

    pg.display.flip()