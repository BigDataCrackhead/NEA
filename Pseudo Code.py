roadList=list of road and junction objects #So that you can navigate around the layout
groupList=list of groups of road/junction and traffic light objects #So that you can keep all traffic lights coordinated and cars on junctions know what is happening
endList=empty array #The list of all the roads that end on the edge of the layout
rateOfCars=the number of cars per in simulation second #A constant value previously set by the user to indicate the number of new cars added to the system per second
time=the number of in simulation seconds per real second #A constant set previously by the user such that the speed of a simulation can be controlled
tempFraction=int(0) #A variable to keep track of left over cars that need to be added to the simulation
carList=empty array #An array which will be used to keep track of all the cars added to the simulation
frameRate=60 #A constant value to make sure the simulation stays running in sync. This is only changed depending on how much processing power the sim needs.
simulationLength=3600

CLASS Car: #The car class that contains all the cars added to the system
    METHOD constructor (self, currentRoad, route): 
        self.time=0
        self.timeWaiting=0
        self.route=route
        self.carLength=(RANDOMINT(0->8)*0.1)+1.2
        self.acceleration=0
        self.velocity=currentRoad.speedLimit-3+RANDOMINT(0->6)
        self.roadObject=currentRoad
        self.roadIndex=0
        self.distanceIntoRoadObject=0
        self.following=False
        self.follower=False
        self.waiting=False

    METHOD tick (self, time, bigCarList):
        #average car length roughly = 4.6m
        carList=self.roadObject.getCars()
        IF self.velocity != 0:
            self.waiting = False

        geometry=["north", "east", "south", "west"]
        IF self.roadObject,typ = "TJ" OR selr.roadObject.typ = "4J":
            tempGroup = self.roadObject.group
            FOR (index=0; index<4; index+=1):
                FOR obj IN tempGroup.direction[index]:
                    IF obj IN self.route:
                        IF obj = self.route[self.roadIndex-1] OR obj = self.route[self.roadIndex-2]:
                            comingFrom = index
                        ELSE:
                            goingTo = index
            
            
            IF (comingFrom+1 = goingTo) OR (comingFrom+1 = 4 AND goingTo = 0):
                IF self.velocity > 8:
                    self.acceleration -= self.velocity * -0.5

            ELIF (comingFrom+2 = goingTo) OR (comingFrom+2 = 4 AND goingTo = 0) OR (comingFrom+2 = 5 AND goingTo = 1):
                IF self.velocity > 8:
                    self.acceleration -= self.velocity * -0.5

            ELSE:
                FOR car IN carList:
                    IF NOT car.waiting:
                        IF car.route[car.roadIndex+1] = self.route[roadIndex+1]:
                            IF car.route[car.roadIndex-1] != self.route[roadIndex-1]:
                                IF self.velocity != 0:
                                    self.acceleration = self.velocity * -0.5
                                ELSE:
                                    self.waiting = True
                            


        IF self.following:
            IF self.distanceIntoRoadObject > self.following.distanceIntoRoadObject:
                self.acceleration = (self.following.velocity - self.velocity) * 5 * (1/(self.following.distanceIntoRoadObject+self.roadObject.length - self.distanceIntoRoadObject + self.following.carLength))
            ELSE:
                self.acceleration = (self.following.velocity - self.velocity) * 5 * (1/(self.following.distanceIntoRoadObject - self.distanceIntoRoadObject+self.following.carLength))

        ELSE:
            FOR car IN carList:
                IF car.distanceIntoRoadObject > self.distanceIntoRoadObject+car.carLength+1+(self.velocity*2):
                    car.follower=self
                    self.following=car
        
        IF self.route[self.index+1].typ = "TL":
            IF self.route[self.index+1].getLights(self.route) != "Green":
                IF self.roadObject.length-self.distanceIntoRoadObject>20:
                    self.acceleration = -1*(self.velocity-(self.roadObject.length-self.distanceIntoRoadObject)

        self.time += time
        IF self.waiting:
            self.timeWaiting += time

        IF self.distanceIntoRoadObject >= self.roadObject.length:
            IF self.roadIndex+1 < LENGTH(self.route):
                self.newRoad()
                IF self.follower.route[roadIndex+1] != self.roadObject:
                    self.follower.following=False
                    self.follower=False
            ELSE:
                bigCarList = self.destroy(bigCarList)

        newVelocity = self.velocity + (self.acceleration * time)
        IF newVelocity <= 0:
            newVelocity = 0
        distanceTravelled = ((self.velocity+newVelocity)/2) * time
        self.velocity=newVelocity
        self.distanceIntoRoadObject += distanceTravelled
        
        IF self.velocity <= 1:
            self.velocity = 0
            self.waiting = True

        IF NOT self.roadObject:
            RETURN bigCarList

    METHOD newRoad (self):
        self.roadObject.carList.REMOVE(self)
        self.roadIndex+=1
        self.roadObject=route[roadIndex]
        self.roadObject.carList.APPEND(self)
        self.distanceIntoRoadObject=0

    METHOD destroy (self, bigCarList):
        self.roadObject.carList.REMOVE(self)
        bigCarList.REMOVE(self)
        self.roadObject = NONE

        timeTaken = self.time
        timeWaiting = self.timeWaiting
        lastRoad = self.route[-1]
        lengthOfRoute = 0
        FOR obj IN self.route:
            lengthOfRoute.APPEND(obj.length)
    
        GLOBAL bigCarData.APPEND(timeTaken, lastRoad, lengthOfRoute, timeWaiting)

        RETURN bigCarList
    
PROCEDURE wait (timePeriod):
    realTimePassed = getTimePassed()

    HALT program FOR (timePeriod-realTimePassed)

FUNCTION findRoute (entry, exit): #A function to find a new route
    finalRoute=[]
    finalRoute.APPEND(entry)
    WHILE finalRoute[-1] != exit:
        tempConns=finalRoute[-1].getConnections()
        chosenConn=RANDOMINT(0->(LENGTH(tempConns)-1))
        chosenConn=tempConns[chosenConn]
        finalRoute.APPEND(chosenConn)
    RETURN finalRoute

FOR object IN roadList:
    IF LENGTH(object.connections) < 2:
        endList.APPEND(object)
        FOR direction IN object.geometry:
            IF direction==True and object.hasNoConnections(direction):
                object.end.APPEND(direction)

timePassed=time/frameRate #The amount of system time that will pass per frame

WHILE simulationLength > totalTimePassed: #While the simulation hasn't been running for it's time limit sets to true
    wait(1/frameRate) #Makes sure the simulation isn't running faster than the framerate it should be
    
    newCars=(rateOfCars*time)+tempFraction #Gets how many cars should be created this frame
    tempFraction=newCars%1 #This usually won't be an integer so gets the fractional part and stores this for next frame
    newCars=TRUNCATE(newCars) #After the fractional part is saved it turns it into the integer part

    FOR (newCarNeeded=0; newCarNeeded<newCars; newCarNeeded+=1): #Loops the number of times a new car is needed
        temp = 1 #Pushes into the while loop
        WHILE temp: #Runs while the entry point is invalid
            temp = 0 #Resets the temporary value so that finding the entry point is valid 
            entryPoint=RANDOMINT(0->(LENGTH(endList)-1)) #Selects an index point for a random entrance to the sim
            FOR car IN carList: #Loops through the current cars to see if they are obstructing new creations              
                IF car.roadObject = endList[entryPoint] AND car.distanceIntoRoadObject > car.carLength: #Checks if car cannot be fit into the entry point
                    temp = 1 #Makes sure you cannot escape the loop before you find a safe spot

        IF NOT temp: #If the entry point is clear 
            exitPoint=RANDOMINT(0->(LENGTH(endList)-1)) #Picks an exit point
            route=findRoute(endList[entryPoint], endList[exitPoint]) #Finds a route from the entry to the exit point

            newCar=Car(endList[entryPoint], route)
            endList[entryPoint].carList.APPEND(newCar.id)
            carList.APPEND(newCar)
    
    newCarList = carList
    FOR car IN carList:
        newCarList = car.tick(timePassed, newCarList)
    carList = newCarList

#math.modf(x)
#Return the fractional and integer parts of x. Both results carry the sign of x and are floats.
