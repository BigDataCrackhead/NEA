import pygame, pickle, sys, time, random, math
from _thread import *

class Object(object):
    def __init__(self, typ, x, y, width, height):
        self.typ=typ
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        
    def move(self, x, y, win):
        self.x=x-int(self.width/2)
        self.y=y-int(self.height/2)
        
        
    def getXY(self):
        listy=(self.x, self.y, self.width, self.height)
        return listy

    def draw(self, win):
        pygame.draw.rect(win, BLUE, (self.x, self.y, self.width, self.height), 2)

pygame.display.init()
pygame.font.init()

WIDTH=1200
HEIGHT=800
BACKGROUND=(80, 80, 86)
BLUE=(0,139,139)

win = pygame.display.set_mode((WIDTH, HEIGHT))

win.fill(BACKGROUND)
pygame.display.flip()

light=Object("l", 20, 20, 100, 100)

objectList=[]
objectList.append(light)
    
while True:
    win.fill(BACKGROUND)
    for i in objectList:
        i.draw(win)
        
    for event in pygame.event.get():
            if event.type==pygame.QUIT:#Quit
                print("Goodbye!")
                pygame.quit()
                sys.exit()
                
            if pygame.mouse.get_pressed()[0]:
                x=0
                try:
                    pos0=event.pos[0]
                    pos1=event.pos[1]
                except:
                    pass
                for i in objectList:
                    l=i.getXY()
                    if pos0>l[0] and pos0<(l[0]+l[2]) and x==0:
                        if pos1>l[1] and pos1<(l[1]+l[3]):
                            x+=1
                            i.move(pos0, pos1, win)
                                            
                if x==0:
                    print(objectList)
                    light=Object("l", pos0, pos1, 100, 100)
                    objectList.append(light)
                    x+=1
                    
    pygame.display.flip()
    
