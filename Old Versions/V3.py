import pygame, pickle, sys, time, random, math, logging
from _thread import *

stop_threads=True#The global variable that tells the threads to stop
pygame.display.init()
pygame.font.init()

redAmber=pygame.image.load("./Assets/TL A R.png")
red=pygame.image.load("./Assets/TL R.png")
amber=pygame.image.load("./Assets/TL A.png")
green=pygame.image.load("./Assets/TL G.png")
road=pygame.image.load("./Assets/road.png")
binny=pygame.image.load("./Assets/bin.png")
tJunct=pygame.image.load("./Assets/Junction T.png")
fourJunct=pygame.image.load("./Assets/Junction +.png")
splitJunct=pygame.image.load("./Assets/Junction Split.png")
rotateImg=pygame.image.load("./Assets/Rotate.png")
edit=pygame.image.load("./Assets/Edit Tool.png")
timey=pygame.image.load("./Assets/Time.png")


WIDTH=1200
HEIGHT=800
BACKGROUND=pygame.Color("#EAEAEA")
BLUE=pygame.Color("#00A896")     
OFFBLUE=pygame.Color("#88CCCC")
ORANGE=pygame.Color("#89043D")
LB=pygame.Color("#2FE6DE")
BLACK=pygame.Color("#000000")

win = pygame.display.set_mode((WIDTH, HEIGHT))

class Object(object):
    def __init__(self, x, y, width, height, typ):
        self.typ=typ
        self.x=x
        self.y=y
        self.width=int(width)
        self.height=int(height)
        self.conn=[]
        self.rotation=360
        if self.typ==redAmber:
            self.i="TL"
        elif self.typ==road:
            self.i="RD"
        elif self.typ==tJunct:
            self.i="TJ"
        elif self.typ==fourJunct:
            self.i="4J"
        elif self.typ==splitJunct:
            self.i="SJ"
        elif self.typ==timey:
            self.i="TM"
        elif self.typ==rotateImg:
            self.i="RO"
        elif self.typ==edit:
            self.i="ET"

    def move(self, xMid, yMid, win):
        self.x=xMid-(self.width/2)
        self.y=yMid-(self.height/2)
        self.conn=[]

    def checkWithin(self, x, y):
        if self.x<x and (self.x+self.width)>x:
            if self.y<y and (self.y+self.height)>y:
                return True
        return False

    def checkInside(self, x1, y1, x2, y2):
        tempX=self.x+(self.width/2)
        tempY=self.y+(self.height/2)
        if tempX>x1 and tempX<x2:
            if tempY>y1 and tempY<y2:
                return True
        return False
    
    def getXY(self):
        listy=(self.x, self.y, self.width, self.height, self.typ)
        return listy

    def draw(self, win):
        win.blit(self.typ, (int(self.x), int(self.y)))

    def addConnection(self, conn):
        self.conn.append(conn)
    
    def popConnections(self):
        temp=self.conn
        self.conn=[]
        return temp

    def pygameSux(self):
        listy=(self.x, self.y, self.i, self.conn, self.rotation)
        return listy
        
class TrafficLight(Object):
    def __init__(self, x, y, timeOn, timeOff, connections):
        Object.__init__(self, x, y, "20", "20", redAmber)
        self.x=x
        self.y=y
        self.timeOn=timeOn
        self.timeOff=timeOff
        self.connections=connections

    def setTimes(self, timeOne, timeTwo):
        self.timeOn=timeOne
        self.timeOff=timeTwo

class Road(Object):#REMINDER TO ADD ORIENTATION TO STUFF
    def __init__(self, x, y, length, con1, con2):
        Object.__init__(self, x, y, "60", "20", road)
        self.x=x
        self.y=y
        self.length=length
        self.con1=con1
        self.con2=con2

class FourJunction(Object):
    def __init__(self, x, y, conn1, conn2, conn3, conn4):
        Object.__init__(self, x, y, "60", "60", fourJunct)
        self.x=x
        self.y=y
        self.conn1=conn1
        self.conn2=conn2
        self.conn3=conn3
        self.conn4=conn4

