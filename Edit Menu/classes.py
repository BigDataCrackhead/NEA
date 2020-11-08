import pygame, math
import Variables as v

counter=0

class Object(object):
    def __init__(self, x, y, width, height, pygameImgID, typ):

        global counter
        counter+=1
        self.ID=counter

        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.pygameImgID=pygameImgID
        self.typ=typ
        self.rotation=360

    def mouseOverSpecial(self, x, y):
        accuracy=8
        listy=self.getSpecial()
        
        for iteration in range(3):
            temp=iteration*60
            yValue=340+temp
            
            if y>yValue-accuracy and y<yValue+accuracy:
                if x>listy[iteration]-accuracy and x<listy[iteration]+accuracy:
                    #print(x, y, iteration, listy[iteration], temp)
                    return iteration+1
        return False

    def getTyp(self):
        return self.typ

    def draw(self, win):
        win.blit(v.road, (self.x, self.y))

class TJunction(Object):
    def __init__(self, x, y, conns=[]):
        Object.__init__(self, x, y, 60, 60, v.tJunct, "TJ")
        self.x=x
        self.y=y
        self.exits=["South", "East", "West"]
        self.laneRules=[["Pink", "Blue"], ["Pink", "Green"]]

    def getSpecial(self):
        return self.laneRules
    
    def setSpecial(self, listy):
        self.laneRules=listy

class FourJunction(Object):
    def __init__(self, x, y, conns=[]):
        Object.__init__(self, x, y, 60, 60, v.fourJunct, "4J")
        self.x=x
        self.y=y
        self.exits=["North", "South", "East", "West"]
        self.laneRules=[["Pink", "Blue"], ["Green", "Orange"]]

    def getSpecial(self):
        return self.laneRules
    
    def setSpecial(self, listy):
        self.laneRules=listy

class Road(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, 60, 20, v.road, "RD")
        
        self.length=100
        self.laneDistro=(1, 1)
    
    def getRealSpecial(self):
        return [self.length, self.laneDistro]

    def getSpecial(self):
        return [math.ceil((((self.length-1)*500)/999)+350), int(((self.laneDistro[0]*500)/4)+350), int(((self.laneDistro[1]*500)/4)+350)]

    def setSpecial(self, listy):
        self.length = math.floor((((listy[0]-350)*999)/500)+1)
        self.laneDistro = (round(((listy[1]-350)*4)/500), round(((listy[2]-350)*4)/500))
        