import pygame, pickle, sys, time, random, math
from _thread import *





#GLOBAL VARIABLES
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





#CLASSES
class Object(object):
    def __init__(self, typ, x, y, width, height):
        self.typ=typ
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        
    def move(self, x, y, win):
        self.x=x#-int(self.width/2)
        self.y=y#-int(self.height/2)
        
    def getXY(self):
        listy=(self.x, self.y, self.width, self.height)
        return listy

    def draw(self, win):
        win.blit(redAmber, (self.x+1, self.y))
        pygame.draw.rect(win, self.typ, (self.x, self.y, self.width, self.height), 2)
    
'''class TrafficLight(Object):
    def __init__(self, x, y, typ, timeOn, timeOff, points):
        width=20
        height=20
        Object.init(self, typ, x, y, width, height)
        self.x=x
        self.y=y
        self.typ=typ
        self.timeOn=timeOn
        self.timeOff=timeOff
        self.points=points
    def draw(self):
        pass

class Car:
    def __init__(self, x, y, color, vel, acc, direc, cap=30):
        self.x=x
        self.y=y
        self.color=color
        self.vel=vel
        self.acc=acc
        self.direc=direc
        self.cap=cap
    def canAcc(self):
        if self.vel<self.cap:
            return True
        return False

class Road:
    def __init__(self, startX, startY, endX, endY):
        self.startX=startX
        self.startY=startY
        self.endX=endX
        self.endY=endY'''






#DRAWING BUTTONS
def returnMenuBtn(win):
    drawText(win, "Return To Menu", 60, 20, 20, BLUE)
    pygame.draw.rect(win,BLUE, (0, 10, 120, 20), 2)

def normalMenu(win):
    pygame.draw.rect(win,BLUE, (0, 600, 100, 100), 2)
    drawText(win, "Lights", 50, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 600, 100, 100), 2)
    drawText(win, "Roads", 150, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 700, 100, 100), 2)
    drawText(win, "Junctions", 50, 720, 30, BLUE)
    pygame.draw.rect(win,BLUE, (0, 700, 100, 100), 2)
    drawText(win, "Other", 150, 720, 30, BLUE)
    
    pygame.display.flip()

def menuOne(win):
    pygame.draw.rect(win,BLUE, (0, 600, 100, 100), 2)
    drawText(win, "New Junction", 50, 620, 21, BLUE)
    pygame.draw.rect(win,BLUE, (100, 600, 100, 100), 2)
    drawText(win, "4-Way", 150, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 700, 100, 100), 2)
    drawText(win, "Lane Split", 50, 720, 26, BLUE)
    pygame.draw.rect(win,BLUE, (0, 700, 100, 100), 2)
    drawText(win, "Back", 150, 720, 30, BLUE)
    pygame.display.flip()

def menuTwo(win):
    pygame.draw.rect(win,BLUE, (0, 600, 100, 100), 2)
    drawText(win, "Edit", 50, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 600, 100, 100), 2)
    drawText(win, "Time", 150, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 700, 100, 100), 2)
    drawText(win, "Roundabouts", 50, 720, 20, BLUE)
    pygame.draw.rect(win,BLUE, (0, 700, 100, 100), 2)
    drawText(win, "Back", 150, 720, 30, BLUE)
    pygame.display.flip()
            
        
    


#BOTTOM LEFT MENU OPTIONS
def newLights(win, listy):
    print("New Lights Added")
    return listy

def openJunctions(win):
    print("Junction Menu Opened")

def newRoad(win, listy):
    print("New Road Added")
    return listy

def other(win):
    print("Other Menu Opened")





#SAVE AND IMPORT    
def drawSaveImprt(win):
    pygame.draw.rect(win, BACKGROUND, (1000, 0, 200, 30))
    
    pygame.draw.rect(win,BLUE, (1000, 0, 100, 30), 2)
    drawText(win, "Save", 1050, 15, 30, BLUE)
    pygame.draw.rect(win,BLUE, (1100, 0, 100, 30), 2)
    drawText(win, "Import", 1150, 15, 30, BLUE)
    
def save(win):
    pygame.draw.rect(win, BACKGROUND, (1000, 0, 200, 30))
    pygame.draw.rect(win,BLUE, (1000, 0, 100, 30), 2)
    drawText(win, "File 1", 1050, 15, 30, BLUE)
    pygame.draw.rect(win,BLUE, (1100, 0, 100, 30), 2)
    drawText(win, "File 2", 1150, 15, 30, BLUE)
    
    print("Save Called")

