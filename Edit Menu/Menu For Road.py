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

inputt=c.Road(600, 400)

def drawText(win, text, x, y, size, colour):
    try:
        font = pygame.font.SysFont("Comic Sans", size)
        toBlit = font.render(text, 1, colour, False)
        win.blit(toBlit, ( int( x-(toBlit.get_width()/2) ) , int( y-(toBlit.get_height()/2)) ))
    except:
        logging.warning('Font Error, Saw It Coming Ngl')

def displayEdit(w, title, yPos, xPos, converted):
    drawText(w, title+": "+str(xPos), 600, yPos-40, 30, v.BLUE)
    pygame.draw.rect(w, v.ORANGE, (350, yPos-2, 500, 4))
    pygame.draw.circle(w, v.BLACK, (converted, yPos), 5)
    pygame.draw.rect(w, v.BLACK, (converted-1, yPos-10, 2, 20))

def drawRoadMenu(w, obj, x, y):
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

    displayEdit(w, "Length in Metres", 340, obj.length, math.floor((((obj.length-1)*500)/999)+350))

    displayEdit(w, "Red Side Lanes", 400, obj.laneDistro[0], int(((obj.laneDistro[0]*500)/4)+350))
    displayEdit(w, "Blue Side Lanes", 460, obj.laneDistro[1], int(((obj.laneDistro[1]*500)/4)+350))
    
    pygame.display.flip()

def roadMenu(w, inp):

    lastClick=False
    temp=None
    
    while True:
        clickCheck=False

        x, y = pygame.mouse.get_pos()

        drawRoadMenu(w, inp, x, y)

        if pygame.mouse.get_pressed()[0]:
            if lastClick:
                if x<350:
                    x=350
                elif x>850:
                    x=850

                windowValue=inp.getSpecial()
                windowValue[temp-1]=x
                inp.setSpecial(windowValue)
                clickCheck=True
            else:
                temp=inp.mouseOverSpecial(x, y)
                if temp:
                    print(inp.getSpecial())
                    values=inp.getSpecial()
                    values[temp-1]=x
                    inp.setSpecial(values)
                    clickCheck=True

                elif click.checkWithin(x, y, 0, 10, 160, 20) or click.checkWithin(x, y, 550, 625, 100, 50):
                    print("Goodbye!")
                    sys.exit()
            
        clock.tick(60)
        lastClick=clickCheck

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print("Goodbye!")
                sys.exit()
roadMenu(w, inputt)