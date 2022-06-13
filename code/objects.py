import pygame as pg
from init import *

clock = pg.time.Clock()

class Account():
    def __init__(self):
        self.balance = 0
    
    def enoughMoney(self, amount, items):
        if self.balance >= amount:
            print(f"You do have {amount} sola")
            print(f"You now have {items} of this")
            return True
        else:
            print(f"You don't have {amount} sola")
            print(f"You now have {items} of this")
            return False
    
    def withdraw(self, amount):
        self.balance -= amount

    def tick(self):
        increase = 10
        self.balance += increase

    def drawBalance(self):
        self.text = font.render(str(self.balance), True, WHITE)
        screen.blit(self.text, (size[0] / 2, size[1] / 100))
        

class Button():
    def __init__(self, id, topLeft, size, img, darkimg, price, names):
        self.amount = 0

        self.id = id
        self.left, self.top = topLeft
        self.topLeft = topLeft
        self.width, self.height = size
        self.price = price
        
        self.image = pg.transform.scale(pg.image.load(img), (self.width, self.height))
        self.darkImage = pg.transform.scale(pg.image.load(darkimg), (self.width, self.height))
        self.isPressed = False
        self.frames = 0
        
        self.name = names[self.id]
        self.text = font.render(self.name, True, BLACK)
        self.text_width, self.text_height = font.size(self.name)


    def draw(self):
        if not self.isPressed:
            screen.blit(self.image, self.topLeft)
        else:
            if self.frames < 5:
                screen.blit(self.darkImage, self.topLeft)
                self.frames += 1
            else:
                self.frames = 0
                self.isPressed = False
        screen.blit(self.text, (self.left + (self.width - self.text_width) / 2, self.top + (self.height - self.text_height) / 2))
        
    def press(self):
        self.isPressed = True
    
    def release(self):
        self.isPressed = False
    
    def increasePrice(self):
        self.price *= 10