import pygame, sys, logging, math
import classes as c
import Highlights as h
import Variables as v
import Click as click

pygame.display.init()
pygame.font.init()

clock=pygame.time.Clock()

w = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Test')

inputt=c.TJunction(600, 400)

def drawText(win, text, x, y, size, colour):
    try:
        font = pygame.font.SysFont("Comic Sans", size)
        toBlit = font.render(text, 1, colour, False)
        win.blit(toBlit, ( int( x-(toBlit.get_width()/2) ) , int( y-(toBlit.get_height()/2)) ))
    except:
        logging.warning('Font Error, Saw It Coming Ngl')

def junctionEditBlock(w, attr, obj):
    yPos=300
    for propertea in attr:
        pygame.draw.circle(w, v.LB, (450, yPos), 12)
        pygame.draw.circle(w, v.LB, (550, yPos), 12)
        pygame.draw.circle(w, v.LB, (650, yPos), 12)
        if obj.getTyp()=="4J":
            pygame.draw.circle(w, v.LB, (750, yPos), 12)
        
        if "Pink" in propertea:
            pygame.draw.circle(w, v.BLUE, (450, yPos), 8)
        
        if "Blue" in propertea:
            pygame.draw.circle(w, v.BLUE, (550, yPos), 8)
        
        if "Green" in propertea:
            pygame.draw.circle(w, v.BLUE, (650, yPos), 8)

        if "Orange" in propertea:
            pygame.draw.circle(w, v.BLUE, (750, yPos), 8)

        yPos+=50
    if yPos>=400:
        pygame.draw.circle(w, v.OFFBLUE, (778, yPos-57), 8)
        pygame.draw.rect(w, v.ORANGE, (771, yPos-59, 14, 4))
    if yPos<=600:
        pygame.draw.circle(w, v.OFFBLUE, (600, yPos), 16)
        pygame.draw.rect(w, v.BLUE, (588, yPos-3, 24, 6))
        pygame.draw.rect(w, v.BLUE, (597, yPos-12, 6, 24))

def drawJunctionMenu(w, obj, x, y):
    objX=str(math.floor(obj.x))
    objY=str(math.floor(obj.y))
    objRot=obj.rotation
    if objRot==360:
        objRot="0"
    else:
        objRot=str(objRot)
    
    w.fill(v.BACKGROUND)

    h.highlighterEdit(w, x, y)

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

    #JUNCTION THINGS

    drawText(w, "Different Traffic Cycles:", 600, 200, 35, v.BLUE)
    drawText(w, "Pink", 450, 250, 30, v.PINK)
    drawText(w, "Blue", 550, 250, 30, v.REALBLUE)
    drawText(w, "Green", 650, 250, 30, v.GREEN)
    if obj.getTyp()=="4J":
        drawText(w, "Orange", 750, 250, 30, v.REALORANGE)

    objAttributes=obj.getSpecial()
    
    junctionEditBlock(w, objAttributes, obj)

    pygame.display.flip()

def junctionMenu(w, inp):
    tolerance=8
    lastClick=False
    while True:
        clickCheck=False

        x, y = pygame.mouse.get_pos()

        drawJunctionMenu(w, inp, x, y)

        if pygame.mouse.get_pressed()[0]:
            if click.checkWithin(x, y, 0, 10, 160, 20) or click.checkWithin(x, y, 550, 625, 100, 50):
                    print("Goodbye!")
                    sys.exit()
            
            elif not lastClick:
                coord=300
                special=inp.getSpecial()
                length=len(special)

                for prop in range(length):
                    if y>coord-tolerance and y<coord+tolerance:
                        if x>450-tolerance and x<450+tolerance:
                            print("P")
                            if "Pink" in special[prop]:
                                special[prop].remove("Pink")
                            else:
                                special[prop].append("Pink")

                        elif x>550-tolerance and x<550+tolerance:
                            print("B")
                            if "Blue" in special[prop]:
                                special[prop].remove("Blue")
                            else:
                                special[prop].append("Blue")
                            
                        elif x>650-tolerance and x<650+tolerance:
                            print("G")
                            if "Green" in special[prop]:
                                special[prop].remove("Green")
                            else:
                                special[prop].append("Green")
                        
                        elif x>750-tolerance and x<750+tolerance:
                            if inp.getTyp()=="4J":
                                print("O")
                                if "Orange" in special[prop]:
                                    special[prop].remove("Orange")
                                else:
                                    special[prop].append("Orange")

                    coord+=50
                if length>1:
                    if y>coord-57-8 and y<coord-57+8:
                        if x>778-8 and x<778+8:
                            special.pop(length-1)

                if length<=7:
                    if y>coord-16 and y<coord+16:
                        if x>(600-16) and x<(600+16):
                            special.append([])

                inp.setSpecial(special)
            clickCheck=True

            

        clock.tick(60)
        lastClick=clickCheck

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print("Goodbye!")
                sys.exit()

junctionMenu(w, inputt)