import pygame as pg

pg.init()

WHITE = 255, 255, 255

BLACK = 0, 0, 0

size = 1366, 768

fontSize = 24

pressEvent = False

clock = pg.time.Clock()

screen = pg.display.set_mode(size)

font = pg.font.SysFont(None, fontSize)