import pygame, math, random
import Variables as v

class Object(object):
    counter=0
    counterStorage=[]
    def __init__(self, x, y, width, height, img, typ):
        if Object.counterStorage:
            self.id=Object.counterStorage.pop()
        else:
            self.id=Object.counter
            Object.counter+=1
        print("Printing New ID:", self.id)

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
        self.end=[]
        self.speedLimit=30
        self.carList=[]
        self.defineGeometry()

    def hasNoConnections(self, direction, itemList):
        temp=0
        for connID in self.conns:
            for obj in itemList:
                if obj.id == connID:
                    conn=obj
            tempGeo=conn.getGeometry()
            for side in tempGeo:
                if type(side[0]) == int:
                    if (side[0] == direction[0]) and (self.y+(self.height/2) == (direction[1][0]+direction[1][1])/2):
                        temp=1
                else:
                    if (side[1] == direction[1]) and (self.x+(self.width/2) == (direction[0][0]+direction[0][1])/2):
                        temp=1

        if temp:
            return False
        return True

    def getConns(self):
        return self.conns

    def getCars(self):
        if self.carList:
            return self.carList
        else:
            return None

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
        self.length=1

    def getLights(self, route):
        return True

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
        self.length=10
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
        self.length=10
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
        self.length=100
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

class Car():
    bigCarData=[]
    def __init__(self, currentRoad, route):
        self.time=0
        self.timeWaiting=0 
        self.route=route 
        self.carLength=(random.randint(0, 8)*0.1)+1.2 
        self.acceleration=0 
        self.velocity=currentRoad.speedLimit-3+(random.randint(0, 5)) 
        self.targetVelocity=self.velocity 
        self.roadObject=currentRoad 
        self.roadIndex=0 
        self.distanceIntoRoadObject=0 
        self.following=False 
        self.follower=False 
        self.waiting=False  
        self.startTarget=[[],[]]
    
    def setTargetVelocity(self):
        self.targetVelocity = self.roadObject.speedLimit-3+(random.randint(0, 5))

    def tick(self, time, bigCarList): 
        carList=self.roadObject.getCars() 
        if self.velocity != 0: 
            self.waiting = False

        if self.roadObject.typ != "4J" and self.roadObject.typ != "TJ": 
            if self.velocity < self.targetVelocity: 
                self.acceleration = 0.5 
            elif self.velocity > self.targetVelocity: 
                self.acceleration = -0.5 

        #geometry=["north", "east", "south", "west"] 
        if self.roadObject.typ == "TJ" or self.roadObject.typ == "4J": 
            tempGroup = self.roadObject.group 
            if tempGroup:
                if self.roadIndex == 0:
                    if self.startTarget == [[],[]]:
                        tempEnd = self.roadObject.end
                        tempIndex = random.randint(len(tempEnd))

                        self.startTarget=tempEnd[tempIndex]
                        
                    comingFrom = self.startTarget
                
                for index in range(4): 
                    for obj in tempGroup.direction[index]: 
                        if obj in self.route: 
                            if obj == self.route[self.roadIndex-1] or obj == self.route[self.roadIndex-2]: 
                                comingFrom = index 
                            else:
                                goingTo = index 
                
                if (comingFrom+1 == goingTo) or (comingFrom+1 == 4 and goingTo == 0): 
                    if self.velocity > 8:
                        self.acceleration -= self.velocity * -0.5 

                elif (comingFrom+2 == goingTo) or (comingFrom+2 == 4 and goingTo == 0) or (comingFrom+2 == 5 and goingTo == 1): 
                    if self.velocity > 8: 
                        self.acceleration -= self.velocity * -0.5 

                else: 
                    for car in carList: 
                        if car.route[car.roadIndex-1] != self.route[self.roadIndex-1]: 
                            if not car.waiting: 
                                if car.route[car.roadIndex+1] == self.route[self.roadIndex+1]: 
                                    if self.velocity != 0: 
                                        self.acceleration = self.velocity * -0.5 
                        
                        else: 
                            if car.waiting: 
                                if car.distanceIntoRoadObject > self.distanceIntoRoadObject:
                                    if self.velocity != 0: 
                                        self.acceleration = self.velocity * -0.5 
                            


        if self.following: 
            if self.distanceIntoRoadObject > self.following.distanceIntoRoadObject: 
                self.acceleration = (self.following.velocity - self.velocity) * 5 * (1/(self.following.distanceIntoRoadObject+self.roadObject.length - self.distanceIntoRoadObject + self.following.carLength)) 
            else: 
                self.acceleration = (self.following.velocity - self.velocity) * 5 * (1/(self.following.distanceIntoRoadObject - self.distanceIntoRoadObject+self.following.carLength)) 

        else:
            for car in carList: 
                if car.distanceIntoRoadObject > self.distanceIntoRoadObject+car.carLength+1+(self.velocity*2) and car.follower == False and self.roadObject.typ != "TJ" and self.roadObject.typ != "4J" and car.route[car.roadIndex-1] == self.route[self.roadIndex-1]: 
                    car.follower=self
                    self.following=car 
        
        try:
            if self.route[self.roadIndex+1].typ == "TL": 
                if self.route[self.roadIndex+1].getLights(self.route) != "Green":
                    if self.roadObject.length-self.distanceIntoRoadObject>20: 
                        self.acceleration = -1*(self.velocity-(self.roadObject.length-self.distanceIntoRoadObject))
        except:
            pass

        self.time += time 
        if self.waiting: 
            self.timeWaiting += time 

        if self.distanceIntoRoadObject >= self.roadObject.length: 
            if self.roadIndex+1 < len(self.route): 
                self.newRoad()
                if self.follower:
                    if self.follower.roadIndex+1 < len(self.follower.route):
                        if self.follower.route[self.follower.roadIndex+1] != self.roadObject: 
                            self.follower.following=False 
                            self.follower=False 
            else: 
                bigCarList = self.destroy(bigCarList) 

        newVelocity = self.velocity + (self.acceleration * time) 
        if newVelocity <= 0: 
            newVelocity = 0 
        distanceTravelled = ((self.velocity+newVelocity)/2) * time 
        self.velocity = newVelocity 
        self.distanceIntoRoadObject += distanceTravelled 
        
        if self.velocity <= 1:
            self.velocity = 0
            self.waiting = True 

        return bigCarList 

    def newRoad(self): 
        self.roadObject.carList.remove(self) 
        self.roadIndex+=1 
        self.roadObject=self.route[self.roadIndex] 
        self.roadObject.carList.append(self)
        self.distanceIntoRoadObject=0 
        self.setTargetVelocity() 

    def destroy(self, bigCarList): 
        self.roadObject.carList.remove(self)
        bigCarList.remove(self) 
        self.roadObject = None 

        timeTaken = self.time 
        timeWaiting = self.timeWaiting 
        lastRoad = self.route[-1] 
        lengthOfRoute = 0
        for obj in self.route: 
            lengthOfRoute += obj.length 
    
        Car.bigCarData.append([timeTaken, lastRoad, lengthOfRoute, timeWaiting]) 

        return bigCarList 