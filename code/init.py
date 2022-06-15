import pygame as pg

pg.init()

WHITE = 255, 255, 255

BLACK = 0, 0, 0

size = 1366, 768

fontSize = size[0] // 50

gap = size[1] // 23

buttonHeight = size[1] // 5.12

buttonWidth = size[0] // 2.73

clock = pg.time.Clock()

screen = pg.display.set_mode(size)

font = pg.font.SysFont(None, fontSize)