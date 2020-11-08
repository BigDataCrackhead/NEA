import pygame, math
import Variables as v

class Object(object):
    counter=0
    counterStorage=[]
    def __init__(self, x, y, width, height, img, typ):

        if Object.counterStorage:
            self.id=Object.counterStorage.pop()
            print("Printing New ID:", self.id)
        else:
            self.id=Object.counter
            print("Printing New ID:", self.id)
            Object.counter+=1

        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.pygameImgID=img
        self.typ=typ
        self.rotation=360
        self.entities=None
        self.conns=[]
        self.group=None
        self.defineGeometry()

    def setGroup(self, group):
        self.group=group
        
    def getGroup(self):
        return self.group
    
    def inGroup(self):
        if self.group==None:
            return False
        return True
    
    def resetCounter(self):
        Object.counter=0
        
    def setId(self, ID):
        Object.counter-=1
        self.id=ID

    def defineGeometry(self):
        self.top=True
        self.left=True
        self.right=True
        self.bottom=True

    def getGeometry(self):
        listy=[]

        listy=self.getThatBeta()

        return listy

    def move(self, xMid, yMid, win):
        self.x=int(xMid-(self.width/2))
        self.y=int(yMid-(self.height/2))
        self.conns=[]

    def snap(self, newObj, e, win):
        """ try:
            self.conns=[]
        except:
            pass """

        if type(e[0])==int:
            if self.x+(self.width/2)>newObj.x+(self.width/2):
                self.move(newObj.x+newObj.width+(self.width/2), newObj.y+(newObj.height/2), win)
            else:
                self.move(newObj.x-(self.width/2), newObj.y+(newObj.height/2), win)
        else:
            if self.y+(self.height/2)>newObj.y+(self.height/2):
                self.move(newObj.x+(newObj.width/2), newObj.y+newObj.height+(self.height/2), win)
            else:
                self.move(newObj.x+(newObj.width/2), newObj.y-(self.height/2), win)

        self.addConnection(newObj.id)
    
    def addConnection(self, conn):
        if not conn in self.conns:
            self.conns.append(conn)
        print(self.id, ": ", self.conns)

    def delConnection(self, conn, itemList):
        for item in itemList:
            if conn==item.id:
                try:
                    item.conns.pop(self.id)
                except:
                    pass
        
        try:
            self.conns.pop(conn)
        except:
            pass

    def draw(self, win):
        win.blit(self.pygameImgID, (self.x, self.y))

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
        tup=(self.length, self.laneDistro)
        return tup

    def setSpecial(self, special):
        self.length, self.laneDistro=special

    def packUpObj(self):
        listy=(self.x, self.y, self.conns, self.rotation, self.typ, self.getSpecial(), self.id)
        return listy

    def updateGlobal(self, listy):
        global counter

        for item in listy:
            if item.id>counter:
                counter=item.id+1

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
    
    def getXY(self):
        return [self.x, self.y, self.width, self.height]

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
    
    def defineGeometry(self):
        self.top=False
        self.left=True
        self.right=True
        self.bottom=False

        tempRotation=360

        while not tempRotation==self.rotation:
            self.top, self.left, self.bottom, self.right = self.right, self.top, self.left, self.bottom

            tempRotation+=90
            if tempRotation==450:
                tempRotation=90

    def getThatBeta(self):
        listy=[]

        if self.top:
            listy.append(((self.x, self.x+self.width), self.y))
        if self.left:
            listy.append((self.x, (self.y, self.y+self.height)))
        if self.bottom:
            listy.append(((self.x, self.x+self.width), self.y+self.height))
        if self.right:
            listy.append((self.x+self.width, (self.y, self.y+self.height)))

        return listy