class TJunction(Object):
    def __init__(self, x, y, conn1, conn2, conn3):
        Object.__init__(self, x, y, "60", "60", tJunct)
        self.x=x
        self.y=y
        self.conn1=conn1
        self.conn2=conn2
        self.conn3=conn3

class Split(Object):
    def __init__(self, x, y, rd1, split1, split2):
        Object.__init__(self, x, y, "60", "60", splitJunct)
        self.x=x
        self.y=y
        self.rd1=rd1
        self.split1=split1
        self.split2=split2

class Edit(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, "20", "20", edit)
        self.x=x
        self.y=y

class Time(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, "20", "20", timey)
        self.x=x
        self.y=y

    def move(self, x, y, win):
        pass

class Rotate(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, "20", "20", rotateImg)
        self.x=x
        self.y=y

def assemble(bigList):
    print(bigList)
    

def timeMenu():
    print("TimeMenu")

def saveBoard(win, l, num):
    listy=[]
    length=len(l)
    for x in range (length, 0, -1):
        o=l[x-1]
        if o.checkInside(0, 600, 200, 800):
            l.remove(o)
    for i in l:
        temp=i.pygameSux()
        listy.append(temp)
    if num==0:
        with open('saveOne.pickle', 'wb') as handle:
            pickle.dump(listy, handle, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        with open('saveTwo.pickle', 'wb') as handle:
            pickle.dump(listy, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
def loadBoard(win, num):
    if num==0:
        with open('saveOne.pickle', 'rb') as handle:
            temp = pickle.load(handle)
    else:
        with open('saveTwo.pickle', 'rb') as handle:
            temp = pickle.load(handle)
    print(temp)
    listy=[]
    listy=assemble(temp)
    return listy

def MRS(win):
    print("MRS Running")
    win.fill(BACKGROUND)

    drawText(win, "Design Saved To File 1", 600, 300, 60, BLUE)
    pygame.display.flip()

    for x in range(4):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#Quit
                stop_threads=False
                print("Goodbye!")
                pygame.quit()
                sys.exit()

        time.sleep(0.5)
        
    win.fill(BACKGROUND)
    
    drawText(win, "Return To Menu", 60, 20, 20, BLUE)
    pygame.draw.rect(win,BLUE, (0, 10, 120, 20), 2)
    
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

    for x in range(4):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#Quit
                stop_threads=False
                print("Goodbye!")
                pygame.quit()
                sys.exit()
        time.sleep(0.5)
        
    win.fill(BACKGROUND)
    
    drawText(win, "Return To Menu", 60, 20, 20, BLUE)
    pygame.draw.rect(win,BLUE, (0, 10, 120, 20), 2)
    
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
                    
def drawText(win, text, x, y, size, colour):
    try:
        font = pygame.font.SysFont("Comic Sans", size)
        toBlit = font.render(text, 1, colour, False)
        win.blit(toBlit, ( int( x-(toBlit.get_width()/2) ) , int( y-(toBlit.get_height()/2)) ))
    except:
        logging.warning('Font Error, Saw It Coming Ngl')

def normalMenu(win, l):
    pygame.draw.rect(win,BLUE, (0, 600, 100, 100), 2)
    drawText(win, "Lights", 50, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 600, 100, 100), 2)
    drawText(win, "Roads", 150, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 700, 100, 100), 2)
    drawText(win, "Junctions", 50, 720, 30, BLUE)
    pygame.draw.rect(win,BLUE, (0, 700, 100, 100), 2)
    drawText(win, "Other", 150, 720, 30, BLUE)

    firstQuart=0
    secondQuart=0
    
    for i in l:
        c=i.getXY()
        if c[4]==redAmber:
            if c[0]>0 and c[0]<100:
                if c[1]>600 and c[1]<700:
                    firstQuart=1
        elif c[4]==road:
            if c[0]>100 and c[0]<200:
                if c[1]>600 and c[1]<700:
                    secondQuart=1
    if firstQuart==0:
        l.append(TrafficLight(40, 645, None, None, 0))
    elif secondQuart==0:
        l.append(Road(120, 645, None, None, None))

    return l

