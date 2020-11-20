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
    METHOD constructor (self, currentRoad, route): #The method run when the class initialises
        self.time=0 #The value to track how long the car has been in the simulation
        self.timeWaiting=0 #The value that tracks how long the car has been waiting
        self.route=route #The route the car will take 
        self.carLength=(RANDOMINT(0->8)*0.1)+1.2 #The assigned length of the car
        self.acceleration=0 #The current acceleration of the car
        self.velocity=currentRoad.speedLimit-3+RANDOMINT(0->6) #The current velocity of the car
        self.targetVelocity=self.velocity #The velocity the car is aiming to acheive
        self.roadObject=currentRoad #The road object that the car currently belongs to
        self.roadIndex=0 #The index of the road object with relation to self.route
        self.distanceIntoRoadObject=0 #The distance into the road object that the car currently is
        self.following=False #Whether or not the car is following another car
        self.follower=False #Whether or not the car has a follower
        self.waiting=False #Whether or not the car is waiting

    METHOD setTargetVelocity(self): #A method to set the target velocity for the car
        self.targetVelocity = currentRoad.speedLimit-3+RANDOMINT(0->5) #Selects a target velocity based on a speed near to the actual speed limit

    METHOD tick (self, time, bigCarList): #The method called every frame to keep cars moving correctly
        carList=self.roadObject.getCars() #Defines the list of cars in the roadObject shared by itself
        IF self.velocity != 0: #If the car is moving makes sure the system does not think it is waiting
            self.waiting = False

        IF self.roadObject.typ != "4J" AND self.roadObject.typ != "TJ": #Checks if itself is any type of object other than t-junction and 4-way junction
            IF self.velocity < self.targetVelocity: #Checks if it is slower than it's target velocity
                self.acceleration = 0.5 #Tells the car to speed up
            ELIF self.velocity > self.targetVelocity: #Checks if it is faster than it's target velocity
                self.acceleration = -0.5 #Tells it to slow down

        geometry=["north", "east", "south", "west"] #Defines basic geometry variables 
        IF self.roadObject,typ = "TJ" OR self.roadObject.typ = "4J": #Checks  
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
                IF car.distanceIntoRoadObject > self.distanceIntoRoadObject+car.carLength+1+(self.velocity*2) AND car.follower = False:
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

        RETURN bigCarList

    METHOD newRoad (self):
        self.roadObject.carList.REMOVE(self)
        self.roadIndex+=1
        self.roadObject=route[roadIndex]
        self.roadObject.carList.APPEND(self)
        self.distanceIntoRoadObject=0
        self.setTargetVelocity()

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
    finalRoute=[] #The empty array that the route will be added to
    finalRoute.APPEND(entry) #The first part of the route will always be the start
    WHILE finalRoute[-1] != exit: #While the last element of the array is not the end point
        tempConns=finalRoute[-1].getConnections() #Find the connections of the last part of the road
        chosenConn=RANDOMINT(0->(LENGTH(tempConns)-1)) #Picks a random index for the temporary connections
        chosenConn=tempConns[chosenConn] #Selects the road associated with the index
        finalRoute.APPEND(chosenConn) #Adds this road to the route
    RETURN finalRoute #Returns the calculated route

PROCEDURE setEnds (object):
    FOR direction IN object.getGeometry: #Loops through north, east, south and west
        IF direction==True AND object.hasNoConnections(direction): #Checks if the direction is possible but unattached
            object.end.APPEND(direction) #Adds this direction to the objects' end list

FOR object IN roadList: #Runs once for every road object in the sim
    IF LENGTH(object.connections) < 2 AND (object.typ = "TL" OR object.typ = "RD" OR object.typ = "TN"): #Runs if the object is either a traffic 
#light or a road and has only one connection 
        endList.APPEND(object) #Adds this object to the list of objects with an end
        setEnds(object) #Makes sure the object knows which directions it has free

    ELIF LENGTH(object.connections) < 3 AND (object.typ = "TJ"): #Runs if the object is a t-junction and has 2 or less connections
        endList.APPEND(object) #Adds this object to the list of objects with an end
        setEnds(object) #Makes sure the object knows which directions it has free
    
    ELIF LENGTH(object.connections) < 4 AND (object.typ = "4J"): #Runs if the object is a 4 way junction and has 3 or less connections
        endList.APPEND(object) #Adds this object to the list of objects with an end
        setEnds(object) #Makes sure the object knows which directions it has free

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

            newCar=Car(endList[entryPoint], route) #Creates a car with the route provided
            endList[entryPoint].carList.APPEND(newCar.id) #Adds this car to the roadObject
            carList.APPEND(newCar) #Adds this car to the total car array
    
    newCarList = carList #A temporary variable is instanced to hold the altered car list
    FOR car IN carList: #Loops through the cars in the sim
        newCarList = car.tick(timePassed, newCarList) #Makes the sim tick one frame forward
    carList = newCarList #Assigns the altered car list to the actual car list