class TrafficLight(Object):
    def __init__(self, x, y, conns=[]):
        Object.__init__(self, x, y, 20, 20, v.redAmber, "TL")
        self.x=x
        self.y=y
        self.group=None
        self.groupList=[]

    def getSpecial(self):
        try:
            return self.group.groupName, self.groupList
        except:
            return None, self.groupList

    def setSpecial(self, groupData):
        self.group=groupData[0]
        self.groupList=groupData[1]

    def getThatBeta(self):
        listy=[]

        listy.append(((self.x, self.x+self.width), self.y))

        listy.append((self.x, (self.y, self.y+self.height)))
    
        listy.append(((self.x, self.x+self.width), self.y+self.height))
    
        listy.append((self.x+self.width, (self.y, self.y+self.height)))

        return listy

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

    def getThatBeta(self):
        listy=[]

        listy.append(((int(self.x+(1/3)*self.width), int(self.x+(2/3)*self.width)), self.y))

        listy.append((self.x, (int(self.y+(1/3)*self.height), int(self.y+(2/3)*self.height))))
    
        listy.append(((int(self.x+(1/3)*self.width), int(self.x+(2/3)*self.width)), self.y+self.height))
    
        listy.append((self.x+self.width, (int(self.y+(1/3)*self.height), int(self.y+(2/3)*self.height))))

        return listy

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
    
    def defineGeometry(self):
        self.top=False
        self.left=True
        self.right=True
        self.bottom=True

        tempRotation=360

        while not tempRotation==self.rotation:
            self.top, self.left, self.bottom, self.right = self.right, self.top, self.left, self.bottom

            tempRotation+=90
            if tempRotation==450:
                tempRotation=90

    def getThatBeta(self):
        listy=[]

        if self.top:
            listy.append(((int(self.x+(1/3)*self.width), int(self.x+(2/3)*self.width)), self.y))

        if self.left:
            listy.append((self.x, (int(self.y+(1/3)*self.height), int(self.y+(2/3)*self.height))))

        if self.bottom:
            listy.append(((int(self.x+(1/3)*self.width), int(self.x+(2/3)*self.width)), self.y+self.height))

        if self.right:
            listy.append((self.x+self.width, (int(self.y+(1/3)*self.height), int(self.y+(2/3)*self.height))))

        return listy

class Turn(Object):
    def __init__(self, x, y, conns=[]):
        Object.__init__(self, x, y, 60, 60, v.splitJunct, "TN")
        self.x=x
        self.y=y
        self.length=None
        self.laneDistro=[1, 1]
    
    def defineGeometry(self):
        self.top=False
        self.left=True
        self.right=False
        self.bottom=True

        tempRotation=360

        while not tempRotation==self.rotation:
            self.top, self.left, self.bottom, self.right = self.right, self.top, self.left, self.bottom

            tempRotation+=90
            if tempRotation==450:
                tempRotation=90

    def getThatBeta(self):
        listy=[]

        if self.top:
            listy.append(((int(self.x+(1/3)*self.width), int(self.x+(2/3)*self.width)), self.y))

        if self.left:
            listy.append((self.x, (int(self.y+(1/3)*self.height), int(self.y+(2/3)*self.height))))

        if self.bottom:
            listy.append(((int(self.x+(1/3)*self.width), int(self.x+(2/3)*self.width)), self.y+self.height))

        if self.right:
            listy.append((self.x+self.width, (int(self.y+(1/3)*self.height), int(self.y+(2/3)*self.height))))

        return listy

class Edit(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, 20, 20, v.edit, "ET")
        self.x=x
        self.y=y

    def getGeometry(self):
        return []

class Time(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, 20, 20, v.timey, "TM")
        self.x=x
        self.y=y

    def move(self, x, y, win):
        pass

    def getGeometry(self):
        return []

class Rotate(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, 20, 20, v.rotateImg, "RO")
        self.x=x
        self.y=y

    def getGeometry(self):
        return []
        
class Group():
    def __init__(self, groupName):
        self.groupName=groupName
        self.groupHost=None
        self.groupMembers=[]
        self.direction=[[], [], [], []]

    def infectGroup(self):
        self.groupHost.group=self
        for cleanItem in self.groupMembers:
            cleanItem.group=self

        print("Using Group:", self)
        print("Infecting Group Host:", self.groupHost)
        print("Infecting Group Members:", self.groupMembers)

    def inDirections(self, groupMember):
        if groupMember in self.direction[0] or groupMember in self.direction[1] or groupMember in self.direction[2] or groupMember in self.direction[3]:
            return True
        return False

    def addDirection(self, groupMember, index):
        self.direction[index].append(groupMember)
    
    def removeDirection(self, groupMember, index):
        self.direction[index].remove(groupMember)

    def getGroupHost(self):
        return self.groupHost

    def getGroupMembers(self):
        return self.groupMembers

    def setGroupHost(self, groupHost):
        self.groupHost=groupHost

    def addMember(self, groupMember):
        self.groupMembers.append(groupMember)
    
    def removeMember(self, groupMember):
        self.groupMembers.remove(groupMember)

    