def saveBoard(win, data, mem):
    if mem:
        print("Board Saved Into File 1")
    else:
        print("Board Saved Into File 2")

    drawSaveImprt(win)

def imprt(win):
    pygame.draw.rect(win, BACKGROUND, (1000, 0, 200, 30))
    pygame.draw.rect(win,BLUE, (1000, 0, 100, 30), 2)
    drawText(win, "File 1", 1050, 15, 30, BLUE)
    pygame.draw.rect(win,BLUE, (1100, 0, 100, 30), 2)
    drawText(win, "File 2", 1150, 15, 30, BLUE)
    
    pygame.display.flip()
    print("Import Called")

def imprtBoard(win, mem):
    if mem:
        print("Import Board From File 1")
    else:
        print("Import Board From File 2")

    drawSaveImprt(win)
    pygame.display.flip()





#JUNCTION MENU
def newJunction(win):
    print("New Junction Called")

def fourJunct(win):
    print("4-Way Junction Called")

def laneSplit(win):
    print("Lane-Split Called")





#OTHER MENU
def edit(win):
    print("Edit Called")

def timeChange(win):
    print("Time Menu Called")

def roundabout(win):
    print("Roundabouts Called")



#DRAWTEXT PROCEDURE
def drawText(win, text, x, y, size, colour):
    try:
        font = pygame.font.SysFont("Comic Sans", size)
        toBlit = font.render(text, 1, colour, False)
        win.blit(toBlit, ( int( x-(toBlit.get_width()/2) ) , int( y-(toBlit.get_height()/2)) ))
    except:
        print('Font Error, Saw It Coming Ngl')





#LAUNCH MRS AND GUI
def MRS(win):
    print("MRS Running")
    win.fill(BACKGROUND)

    drawText(win, "Design Saved To File 1", 600, 300, 60, BLUE)
    pygame.display.flip()
    t=0
    
    while True:
        t+=1
        if t<=4:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Quit
                    stop_threads=False
                    print("Goodbye!")
                    pygame.quit()
                    sys.exit()
                    
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    print(pos)
                    if pos[0]>0 and pos[0]<160:#Return To Menu
                        if pos[1]>10 and pos[1]<30:
                            print("Returning To Main Menu")
                            mainMenu(win)
                            break
        else:
            break
        time.sleep(0.5)
        
    win.fill(BACKGROUND)
    
    returnMenuBtn(win)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#Quit
                stop_threads=False
                print("Goodbye!")
                pygame.quit()
                sys.exit()
                
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                print(pos)
                if pos[0]>0 and pos[0]<160:#Return To Menu
                    if pos[1]>10 and pos[1]<30:
                        print("Returning To Main Menu")
                        mainMenu(win)
                        break
                
def GUI(win):
    print("GUI Running")
    win.fill(BACKGROUND)

    drawText(win, "Design Saved To File 1", 600, 300, 60, BLUE)
    pygame.display.flip()
    t=0
    
    while True:
        t+=1
        if t<=4:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Quit
                    stop_threads=False
                    print("Goodbye!")
                    pygame.quit()
                    sys.exit()
                    
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    print(pos)
                    if pos[0]>0 and pos[0]<160:#Return To Menu
                        if pos[1]>10 and pos[1]<30:
                            print("Returning To Main Menu")
                            mainMenu(win)
                            break
        else:
            break
        time.sleep(0.5)
        
    win.fill(BACKGROUND)
    
    returnMenuBtn(win)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#Quit
                stop_threads=False
                print("Goodbye!")
                pygame.quit()
                sys.exit()
                
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                print(pos)
                if pos[0]>0 and pos[0]<160:#Return To Menu
                    if pos[1]>10 and pos[1]<30:
                        print("Returning To Main Menu")
                        mainMenu(win)
                        break





