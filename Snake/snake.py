import math
import random
import pygame
import tkinter as tkinter
from tkinter import messagebox

class Cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirx=1, diry=0, color=(255,0,0)):
        pass
    
    def move(self, dirx, diry):
        pass
    
    def draw(self, surface, eyes=False):
        pass

class Snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x,y=0,0

    for i in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))

def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnake(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global rows, width
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = Snake((255,0,0),(10,10))
    flag = True
    clock = pygame.time.Clock()
    while(flag):
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(win)

# rows = 
# w = 
# h = 

# Cube.rows = rows
# Cube.w = w

main()