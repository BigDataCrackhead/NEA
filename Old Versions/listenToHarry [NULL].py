
import pygame
import Variables as v

class Object(object):
    def __init__(self, x, y, width, height, typ, id):
        self.typ=typ
        self.x=x
        self.y=y
        self.width=int(width)
        self.height=int(height)
        self.conn=[]
        self.rotation=360
        self.id=id
        self.special=[]

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

    def getSpecial(self):
        return self.special

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
        listy=(self.x, self.y, self.id, self.conn, self.rotation, self.special)
        return listy
        
class TrafficLight(Object):
    def __init__(self, x, y, conns, time):
        Object.__init__(self, x, y, "20", "20", v.redAmber, "TL")
        self.x=x
        self.y=y
        self.time=time
        self.conns=conns

    def setTimes(self, timeOne, timeTwo):
        self.time=(timeOne, timeTwo)

    def setSpecial(self):
        self.special=self.time

    

class Road(Object):
    def __init__(self, x, y, conns, length):
        Object.__init__(self, x, y, "60", "20", v.road, "RD")
        self.x=x
        self.y=y
        self.length=length
        self.conns=conns
        self.laneDistro=[1, 1]
    
    def setLaneDistro(self, laneDistro):
        self.laneDistro=laneDistro

    def pygameSux(self):
        listy=(self.x, self.y, self.id, self.conn, self.rotation, self.laneDistro, self.special)
        return listy

    def setSpecial(self):
        self.special=(self.length, self.laneDistro)

class FourJunction(Object):
    def __init__(self, x, y, conns, active):
        Object.__init__(self, x, y, "60", "60", v.fourJunct, "4J")
        self.x=x
        self.y=y
        self.conns=conns
        self.active=active
        self.cycle=[[], []]

    def setCycle(self):
        pass

    def setSpecial(self):
        self.special=self.cycle

class TJunction(Object):
    def __init__(self, x, y, conns, active):
        Object.__init__(self, x, y, "60", "60", v.tJunct, "TJ")
        self.x=x
        self.y=y
        self.conns=conns
        self.active=active

    def setCycle(self):
        pass

    def setSpecial(self):
        self.cycle

class Turn(Object):
    def __init__(self, x, y, conns, laneDistro):
        Object.__init__(self, x, y, "60", "60", v.splitJunct, "TN")
        self.x=x
        self.y=y
        self.conns=conns
        self.laneDistro=laneDistro



class Edit(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, "20", "20", v.edit, "ET")
        self.x=x
        self.y=y

class Time(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, "20", "20", v.timey, "TM")
        self.x=x
        self.y=y

    def move(self, x, y, win):
        pass

class Rotate(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, "20", "20", v.rotateImg, "RO")
        self.x=x
        self.y=y