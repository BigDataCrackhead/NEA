import pygame
import logging
import math
import sys
import Menu as m
import Highlights as h
import Variables as v
import Click as click
import listenToHarry as classy
from pynput import keyboard

globalKey = None

def drawGUI(w, x, y):
    win.fill(v.BACKGROUND)

    h.highlighterGUI(w, x, y)

def groupEdit(w, g, l):
    pygame.display.set_caption('Group Edit: {}'.format(g.groupName))

    length = len(l)
    for x in range(length, 0, -1):  # Loops through the objects
        menu = l[x-1]
        # Removes objects that are generated for the menu
        if menu.checkInside(0, 600, 200, 800):
            l.remove(menu)
            classy.Object.counterStorage.append(menu.id)

    while True:
        w.fill(v.BACKGROUND)

        x, y = pygame.mouse.get_pos()

        h.highlightGroupEdit(w, g, x, y)

        drawText(w, "Return To Design Phase", 80, 20, 20, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (0, 10, 160, 20), 2)
        
        pygame.draw.rect(w, v.BLUE, (0, 600, 100, 100), 2)
        drawText(w, "Links", 50, 650, 35, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (100, 600, 100, 100), 2)
        drawText(w, "Members", 150, 650, 31, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (100, 700, 100, 100), 2)
        drawText(w, "Host", 50, 750, 35, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (0, 700, 100, 100), 2)
        drawText(w, "Done", 150, 750, 35, v.BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Goodbye!")
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x>0 and x<100:
                    if y>600 and y<700:
                        g=groupLink(g, w, l)
                    elif y>700 and y<800:
                        g=mainGroupElementDraw(g, w, l)
                if x>100 and x<200:
                    if y>600 and y<700:
                        g=groupMemberEditDraw(w, g, l)
                    elif y>700 and y<800:
                        return g

        for i in l:
            i.draw(w)

        pygame.display.flip()

def groupLink(g, w, l):
    pygame.display.set_caption("Link Traffic Lights")

    currentItem=None
    colourList=[v.GREEN, v.ORANGE, v.REALBLUE, v.REALORANGE]

    while True:
        w.fill(v.BACKGROUND)

        x, y = pygame.mouse.get_pos()

        h.highlightGroupLink(w, currentItem, x, y)

        tempIndex=0
        for index in g.direction:
            colour=colourList[tempIndex]
            tempIndex+=1
            for item in index:
                temp=item.getXY()
                pygame.draw.rect(w, colour, (temp[0]-4, temp[1]-4, temp[2]+8, temp[3]+8))

        drawText(w, "Return To Design Phase", 80, 20, 20, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (0, 10, 160, 20), 2)

        if currentItem:
            pygame.draw.rect(w, v.BLUE, (0, 600, 100, 100), 2)
            drawText(w, "North", 50, 650, 35, v.BLUE)
            pygame.draw.rect(w, v.BLUE, (100, 600, 100, 100), 2)
            drawText(w, "East", 150, 650, 31, v.BLUE)
            pygame.draw.rect(w, v.BLUE, (100, 700, 100, 100), 2)
            drawText(w, "South", 50, 750, 35, v.BLUE)
            pygame.draw.rect(w, v.BLUE, (0, 700, 100, 100), 2)
            drawText(w, "West", 150, 750, 35, v.BLUE)
        else:
            drawText(w, "Done", 100, 700, 40, v.BLUE)
            pygame.draw.rect(w, v.BLUE, (0, 600, 200, 200), 2)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Goodbye!")
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not currentItem:
                    if x>0 and x<200:
                        if y>600 and y<800:
                            return g

                    for item in l:
                        if item.typ=="TL":
                            temp=item.getXY()
                            if x>temp[0] and x<temp[0]+temp[2]:
                                if y>temp[1] and y<temp[1]+temp[3]:
                                    currentItem=item
                            
                if currentItem:
                    if g.inDirections(currentItem):
                        if x>0 and x<100:
                            if y>600 and y<700:
                                try:
                                    g.removeDirection(currentItem, 0)
                                except:
                                    if currentItem in g.direction[1]:
                                        g.removeDirection(currentItem, 1)
                                    elif currentItem in g.direction[2]:
                                        g.removeDirection(currentItem, 2)
                                    elif currentItem in g.direction[3]:
                                        g.removeDirection(currentItem, 3)
                                    g.addDirection(currentItem, 0)
                                currentItem=None
                            elif y>700 and y<800:
                                try:
                                    g.removeDirection(currentItem, 1)
                                except:
                                    if currentItem in g.direction[0]:
                                        g.removeDirection(currentItem, 0)
                                    elif currentItem in g.direction[2]:
                                        g.removeDirection(currentItem, 2)
                                    elif currentItem in g.direction[3]:
                                        g.removeDirection(currentItem, 3)
                                    g.addDirection(currentItem, 1)
                                currentItem=None
                        elif x>100 and x<200:
                            if y>600 and y<700:
                                try:
                                    g.removeDirection(currentItem, 2)
                                except:
                                    if currentItem in g.direction[1]:
                                        g.removeDirection(currentItem, 1)
                                    elif currentItem in g.direction[0]:
                                        g.removeDirection(currentItem, 0)
                                    elif currentItem in g.direction[3]:
                                        g.removeDirection(currentItem, 3)
                                    g.addDirection(currentItem, 2)
                                currentItem=None
                            elif y>700 and y<800:
                                try:
                                    g.removeDirection(currentItem, 3)
                                except:
                                    if currentItem in g.direction[1]:
                                        g.removeDirection(currentItem, 1)
                                    elif currentItem in g.direction[2]:
                                        g.removeDirection(currentItem, 2)
                                    elif currentItem in g.direction[0]:
                                        g.removeDirection(currentItem, 0)
                                    g.addDirection(currentItem, 3)
                                currentItem=None
                    else:
                        if x>0 and x<100:
                            if y>600 and y<700:
                                g.addDirection(currentItem, 0)
                                currentItem=None
                            elif y>700 and y<800:
                                g.addDirection(currentItem, 1)
                                currentItem=None
                        elif x>100 and x<200:
                            if y>600 and y<700:
                                g.addDirection(currentItem, 2)
                                currentItem=None
                            elif y>700 and y<800:
                                g.addDirection(currentItem, 3)
                                currentItem=None
                    try:
                        print(currentItem.id, g.direction)
                    except:
                        pass                                

        for i in l:
            i.draw(w)

        pygame.display.flip()

def groupMemberEditDraw(w, g, l):
    pygame.display.set_caption('Select Group Members:')

    while True:
        groupMembers = g.getGroupMembers()

        x, y = pygame.mouse.get_pos()

        w.fill(v.BACKGROUND)

        back = h.highlighterGroupHost(w, x, y)

        for item in groupMembers:
            temp=item.getXY()
            pygame.draw.rect(
                w, v.OFFBLUE, (temp[0]-4, temp[1]-4, temp[2]+8, temp[3]+8))

        drawText(w, "Return To Design Phase", 80, 20, 20, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (0, 10, 160, 20), 2)

        drawText(w, "Done", 100, 700, 40, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (0, 600, 200, 200), 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Goodbye!")
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back:
                    logging.warning("Leaving Group Naming")
                    return g
                elif x > 0 and x < 200:
                    if y > 600 and y < 800:
                        return g

                for item in l:
                    temp=item.getXY()
                    if x>temp[0] and x<temp[0]+temp[2]:
                        if y>temp[1] and y<temp[1]+temp[3]:
                            if item.typ=="TL":
                                if item in groupMembers:
                                    g.removeMember(item)
                                    item.setGroup(None)
                                else:
                                    g.addMember(item)
                                    item.setGroup(g)

        for i in l:
            i.draw(w)

        pygame.display.flip()


def mainGroupElementDraw(g, w, l):
    pygame.display.set_caption('Select Host Element:')

    length = len(l)
    for x in range(length, 0, -1):  # Loops through the objects
        menu = l[x-1]
        # Removes objects that are generated for the menu
        if menu.checkInside(0, 600, 200, 800):
            l.remove(menu)
            classy.Object.counterStorage.append(menu.id)

    while True:
        groupHost = g.getGroupHost()

        x, y = pygame.mouse.get_pos()

        w.fill(v.BACKGROUND)

        back = h.highlighterGroupHost(w, x, y, groupHost)

        drawText(w, "Return To Design Phase", 80, 20, 20, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (0, 10, 160, 20), 2)

        drawText(w, "Done", 100, 700, 40, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (0, 600, 200, 200), 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Goodbye!")
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back:
                    logging.warning("Leaving Group Naming")
                    return None
                elif x > 0 and x < 200:
                    if y > 600 and y < 800:
                        return g
                        
                for item in l:
                    if item.typ == "4J" or item.typ == "TJ" or item.typ == "RD":
                        if item.checkWithin(x, y):
                            if groupHost == item:
                                g.setGroupHost(None)
                                item.setGroup(None)
                            else:
                                g.setGroupHost(item)
                                item.setGroup(g)

        for i in l:
            i.draw(w)

        pygame.display.flip()


def onPress(key):
    global globalKey
    try:
        globalKey = key.char.replace("'", "")
    except AttributeError:
        if key == keyboard.Key.space:
            globalKey = " "
        elif key == keyboard.Key.backspace:
            globalKey = "Wait, Go Back"
        elif key == keyboard.Key.enter:
            globalKey = "Aight, That Will Do"


def onRelease(key):
    global globalKey
    globalKey = None


def groupNameDraw(w):
    name = []

    listener = keyboard.Listener(on_press=onPress, on_release=onRelease)
    listener.start()

    clock = pygame.time.Clock()
    lastKey = None

    while True:
        global globalKey

        clock.tick(60)

        x, y = pygame.mouse.get_pos()

        w.fill(v.BACKGROUND)

        back = h.highlighterGroupName(w, x, y)

        drawText(w, "Return To Design Phase", 80, 20, 20, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (0, 10, 160, 20), 2)

        drawText(w, "Enter The Group Name", 600, 300, 35, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (400, 400, 400, 100), 5)

        temp = ''.join(name)

        drawText(w, temp, 600, 450, 30, v.BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Goodbye!")
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back:
                    logging.warning("Leaving Group Naming")
                    listener.stop()
                    return None

        if len(name) > 30:
            return temp
        else:
            if globalKey != lastKey:
                if globalKey != None:
                    if globalKey == 'Wait, Go Back':
                        try:
                            name.pop()
                        except:
                            pass
                    elif globalKey == 'Aight, That Will Do':
                        return temp
                    else:
                        name.append(globalKey)

        lastKey = globalKey

        pygame.display.flip()


def drawTime(w, x, y, time):

    w.fill(v.BACKGROUND)

    h.highlighterTime(w, x, y)

    text = "Time = "+str(int((time-350)*2))

    drawText(w, "Return To Design Phase", 80, 20, 20, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (0, 10, 160, 20), 2)

    drawText(w, "Time Menu", 600, 150, 55, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (450, 100, 300, 100), 2)

    drawText(w, "One Unit of 'Time' = One Minute per in Simulation Second",
             600, 350, 25, v.BLUE)

    drawText(w, text, 600, 400, 30, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (500, 375, 200, 50), 2)

    pygame.draw.rect(w, v.ORANGE, (350, 498, 500, 4))

    drawText(w, "0", 350, 450, 25, v.BLUE)
    pygame.draw.rect(w, v.ORANGE, (348, 470, 4, 30))
    drawText(w, "250", 475, 550, 25, v.BLUE)
    pygame.draw.rect(w, v.ORANGE, (473, 500, 4, 30))
    drawText(w, "500", 600, 450, 25, v.BLUE)
    pygame.draw.rect(w, v.ORANGE, (598, 470, 4, 30))
    drawText(w, "750", 725, 550, 25, v.BLUE)
    pygame.draw.rect(w, v.ORANGE, (723, 500, 4, 30))
    drawText(w, "1000", 850, 450, 25, v.BLUE)
    pygame.draw.rect(w, v.ORANGE, (848, 470, 4, 30))

    drawText(w, "Done", 600, 600, 35, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (560, 580, 80, 40), 2)

    if time:
        pygame.draw.circle(w, v.BLACK, (time, 500), 8)
        pygame.draw.rect(w, v.BLACK, (time-1, 470, 2, 60))

    pygame.display.flip()


def editJunction(w, x, y, objectX, objectY, obj, rot, states, exits):
    w.fill(v.BACKGROUND)

    h.highlighterEdit(w, x, y)


def displayEdit(w, title, yPos, xPos, converted):
    drawText(w, title+": "+str(xPos), 600, yPos-40, 30, v.BLUE)
    pygame.draw.rect(w, v.ORANGE, (350, yPos-2, 500, 4))
    pygame.draw.circle(w, v.BLACK, (converted, yPos), 5)
    pygame.draw.rect(w, v.BLACK, (converted-1, yPos-10, 2, 20))


def junctionEditBlock(w, attr, obj):
    yPos = 300
    for propertea in attr:
        pygame.draw.circle(w, v.LB, (450, yPos), 12)
        pygame.draw.circle(w, v.LB, (550, yPos), 12)
        pygame.draw.circle(w, v.LB, (650, yPos), 12)
        if obj.getTyp() == "4J":
            pygame.draw.circle(w, v.LB, (750, yPos), 12)

        if "Pink" in propertea:
            pygame.draw.circle(w, v.BLUE, (450, yPos), 8)

        if "Blue" in propertea:
            pygame.draw.circle(w, v.BLUE, (550, yPos), 8)

        if "Green" in propertea:
            pygame.draw.circle(w, v.BLUE, (650, yPos), 8)

        if "Orange" in propertea:
            pygame.draw.circle(w, v.BLUE, (750, yPos), 8)

        yPos += 50
    if yPos >= 400:
        pygame.draw.circle(w, v.OFFBLUE, (778, yPos-57), 8)
        pygame.draw.rect(w, v.ORANGE, (771, yPos-59, 14, 4))
    if yPos <= 600:
        pygame.draw.circle(w, v.OFFBLUE, (600, yPos), 16)
        pygame.draw.rect(w, v.BLUE, (588, yPos-3, 24, 6))
        pygame.draw.rect(w, v.BLUE, (597, yPos-12, 6, 24))


def drawJunctionMenu(w, obj, x, y):
    objX = str(math.floor(obj.x))
    objY = str(math.floor(obj.y))
    objRot = obj.rotation
    if objRot == 360:
        objRot = "0"
    else:
        objRot = str(objRot)

    w.fill(v.BACKGROUND)

    h.highlighterEdit(w, x, y, obj)

    if obj.group:
        drawText(w, obj.group.groupName, 100, 500, 25, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (40, 490, 120, 20), 2)

    drawText(w, "Return To Design Phase", 80, 20, 20, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (0, 10, 160, 20), 2)

    drawText(w, "Edit Menu", 600, 150, 44, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (500, 125, 200, 50), 2)

    drawText(w, "Done", 600, 650, 40, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (550, 625, 100, 50), 2)

    image = pygame.transform.scale(obj.pygameImgID, (150, 150))
    w.blit(image, (100, 100))

    pygame.draw.rect(w, v.OFFBLUE, (40, 280, 120, 130), 5)
    drawText(w, "Info:", 100, 300, 40, v.BLUE)
    drawText(w, "x: "+objX, 100, 350, 30, v.BLUE)
    drawText(w, "y: "+objY, 100, 370, 30, v.BLUE)
    drawText(w, "rotation: "+objRot, 100, 390, 30, v.BLUE)

    # JUNCTION THINGS

    drawText(w, "Different Traffic Cycles:", 600, 200, 35, v.BLUE)
    drawText(w, "Pink", 450, 250, 30, v.PINK)
    drawText(w, "Blue", 550, 250, 30, v.REALBLUE)
    drawText(w, "Green", 650, 250, 30, v.GREEN)
    if obj.getTyp() == "4J":
        drawText(w, "Orange", 750, 250, 30, v.REALORANGE)

    objAttributes = obj.getSpecial()

    junctionEditBlock(w, objAttributes, obj)

    pygame.display.flip()


def junctionMenu(w, inp, itemList):
    tolerance = 8
    lastClick = False
    clock = pygame.time.Clock()
    while True:
        clickCheck = False

        x, y = pygame.mouse.get_pos()

        drawJunctionMenu(w, inp, x, y)

        if pygame.mouse.get_pressed()[0]:
            if click.checkWithin(x, y, 0, 10, 160, 20) or click.checkWithin(x, y, 550, 625, 100, 50):
                return inp

            elif not lastClick:
                coord = 300
                special = inp.getSpecial()
                length = len(special)

                if click.checkWithin(x, y, 40, 490, 120, 20):
                    if inp.group:
                        groupEdit(w, inp.group, itemList)

                for prop in range(length):
                    if y > coord-tolerance and y < coord+tolerance:
                        if x > 450-tolerance and x < 450+tolerance:
                            print("Pink")
                            if "Pink" in special[prop]:
                                special[prop].remove("Pink")
                            else:
                                special[prop].append("Pink")

                        elif x > 550-tolerance and x < 550+tolerance:
                            print("Blue")
                            if "Blue" in special[prop]:
                                special[prop].remove("Blue")
                            else:
                                special[prop].append("Blue")

                        elif x > 650-tolerance and x < 650+tolerance:
                            print("Green")
                            if "Green" in special[prop]:
                                special[prop].remove("Green")
                            else:
                                special[prop].append("Green")

                        elif x > 750-tolerance and x < 750+tolerance:
                            if inp.getTyp() == "4J":
                                print("Orange")
                                if "Orange" in special[prop]:
                                    special[prop].remove("Orange")
                                else:
                                    special[prop].append("Orange")

                    coord += 50
                if length > 1:
                    if y > coord-57-8 and y < coord-57+8:
                        if x > 778-8 and x < 778+8:
                            special.pop(length-1)

                if length <= 7:
                    if y > coord-16 and y < coord+16:
                        if x > (600-16) and x < (600+16):
                            special.append([])

                inp.setSpecial(special)
            clickCheck = True

        clock.tick(60)
        lastClick = clickCheck

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Goodbye!")
                sys.exit()


def drawRoadMenu(w, obj, x, y):
    objX = str(math.floor(obj.x))
    objY = str(math.floor(obj.y))
    objRot = obj.rotation
    if objRot == 360:
        objRot = "0"
    else:
        objRot = str(objRot)

    w.fill(v.BACKGROUND)

    h.highlighterEdit(w, x, y, obj)

    if obj.group:
        drawText(w, obj.group.groupName, 100, 500, 25, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (40, 490, 120, 20), 2)


    drawText(w, "Return To Design Phase", 80, 20, 20, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (0, 10, 160, 20), 2)

    drawText(w, "Edit Menu", 600, 150, 44, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (500, 125, 200, 50), 2)

    drawText(w, "Done", 600, 650, 40, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (550, 625, 100, 50), 2)

    image = pygame.transform.scale(obj.pygameImgID, (150, 150))
    w.blit(image, (100, 100))

    pygame.draw.rect(w, v.OFFBLUE, (40, 280, 120, 130), 5)
    drawText(w, "Info:", 100, 300, 40, v.BLUE)
    drawText(w, "x: "+objX, 100, 350, 30, v.BLUE)
    drawText(w, "y: "+objY, 100, 370, 30, v.BLUE)
    drawText(w, "rotation: "+objRot, 100, 390, 30, v.BLUE)

    displayEdit(w, "Length in Metres", 340, obj.length,
                math.floor((((obj.length-1)*500)/999)+350))

    displayEdit(w, "Red Side Lanes", 400, obj.laneDistro[0], int(
        ((obj.laneDistro[0]*500)/4)+350))
    displayEdit(w, "Blue Side Lanes", 460, obj.laneDistro[1], int(
        ((obj.laneDistro[1]*500)/4)+350))

    pygame.display.flip()


def roadMenu(w, inp, itemList):

    lastClick = False
    temp = None

    clock = pygame.time.Clock()

    while True:
        clickCheck = False

        x, y = pygame.mouse.get_pos()

        drawRoadMenu(w, inp, x, y)

        if pygame.mouse.get_pressed()[0]:
            if lastClick:
                if x < 350:
                    x = 350
                elif x > 850:
                    x = 850

                windowValue = inp.getSpecial()
                windowValue[temp-1] = x
                inp.setSpecial(windowValue)
                clickCheck = True
            else:
                temp = inp.mouseOverSpecial(x, y)
                if temp:
                    print("Getting Special Values", inp.getSpecial())
                    values = inp.getSpecial()
                    values[temp-1] = x
                    inp.setSpecial(values)
                    clickCheck = True

                elif click.checkWithin(x, y, 40, 490, 120, 20):
                    if inp.group:
                        groupEdit(w, inp.group, itemList)
                elif click.checkWithin(x, y, 0, 10, 160, 20) or click.checkWithin(x, y, 550, 625, 100, 50):
                    return inp

        clock.tick(60)
        lastClick = clickCheck

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Goodbye")
                sys.exit()


def drawAll(w, x, y, l, menu, si):
    w.fill(v.BACKGROUND)

    h.highlighter(w, x, y)

    drawText(w, "Return To Menu", 60, 20, 20, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (0, 10, 120, 20), 2)

    drawText(w, "Run MRS", 1120, 760, 40, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (1050, 740, 140, 35), 2)
    drawText(w, "Run GUI", 1120, 700, 40, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (1050, 680, 140, 35), 2)
    w.blit(v.binny, (200, 740))

    if si == 0:
        pygame.draw.rect(w, v.BLUE, (1000, 0, 100, 30), 2)
        drawText(w, "Save", 1050, 15, 30, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (1100, 0, 100, 30), 2)
        drawText(w, "Import", 1150, 15, 30, v.BLUE)
    elif si == 1:
        pygame.draw.rect(w, v.BLUE, (1000, 0, 100, 30), 2)
        drawText(w, "File 1", 1050, 15, 30, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (1100, 0, 100, 30), 2)
        drawText(w, "File 2", 1150, 15, 30, v.BLUE)
    elif si == 2:
        pygame.draw.rect(w, v.BLUE, (1000, 0, 100, 30), 2)
        drawText(w, "File 1", 1050, 15, 30, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (1100, 0, 100, 30), 2)
        drawText(w, "File 2", 1150, 15, 30, v.BLUE)

    if menu == 0:
        l = m.normalMenu(w, l)

    elif menu == 1:
        l = m.junctionMenu(w, l)

    elif menu == 2:
        l = m.otherMenu(w, l)

    for i in l:
        i.draw(w)

    pygame.display.flip()


def drawText(win, text, x, y, size, colour):
    try:
        font = pygame.font.SysFont("Comic Sans", size)
        toBlit = font.render(text, 1, colour, False)
        win.blit(toBlit, (int(x-(toBlit.get_width()/2)),
                          int(y-(toBlit.get_height()/2))))
    except:
        logging.warning('Font Error, Saw It Coming Ngl')
