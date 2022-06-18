import pygame as pg
from init import *

clock = pg.time.Clock()

class Account():
    def __init__(self):
        self.balance = 0
    
    def enoughMoney(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False
    
    def withdraw(self, amount):
        self.balance -= amount

    def tick(self, increase):
        self.balance += increase

    def drawBalance(self):
        self.text = font.render(f"{self.balance:,}", True, WHITE)
        screen.blit(self.text, (size[0] / 2, size[1] / 100))
        

class Button():
    def __init__(self, id, topLeft, size, img, darkimg, price, names):
        self.amount = 0
        self.type = "undef"
        self.clickerAmount = 1
        
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
        elif self.type != "upgrade":
            if self.frames < 2:
                screen.blit(self.darkImage, self.topLeft)
                self.frames += 1
            else:
                self.frames = 0
                self.isPressed = False

        elif self.type == "upgrade" and self.amount != 1:
            if self.frames < 2:
                screen.blit(self.darkImage, self.topLeft)
                self.frames += 1
            else:
                self.frames = 0
                self.isPressed = False
        else:
            screen.blit(self.darkImage, self.topLeft)
            
        
        
        screen.blit(self.text, (self.left + (self.width - self.text_width) / 2, self.top + (self.height - self.text_height) / 2))
        
        if self.type != "clicker":
            try:
                self.priceText = font.render(f"Price: {self.price:,}", True, BLACK)
                screen.blit(self.priceText, (self.left, self.top))
            except ValueError:
                self.priceText = font.render(f"Bought", True, BLACK)
                screen.blit(self.priceText, (self.left, self.top))

    def press(self):
        self.isPressed = True
    
    def release(self):
        self.isPressed = False
    
    def increasePrice(self):
        self.price *= 2