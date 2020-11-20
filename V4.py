import pygame, pickle, sys, random, math, logging, time
from _thread import *
import listenToHarry as classy
import Draw as d
import Click as c
import Sims as s
import Pack as p
import Edits as e
import Variables as v

#math.modf(x)
#Return the fractional and integer parts of x. Both results carry the sign of x and are floats.
#average car length roughly = 4.6m
stop_threads=True#The global variable that tells the threads to stop
pygame.display.init()
pygame.font.init()

WIDTH=1200
HEIGHT=800

pygameWindowInstance = pygame.display.set_mode((WIDTH, HEIGHT))

clockInstance=pygame.time.Clock()

def main(w, clock):
    pygame.display.set_caption('Design Phase')

    itemList=[]
    groupList=[]
    menu=0
    saveImport=0
    lastMove=False
    lastClick=False
    l=None
    time=None

    while True:
        clickCheck=False
        moveCheck=False

        clock.tick(60)

        x, y = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            clickCheck=True
            if lastMove:
                l.move(x, y, w)
                moveCheck=True
            else:
                if x>1050 and x<1190:#Run GUI or MRS
                    if y>740 and y<770:
                        s.MRS()
                        break
                    elif y>680 and y<710:
                        s.GUI()
                        break

                if not lastClick:
                    if c.checkWithin(x, y, 0, 10, 160, 20):
                        print("Returning To Main Menu")
                        itemList[0].resetCounter()
                        break

                    l=c.checkMove(w, x, y, itemList)
                if l:
                    if l.typ==("TM"):
                        pass
                    else:
                        moveCheck=True

                if not moveCheck and not lastClick:
                    quart=0
                    if c.checkWithin(x, y, 1000, 0, 100, 30):
                        if saveImport==0:
                            saveImport=1
                        elif saveImport==1:
                            p.pack(itemList, 1, time, groupList)
                            saveImport=0
                        elif saveImport==2:
                            itemList, time, groupList=p.unpack(1)
                            saveImport=0

                    if c.checkWithin(x, y, 1100, 0, 100, 30):
                        if saveImport==0:
                            saveImport=2
                        elif saveImport==1:
                            p.pack(itemList, 2, time, groupList)
                            saveImport=0
                        elif saveImport==2:
                            itemList, time, groupList=p.unpack(2)
                            saveImport=0

                    elif c.checkWithin(x, y, 0, 700, 100, 100):
                        quart=1
                    elif c.checkWithin(x, y, 100, 700, 100, 100):
                        quart=2
                    if menu==0:
                        if quart==1:
                            length=len(itemList)
                            for x in range(length, 0, -1):
                                o=itemList[x-1]
                                if o.checkInside(0, 600, 200, 800):
                                    itemList.remove(o)
                                    classy.Object.counterStorage.append(o.id)
                            menu=1  
                        elif quart==2:
                            length=len(itemList)
                            for x in range (length, 0, -1):
                                o=itemList[x-1]
                                if o.checkInside(0, 600, 200, 800):
                                    itemList.remove(o)
                                    classy.Object.counterStorage.append(o.id)
                            menu=2

                    elif menu==1 or menu==2:
                        if quart==2:
                            length=len(itemList)
                            for x in range (length, 0, -1):
                                o=itemList[x-1]
                                if o.checkInside(0, 600, 200, 800):
                                    itemList.remove(o)
                                    classy.Object.counterStorage.append(o.id)
                            menu=0
                    if menu==2:
                        if c.checkWithin(x, y, 100, 600, 100, 100):
                               time=e.time(w, time)

        if lastMove and not clickCheck:
            if l.checkInside(200, 740, 240, 800):
                    itemList.remove(l)
                    classy.Object.counterStorage.append(l.id)
            """ elif onTop(l, itemList):
                itemList.remove(l) """
            
            e.snap(w, itemList, l)

            tempX=l.x+(l.width/2)
            tempY=l.y+(l.height/2)
            if l.typ=="ET":
                for i in itemList:
                    if i.checkWithin(tempX, tempY):
                        itemList.remove(l)
                        classy.Object.counterStorage.append(l.id)
                        if i!=l:
                            if i.typ=="TL":
                                groupList.append(e.edit(w, i, itemList))
                            else:
                                i=e.edit(w, i, itemList)

                            clickCheck=True
                        break
                    
            elif l.typ=="RO":
                for i in itemList:
                    if i.checkWithin(tempX, tempY):
                        itemList.remove(l)
                        classy.Object.counterStorage.append(l.id)
                        c.rotate(i, itemList)
                        i.defineGeometry()
                        clickCheck=True
                        break

        d.drawAll(w, x, y, itemList, menu, saveImport)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print("Goodbye!")
                pygame.quit()
                sys.exit()
        
        lastClick=clickCheck
        lastMove=moveCheck

def threaded_title(win, WIDTH, HEIGHT):
    global stop_threads
    while stop_threads:
        if stop_threads:
            win.fill(v.BACKGROUND)            
            d.drawText(win, "Traffic Light Optimiser", int(WIDTH/2), int(-200+HEIGHT/2), 60, v.BLUE)
            d.drawText(win, "Click To Start", int(WIDTH/2), int(-100+HEIGHT/2), 50, v.BLUE)
            pygame.display.flip() 
        else:
            break
        time.sleep(0.5)
        if stop_threads:
            win.fill(v.BACKGROUND)            
            d.drawText(win, "Traffic Light Optimiser", int(WIDTH/2), int(-200+HEIGHT/2), 60, v.BLUE)            
            pygame.display.flip()
        else:
            break
        time.sleep(0.5)
    print("Thread Ended")
    return

def mainMenu(win, w, h, clock):
    global stop_threads  
    print("Running Main Menu")
    pygame.display.set_caption("Reinforcement Learning Traffic Lights")   
    stop_threads=True  
    run = True    
    start_new_thread(threaded_title, (win, w, h))
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
                print("Ending Start Menu")
                run = False
                stop_threads=False
    main(win, clock)    

while True:
    mainMenu(pygameWindowInstance, WIDTH, HEIGHT, clockInstance)