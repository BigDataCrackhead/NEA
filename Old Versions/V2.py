import pygame, pickle, sys, time, random, math
from _thread import *

stop_threads=True
pygame.display.init()
pygame.font.init()

redAmber=pygame.image.load("TL A R.png")
red=pygame.image.load("TL R.png")
amber=pygame.image.load("TL A.png")
green=pygame.image.load("TL G.png")

WIDTH=1200
HEIGHT=800
BACKGROUND=pygame.Color("#EAEAEA")
BLUE=pygame.Color("#00A896")
ORANGE=pygame.Color("#89043D")
LB=pygame.Color("#2FE6DE")

win = pygame.display.set_mode((WIDTH, HEIGHT))

store = {TL:redAmber, Road:roadyBoi}

class Object(object):
    def __init__(self, x, y, width, height, typ):
        self.typ=typ
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def move(self, x, y, win):
        self.x=x
        self.y=y

    def draw(self, win):
        win.blit(redAmber, (self.x+1, self.y))
        pygame.draw.rect(win, self.typ, (self.x, self.y, self.width, self.height), 2)

class TrafficLight(Object):
    def __init__(self, x, y, timeOn, timeOff, points):
        width=20
        height=20
        Object.__init__(self, x, y, width, height, "TL")
        self.x=x
        self.y=y
        self.timeOn=timeOn
        self.timeOff=timeOff
        self.points=points

    
def drawText(win, text, x, y, size, colour):
    try:
        font = pygame.font.SysFont("Comic Sans", size)
        toBlit = font.render(text, 1, colour, False)
        win.blit(toBlit, ( int( x-(toBlit.get_width()/2) ) , int( y-(toBlit.get_height()/2)) ))
    except:
        print('Font Error, Saw It Coming Ngl')

def normalMenu(win):
    pygame.draw.rect(win,BLUE, (0, 600, 100, 100), 2)
    drawText(win, "Lights", 50, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 600, 100, 100), 2)
    drawText(win, "Roads", 150, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 700, 100, 100), 2)
    drawText(win, "Junctions", 50, 720, 30, BLUE)
    pygame.draw.rect(win,BLUE, (0, 700, 100, 100), 2)
    drawText(win, "Other", 150, 720, 30, BLUE)
    
def drawAll(win, listy):
    win.fill(BACKGROUND)
    drawText(win, "Return To Menu", 60, 20, 20, BLUE)
    pygame.draw.rect(win,BLUE, (0, 10, 120, 20), 2)
    normalMenu(win)
    
    for i in listy:
        i.draw(win)

    pygame.display.flip()
        
def main(win):
    print("Design Phase Started")
    pygame.display.set_caption('Design Phase')

    itemList=[]
    light=TrafficLight(40, 645, None, None, 0)
    itemList.append(light)

    while True:
        drawAll(win, itemList)
        
    mainMenu(win)




def threaded_title(win, WIDTH, HEIGHT):
    global stop_threads
    while stop_threads:
        if stop_threads:
            win.fill(BACKGROUND)            
            drawText(win, "Traffic Light Optimiser", int(WIDTH/2), int(-200+HEIGHT/2), 60, BLUE)
            drawText(win, "Click To Start", int(WIDTH/2), int(-100+HEIGHT/2), 50, BLUE)
            pygame.display.flip() 
        else:
            break
        time.sleep(0.5)
        if stop_threads:
            win.fill(BACKGROUND)            
            drawText(win, "Traffic Light Optimiser", int(WIDTH/2), int(-200+HEIGHT/2), 60, BLUE)            
            pygame.display.flip()
        else:
            break
        time.sleep(0.5)
    print("Thread Ended")
    return
def mainMenu(win):
    global stop_threads  
    print("Running Main Menu")
    pygame.display.set_caption("Reinforcement Learning Traffic Lights")   
    stop_threads=True  
    run = True  
    clock = pygame.time.Clock()  
    start_new_thread(threaded_title, (win, WIDTH, HEIGHT))
    print("Thread Started")   
    while run:
        clock.tick(30)     
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#Quit
                stop_threads=False
                print("Goodbye!")
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                run = False
                stop_threads=False
    main(win)
while True:
    try:
        mainMenu(win)
    except:
        sys.exit()
