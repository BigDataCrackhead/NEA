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
        IF self.roadObject.typ = "TJ" OR self.roadObject.typ = "4J": #Checks if the road the object is on is a t-junction or a 4 way junction
            tempGroup = self.roadObject.group #Creates a temporary group variable that holds the group of the junction
            FOR (index=0; index<4; index+=1): #Loops through four times
                FOR obj IN tempGroup.direction[index]: #Loops through the objects in the directions of the group
                    IF obj IN self.route: #If one of these objects is in the route runs
                        IF obj = self.route[self.roadIndex-1] OR obj = self.route[self.roadIndex-2]: #If this object is either the previous object the car was on or the object the car was on before that runs
                            comingFrom = index #This means it must have been coming from this direction
                        ELSE:
                            goingTo = index #Otherwise it must be going to this direction
            
            IF (comingFrom+1 = goingTo) OR (comingFrom+1 = 4 AND goingTo = 0): #If the car is turning left
                IF self.velocity > 8: #And the velocity is greater than 8
                    self.acceleration -= self.velocity * -0.5 #Slow down

            ELIF (comingFrom+2 = goingTo) OR (comingFrom+2 = 4 AND goingTo = 0) OR (comingFrom+2 = 5 AND goingTo = 1): #If the car is going straight ahead
                IF self.velocity > 8: #And the velocity is greater than 8
                    self.acceleration -= self.velocity * -0.5 #Slow Down

            ELSE: #Otherwise
                FOR car IN carList: #Loop through the car list
                    IF car.route[car.roadIndex-1] != self.route[roadIndex-1]: #If the car came from anywhere but where you came from
                        IF NOT car.waiting: #If that car is not waiting
                            IF car.route[car.roadIndex+1] = self.route[roadIndex+1]: #If that car has the same destination
                                IF self.velocity != 0: #And the velocity is not 0
                                    self.acceleration = self.velocity * -0.5 #Slow down
                    
                    ELSE: #If the car came from the same direction
                        IF car.waiting: #And the car is waiting
                            IF car.distanceIntoRoadObject > self.distanceIntoRoadObject: #And it is ahead 
                                IF self.velocity != 0: #And you are moving
                                    self.acceleration = self.velocity * -0.5 #Slow down
                            


        IF self.following: #If you are following a car
            IF self.distanceIntoRoadObject > self.following.distanceIntoRoadObject: #Runs if the car is in a new road object
                self.acceleration = (self.following.velocity - self.velocity) * 5 * (1/(self.following.distanceIntoRoadObject+self.roadObject.length - self.distanceIntoRoadObject + self.following.carLength)) #Calculates what the new acceleration of the car should be
            ELSE: #If both cars are on the same road object
                self.acceleration = (self.following.velocity - self.velocity) * 5 * (1/(self.following.distanceIntoRoadObject - self.distanceIntoRoadObject+self.following.carLength)) #Calculates the new acceleration of the car

        ELSE: #If you are not following a car
            FOR car IN carList: #Loops through the cars in the roadObject
                IF car.distanceIntoRoadObject > self.distanceIntoRoadObject+car.carLength+1+(self.velocity*2) AND car.follower = False AND self.roadObject.typ != "TJ" AND self.roadObject.typ != "4J" AND car.route[car.roadIndex-1] = self.route[self.roadIndex-1]: #If the car is suitably close, you are not on a junction, both came from the same road and the car does not have a follower already
                    car.follower=self #Set yourself as the car's follower
                    self.following=car #Set your following to the car
        
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
