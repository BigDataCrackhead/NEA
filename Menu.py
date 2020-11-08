import pygame
import Draw as d
import listenToHarry as classy
import Variables as v

BLUE=pygame.Color("#00A896")

def normalMenu(win, l):
    pygame.draw.rect(win,BLUE, (0, 600, 100, 100), 2)
    d.drawText(win, "Lights", 50, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 600, 100, 100), 2)
    d.drawText(win, "Roads", 150, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 700, 100, 100), 2)
    d.drawText(win, "Junctions", 50, 720, 30, BLUE)
    pygame.draw.rect(win,BLUE, (0, 700, 100, 100), 2)
    d.drawText(win, "Other", 150, 720, 30, BLUE)

    firstQuart=0
    secondQuart=0

    for i in l:
        if i.pygameImgID==v.redAmber:
            if i.checkInside(0, 600, 100, 700):
                firstQuart=1
        elif i.pygameImgID==v.road:
            if i.checkInside(100, 600, 200, 700):
                secondQuart=1
    if firstQuart==0:
        l.append(classy.TrafficLight(40, 645))
    elif secondQuart==0:
        l.append(classy.Road(120, 645))

    return l

def junctionMenu(win, l):
    pygame.draw.rect(win,BLUE, (0, 600, 100, 100), 2)
    d.drawText(win, "New Junction", 50, 620, 21, BLUE)
    pygame.draw.rect(win,BLUE, (100, 600, 100, 100), 2)
    d.drawText(win, "4-Way", 150, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 700, 100, 100), 2)
    d.drawText(win, "Turn", 50, 720, 30, BLUE)
    pygame.draw.rect(win,BLUE, (0, 700, 100, 100), 2)
    d.drawText(win, "Back", 150, 720, 30, BLUE)

    firstQuart=0
    secondQuart=0
    thirdQuart=0
    for i in l:
        if i.pygameImgID==v.tJunct:
            if i.checkInside(0, 600, 100, 700):
                firstQuart=1
        elif i.pygameImgID==v.fourJunct:
            if i.checkInside(100, 600, 200, 700):
                secondQuart=1
        elif i.pygameImgID==v.splitJunct:
            if i.checkInside(0, 700, 100, 800):
                thirdQuart=1
    if firstQuart==0:
        l.append(classy.TJunction(20, 625))
    elif secondQuart==0:
        l.append(classy.FourJunction(120, 635))
    elif thirdQuart==0:
        l.append(classy.Turn(25, 725))

    return l

def otherMenu(win, l):
    pygame.draw.rect(win,BLUE, (0, 600, 100, 100), 2)
    d.drawText(win, "Edit", 50, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 600, 100, 100), 2)
    d.drawText(win, "Time", 150, 620, 30, BLUE)
    pygame.draw.rect(win,BLUE, (100, 700, 100, 100), 2)
    d.drawText(win, "Rotate", 50, 720, 20, BLUE)
    pygame.draw.rect(win,BLUE, (0, 700, 100, 100), 2)
    d.drawText(win, "Back", 150, 720, 30, BLUE)

    firstQuart=0
    secondQuart=0
    thirdQuart=0
    for i in l:
        if i.pygameImgID==v.edit:
            if i.checkInside(0, 600, 100, 700):
                firstQuart=1
        elif i.pygameImgID==v.timey:
            if i.checkInside(100, 600, 200, 700):
                secondQuart=1
        elif i.pygameImgID==v.rotateImg:
            if i.checkInside(0, 700, 100, 800):
                thirdQuart=1
    if firstQuart==0:
        l.append(classy.Edit(40, 645))
    elif secondQuart==0:
        l.append(classy.Time(140, 645))
    elif thirdQuart==0:
        l.append(classy.Rotate(40, 745))

    return l