def junctionMenu(win, l):
    pygame.draw.rect(win,BLUE, (0, 600, 100, 100), 2)
    drawText(win, "New Junction", 50, 620, 21, BLUE)
    pygame.draw.rect(win,BLUE, (100, 600, 100, 100), 2)
    drawText(win, "4-Way", 150, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 700, 100, 100), 2)
    drawText(win, "Lane Split", 50, 720, 26, BLUE)
    pygame.draw.rect(win,BLUE, (0, 700, 100, 100), 2)
    drawText(win, "Back", 150, 720, 30, BLUE)

    firstQuart=0
    secondQuart=0
    thirdQuart=0
    for i in l:
        c=i.getXY()
        if c[4]==tJunct:
            if c[0]>0 and c[0]<100:
                if c[1]>600 and c[1]<700:
                    firstQuart=1
        elif c[4]==fourJunct:
            if c[0]>100 and c[0]<200:
                if c[1]>600 and c[1]<700:
                    secondQuart=1
        elif c[4]==splitJunct:
            if c[0]>0 and c[0]<100:
                if c[1]>700 and c[1]<800:
                    thirdQuart=1
    if firstQuart==0:
        l.append(TJunction(20, 635, None, None, None))

    elif secondQuart==0:
        l.append(FourJunction(120, 635, None, None, None, None))

    elif thirdQuart==0:
        l.append(Split(20, 735, None, None, None))

    return l

def otherMenu(win, l):
    pygame.draw.rect(win,BLUE, (0, 600, 100, 100), 2)
    drawText(win, "Edit", 50, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 600, 100, 100), 2)
    drawText(win, "Time", 150, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 700, 100, 100), 2)
    drawText(win, "Rotate", 50, 720, 20, BLUE)
    pygame.draw.rect(win,BLUE, (0, 700, 100, 100), 2)
    drawText(win, "Back", 150, 720, 30, BLUE)

    firstQuart=0
    secondQuart=0
    thirdQuart=0
    for i in l:
        c=i.getXY()
        if c[4]==edit:
            if c[0]>0 and c[0]<100:
                if c[1]>600 and c[1]<700:
                    firstQuart=1
        elif c[4]==timey:
            if c[0]>100 and c[0]<200:
                if c[1]>600 and c[1]<700:
                    secondQuart=1
        elif c[4]==rotateImg:
            if c[0]>0 and c[0]<100:
                if c[1]>700 and c[1]<800:
                    thirdQuart=1

    if firstQuart==0:
        l.append(Edit(40, 645))

    elif secondQuart==0:
        l.append(Time(140, 645))

    elif thirdQuart==0:
        l.append(Rotate(40, 745))

    return l
    
def drawAll(win, listy, m):
    win.fill(BACKGROUND)
    win.blit(binny, (200, 740))

    if m==0:
        listy=normalMenu(win, listy)

    if m==1:
        listy=junctionMenu(win, listy)

    if m==2:
        listy=otherMenu(win, listy)

    try:
        for i in listy:
            i.draw(win)
    except:
        pass

    return listy

def rotate(win, obj, deg):
    temp=obj.popConnections()
    typ=obj.getXY()
    obj.typ=pygame.transform.rotate(typ[4], deg)
    obj.conn=temp
    obj.width, obj.height=obj.height, obj.width
    obj.rotation+=deg
    if obj.rotation==450:
        obj.rotation=90
       
