import pygame as pg
import sys

from style import *
from logic import *

class Game():
    def start(self):
        pressEvent = False
        while True:
            screen.fill((BLACK))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    pressEvent = True

            if pressEvent:
                whenPress()
                pressEvent = False

            drawButtons()
            drawInfo()
            playerBank.drawBalance()
            playerBank.tick(calcIncr())

            clock.tick(60)

            pg.display.flip()
            
game = Game()

if __name__ == "__main__":
    game.start()