#MAIN
def main(win):
    print("Design Phase Started")
    win.fill(BACKGROUND)
    pygame.display.set_caption('Design Phase')

    itemList=[]

    saveFlip=False
    imprtFlip=False
    
    menuMode=0

    light=Object(ORANGE, 40, 645, 20, 20)
    itemList.append(light)
    
    while True:
        win.fill(BACKGROUND)
        
        returnMenuBtn(win)
        drawSaveImprt(win)

        for i in itemList:
            i.draw(win)
            
        drawText(win, "Run GUI", 1120, 700, 40, BLUE)
        pygame.draw.rect(win,BLUE, (1050, 680, 140, 35), 2)
        
        drawText(win, "Run MRS", 1120, 760, 40, BLUE)
        pygame.draw.rect(win,BLUE, (1050, 740, 140, 35), 2)
        
        if menuMode==0:
            normalMenu(win)
        
        elif menuMode==1:
            menuOne(win)
            
        elif menuMode==2:
            menuTwo(win)
            
        pos=pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
                temp=0
                try:
                    pos0=event.pos[0]
                    pos1=event.pos[1]
                    for i in itemList:
                        p=i.getXY()
                        if pos0>p[0] and pos0<(p[0]+p[2]) and temp==0:
                            if pos1>p[1] and pos1<(p[1]+p[3]):
                                temp+=1
                                i.move(pos0, pos1, win)
                except:
                    print("Event.pos Error, Saw It Coming Ngl")
                            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#Quit
                stop_threads=False
                print("Goodbye!")
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[0]<120:#Return To Menu
                    if pos[1]>10 and pos[1]<30:
                        print(itemList)
                        print("Returning To Main Menu")
                        mainMenu(win)
                        break
                 
                elif pos[1]>0 and pos[1]<30:#Save/Import
                    if saveFlip:
                        if pos[0]>1000 and pos[0]<1100:
                            typ=True#True is One
                            saveFlip=False
                        elif pos[0]>1100 and pos[0]<1200:
                            typ=False#False is Two
                            saveFlip=False
                            
                        saveBoard(win, itemList, typ)
                        
                    elif imprtFlip:
                        if pos[0]>1000 and pos[0]<1100:
                            typ=True#True is One
                            imprtFlip=False
                        elif pos[0]>1100 and pos[0]<1200:
                            typ=False#False is Two
                            imprtFlip=False
                            
                        imprtBoard(win, typ)
                        
                    else:
                        if pos[0]>1000 and pos[0]<1100:
                            save(win)
                            saveFlip=True
                        elif pos[0]>1100 and pos[0]<1200:
                            imprt(win)
                            imprtFlip=True
                
                elif pos[0]>1050 and pos[0]<1190:#Run GUI or MRS
                    
                    if pos[1]>740 and pos[1]<770:
                        MRS(win)
                        break
                    elif pos[1]>680 and pos[1]<710:
                        GUI(win)
                        break
                
                '''for x in range(length):
                    if pos[0]>itemList[x][1] and pos[0]<(itemList[x][1]+itemList[x][3]):
                        if pos[1]>itemList[x][2] and pos[1]<(itemList[x][2]+itemList[x][4]):
                            xTemp=itemList[x][1]
                            yTemp=itemList[x][2]
                            print(xTemp, yTemp)
                            #xTemp-change in pos[0]
                            down=pygame.mouse.get_pressed()
                            while down[0]:
                                print("!")
                                #call move function to the mouses position minus the width and height
                                pass'''
                if menuMode==0: 
                    if pos[0]>0 and pos[0]<100:
                        if pos[1]>600 and pos[1]<700:
                            itemList=newLights(win, itemList)#Top Left
                        elif pos[1]>700 and pos[1]<800:
                            openJunctions(win)#Bottom Left
                            menuMode=1
                            
                    elif pos[0]>100 and pos[0]<200:
                        if pos[1]>600 and pos[1]<700:
                            itemList=newRoad(win, itemList)#Top Right
                        elif pos[1]>700 and pos[1]<800:
                            other(win)#Bottom Right
                            menuMode=2
                            
                elif menuMode==1: 
                    if pos[0]>0 and pos[0]<100:
                        if pos[1]>600 and pos[1]<700:
                            newJunction(win)#Top Left
                        elif pos[1]>700 and pos[1]<800:
                            laneSplit(win)#Bottom Left
                            
                    elif pos[0]>100 and pos[0]<200:
                        if pos[1]>600 and pos[1]<700:
                            fourJunct(win)#Top Right
                        elif pos[1]>700 and pos[1]<800:
                            normalMenu(win)#Bottom Right
                            menuMode=0
                            
                elif menuMode==2: 
                    if pos[0]>0 and pos[0]<100:
                        if pos[1]>600 and pos[1]<700:
                            edit(win)#Top Left
                        elif pos[1]>700 and pos[1]<800:
                            roundabout(win)#Bottom Left
                            
                    elif pos[0]>100 and pos[0]<200:
                        if pos[1]>600 and pos[1]<700:
                            timeChange(win)#Top Right
                        elif pos[1]>700 and pos[1]<800:
                            normalMenu(win)#Bottom Right
                            menuMode=0
           
    mainMenu(win)





#FLASHING TITLE 
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





#MAIN MENU
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





#START
while True:
    try:
        mainMenu(win)
    except:
        sys.exit()