def main(win):
    print("Design Phase Started")
    pygame.display.set_caption('Design Phase')

    clock=pygame.time.Clock()
    
    itemList=[]
    l=TrafficLight(40, 645, None, None, 0)
    itemList.append(Road(120, 645, None, None, None))
    #itemList.append(Road(120, 645, None, None, None))
    itemList.append(l)

    clock.tick(540)
    menu=0
    last=False
    lastMenu=False
    saveImport=0
    #rotate(win, itemList[0], 90)
    #rotate(win, itemList[1], 90)

    while True:
        press=False
        pressMenu=False
        saveCheck=False

        itemList=drawAll(win, itemList, menu)

        x, y = pygame.mouse.get_pos()
        if x>0 and x<120:
            if y>10 and y<30:
                pygame.draw.rect(win, OFFBLUE, (0, 10, 120, 20))
        if x>1050 and x<1190:
            if y>680 and y<715:
                pygame.draw.rect(win, OFFBLUE, (1050, 680, 140, 35))
            elif y>740 and y<775:
                pygame.draw.rect(win, OFFBLUE, (1050, 740, 140, 35))
        if y>0 and y<30:
            if x>1000 and x<1100:
                pygame.draw.rect(win,OFFBLUE, (1000, 0, 100, 30))
            if x>1100 and x<1200:
                pygame.draw.rect(win,OFFBLUE, (1100, 0, 100, 30))

        drawText(win, "Return To Menu", 60, 20, 20, BLUE)
        pygame.draw.rect(win,BLUE, (0, 10, 120, 20), 2)
        drawText(win, "Run MRS", 1120, 760, 40, BLUE)
        pygame.draw.rect(win,BLUE, (1050, 740, 140, 35), 2)
        drawText(win, "Run GUI", 1120, 700, 40, BLUE)
        pygame.draw.rect(win,BLUE, (1050, 680, 140, 35), 2)

        if saveImport==0:
            pygame.draw.rect(win,BLUE, (1000, 0, 100, 30), 2)
            drawText(win, "Save", 1050, 15, 30, BLUE)
            pygame.draw.rect(win,BLUE, (1100, 0, 100, 30), 2)
            drawText(win, "Import", 1150, 15, 30, BLUE)
        elif saveImport==1:
            pygame.draw.rect(win,BLUE, (1000, 0, 100, 30), 2)
            drawText(win, "File 1", 1050, 15, 30, BLUE)
            pygame.draw.rect(win,BLUE, (1100, 0, 100, 30), 2)
            drawText(win, "File 2", 1150, 15, 30, BLUE)
        elif saveImport==2:
            pygame.draw.rect(win,BLUE, (1000, 0, 100, 30), 2)
            drawText(win, "File 1", 1050, 15, 30, BLUE)
            pygame.draw.rect(win,BLUE, (1100, 0, 100, 30), 2)
            drawText(win, "File 2", 1150, 15, 30, BLUE)

        if pygame.mouse.get_pressed()[0]:
                try:
                    posX, posY=event.pos
                    
                    if last:
                        l.move(posX, posY, win)
                        press=True
                        
                    else:
                        if posX>0 and posX<160:#Return To Menu
                            if posY>10 and posY<30:
                                print("Returning To Main Menu")
                                mainMenu(win)
                                break
                            
                        elif posX>1050 and posX<1190:#Run GUI or MRS
                            if posY>740 and posY<770:
                                MRS(win)
                                break
                            
                            elif posY>680 and posY<710:
                                GUI(win)
                                break
                        
                        if posX>130 and posX<150:
                            if posY>635 and posY<655:
                                for i in itemList:
                                    temp=i.pygameSux()
                                    spareList.append(temp)
                                print(spareList)
                                with open('spareSave.pickle', 'wb') as handle:
                                    pickle.dump(spareList, handle, protocol=pickle.HIGHEST_PROTOCOL)
                                timeMenu()
                        if posY>0 and posY<30:
                            if posX>1000 and posX<1100:
                                if not lastSave:
                                    if saveImport==1:
                                        saveBoard(win, itemList, 0)
                                        saveImport=0
                                    elif saveImport==2:
                                        itemList=loadBoard(win, 0)
                                        saveImport=0
                                    elif saveImport==0:
                                        saveImport=1
                                saveCheck=True

                            elif posX>1100 and posX<1200:
                                if not lastSave:
                                    if saveImport==0:
                                        saveImport=2
                                    elif saveImport==1:
                                        saveBoard(win, itemList, 1)
                                        saveImport=0
                                    elif saveImport==2:
                                        itemList=loadBoard(win, 1)
                                        saveImport=0
                                saveCheck=True

                        for i in itemList:
                            if i.checkWithin(posX, posY):
                                i.move(posX, posY, win)
                                l=i
                                press=True
                                break
                            
                        if not press:
                            if menu==0:
                                if posY>700 and posY<800:
                                    if posX>0 and posX<100:
                                        if not lastMenu:
                                            menu=1
                                            press=True
                                            length=len(itemList)
                                            for x in range (length, 0, -1):
                                                o=itemList[x-1]
                                                if o.checkInside(0, 600, 200, 800):
                                                    itemList.remove(o)
                                            
                                        pressMenu=True
                                        
                                    elif posX>100 and posX<200:
                                        if not lastMenu:
                                            menu=2
                                            length=len(itemList)
                                            for x in range (length, 0, -1):
                                                o=itemList[x-1]
                                                if o.checkInside(0, 600, 200, 800):
                                                    itemList.remove(o)

                                        pressMenu=True
                                        
                            elif menu==1:
                                if posX>100 and posX<200:
                                    if posY>700 and posY<800:
                                        if not lastMenu:
                                            menu=0
                                            length=len(itemList)
                                            for x in range (length, 0, -1):
                                                o=itemList[x-1]
                                                if o.checkInside(0, 600, 200, 800):
                                                    itemList.remove(o)

                                        pressMenu=True
                                        
                            elif menu==2:
                                if posX>100 and posX<200:
                                    if posY>700 and posY<800:
                                        if not lastMenu:
                                            menu=0
                                            length=len(itemList)
                                            for x in range (length, 0, -1):
                                                o=itemList[x-1]
                                                if o.checkInside(0, 600, 200, 800):
                                                    itemList.remove(o)

                                        pressMenu=True
                                    
                except:
                    logging.warning("Event.pos Error, SAW IT COMING NGL")

        if last==True and press==False:
            for i in itemList:
                one=l.getXY()
                two=i.getXY()
                if i.checkInside(200, 740, 240, 800):
                    itemList.remove(i)
                elif two[4]==edit:
                    for x in itemList:
                        if not x==i:
                            if x.checkWithin(two[0]-(two[2]/2), two[1]-(two[3]/2)):
                                print("!")
                    itemList.remove(i)
                elif two[4]==rotateImg:
                    itemList.remove(i)
                elif l!=i:
                    if i.rotation%180==0 and l.rotation%180==0:
                        temp=one[0]+one[2]
                        y1=one[1]+(one[3]/2)
                        y2=two[1]+(two[3]/2)
                        if (temp+10)>two[0] and (temp-10)<two[0]:
                            if (y1+10)>y2 and (y1-10)<y2:
                                l.move(two[0]-(one[2]/2), y2, win)
                                
                        temp=two[0]+two[2]
                        if (temp+10)>one[0] and (temp-10)<one[0]:
                            if (y1+10)>y2 and (y1-10)<y2:
                                l.move(two[0]+two[2]+(one[2]/2), y2, win)

                    if not i.rotation%180==0 and not l.rotation%180==0:
                        temp=one[1]+one[3]
                        x1=one[0]+(one[2]/2)
                        x2=two[0]+(two[2]/2)
                        if (temp+10)>two[1] and (temp-10)<two[1]:
                            if (x1+10)>x2 and (x1-10)<x2:
                                l.move(x2, two[1]-(one[3]/2), win)
                                
                        temp=two[1]+two[3]
                        if (temp+10)>one[1] and (temp-10)<one[1]:
                            if (x1+10)>x2 and (x1-10)<x2:
                                l.move(x2, two[1]+two[3]+(one[3]/2), win)

                    
                        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#Quit
                stop_threads=False
                logging.critical("Goodbye!")
                pygame.quit()
                sys.exit()      
        
        if press:
            last=True
        else:
            last=False
        if pressMenu:
            lastMenu=True
        else:
            lastMenu=False
        if saveCheck:
            lastSave=True
        else:
            lastSave=False
            
        pygame.display.flip()
        
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
                logging.critical("Goodbye!")
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                run = False
                stop_threads=False
    main(win)

while True:
    mainMenu(win)
    
