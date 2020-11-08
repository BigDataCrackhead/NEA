import pygame, logging, math
import Menu as m
import Highlights as h
import Variables as v  

def drawTime(w, x, y, time):
    w.fill(v.BACKGROUND)

    h.highlighterTime(w, x, y)
    
    text="Time = "+str(time)

    drawText(w, "Return To Design Phase", 80, 20, 20, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (0, 10, 160, 20), 2)

    drawText(w, "Time Menu", 600, 150, 55, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (450, 100, 300, 100), 2)

    drawText(w, "One Unit of 'Time' = One Minute per in Simulation Second", 600, 350, 25, v.BLUE)
    
    drawText(w, text, 600, 400, 30, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (500, 375, 200, 50), 2)

    pygame.draw.rect(w, v.ORANGE, (350, 498, 500, 4))
    
    drawText(w, "Time1", 350, 450, 25, v.BLUE)
    pygame.draw.rect(w, v.ORANGE, (348, 470, 4, 30))
    drawText(w, "Time2", 475, 550, 25, v.BLUE)
    pygame.draw.rect(w, v.ORANGE, (473, 500, 4, 30))
    drawText(w, "Time3", 600, 450, 25, v.BLUE)
    pygame.draw.rect(w, v.ORANGE, (598, 470, 4, 30))
    drawText(w, "Time4", 725, 550, 25, v.BLUE)
    pygame.draw.rect(w, v.ORANGE, (723, 500, 4, 30))
    drawText(w, "Time5", 850, 450, 25, v.BLUE)
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

def drawEdit(w, x, y, initialX, initialY, obj, rot, special1, special2, t1, t2):

    #rotConverted=int((rot*(500/360))-350)
    rotConverted=rot

    w.fill(v.BACKGROUND)

    h.highlighterEdit(w, x, y)

    drawText(w, "Return To Design Phase", 80, 20, 20, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (0, 10, 160, 20), 2)

    drawText(w, "Edit Menu", 600, 150, 44, v.BLUE)
    pygame.draw.rect(w, v.BLUE, (500, 125, 200, 50), 2)

    w.blit(obj, (100, 100))

    truncatedX=math.floor(initialX)
    truncatedY=math.floor(initialY)

    xConverted=int((truncatedX*(500/1200))-350)
    yConverted=int((truncatedY*(500/800))-350)

    displayEdit(w, "X-Position", 280, truncatedX, xConverted)

    displayEdit(w, "Y-Position", 340, truncatedY, yConverted)
    
    displayEdit(w, "Rotation", 400, rot, rotConverted)
    
    temp=460
    forCountOne=0
    forCountTwo=0

    if type(special1)==int:
        specialOneConverted=int((special1*(500/4))+350)
        displayEdit(w, t1, temp, special1, specialOneConverted)
        temp+=60
    else:
        specialOneList=[]
        for spec in special1:
            specialOneConverted=int((spec*(500/4))+350)
            specialOneList.append(specialOneConverted)
            displayEdit(w, t1[forCountOne], temp, spec, specialOneConverted)
            temp+=60
            forCountOne+=1

    if type(special2)==int:
        specialTwoConverted=int((special2*(500/4))+350)
        displayEdit(w, t2, temp, special2, specialTwoConverted)
    else:
        specialTwoList=[]
        for spec in special2:
            specialTwoConverted=int((spec*(500/4))+350)
            specialTwoList.append(specialTwoConverted)
            displayEdit(w, t2[forCountTwo], temp, spec, specialTwoConverted)
            temp+=60
            forCountTwo+=1

    pygame.display.flip()
    listy=[(xConverted, 280, truncatedX), (yConverted, 340, truncatedY), (rotConverted, 400, rot)] 

    base=460

    if forCountOne==0:
        listy.append((specialOneConverted, base))
        base+=60
    else:
        for spec in specialOneList:
            listy.append((spec, base))
            base+=60

    if forCountTwo==0:
        listy.append((specialTwoConverted, base))
    else:
        for spec in specialTwoList:
            listy.append((spec, base))
            base+=60

    return listy

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

    if si==0:
        pygame.draw.rect(w, v.BLUE, (1000, 0, 100, 30), 2)
        drawText(w, "Save", 1050, 15, 30, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (1100, 0, 100, 30), 2)
        drawText(w, "Import", 1150, 15, 30, v.BLUE)
    elif si==1:
        pygame.draw.rect(w, v.BLUE, (1000, 0, 100, 30), 2)
        drawText(w, "File 1", 1050, 15, 30, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (1100, 0, 100, 30), 2)
        drawText(w, "File 2", 1150, 15, 30, v.BLUE)
    elif si==2:
        pygame.draw.rect(w, v.BLUE, (1000, 0, 100, 30), 2)
        drawText(w, "File 1", 1050, 15, 30, v.BLUE)
        pygame.draw.rect(w, v.BLUE, (1100, 0, 100, 30), 2)
        drawText(w, "File 2", 1150, 15, 30, v.BLUE)

    if menu==0:
        l=m.normalMenu(w, l)

    elif menu==1:
        l=m.junctionMenu(w, l)

    elif menu==2:
        l=m.otherMenu(w, l)

    for i in l:
        i.draw(w)

    pygame.display.flip()

def drawText(win, text, x, y, size, colour):
    try:
        font = pygame.font.SysFont("Comic Sans", size)
        toBlit = font.render(text, 1, colour, False)
        win.blit(toBlit, ( int( x-(toBlit.get_width()/2) ) , int( y-(toBlit.get_height()/2)) ))
    except:
        logging.warning('Font Error, Saw It Coming Ngl')