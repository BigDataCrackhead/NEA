import pygame, random, math
import Draw as d
import Pack as p

pygame.display.init()
pygame.font.init()

WIDTH=1200
HEIGHT=800
FRAMERATE=60
SIMLENGTH=120
BIGCARDATA=[]
RATEOFCARS=1
endList=[]

w = pygame.display.set_mode((WIDTH, HEIGHT))

c=pygame.time.Clock()

itemList, time, groupList=p.unpack(1)

if not time:
	time=1

def findRoute(entry, ext):
	finalRoute=[] 
    finalRoute.append(entry) 
    while finalRoute[-1] != ext:
        tempConns=finalRoute[-1].getConns() 
        chosenConn=random.randint(0, (len(tempConns)-1))
		if tempConns[chosenConn] != finalRoute[-1]:
        	chosenConn=tempConns[chosenConn] 
        	finalRoute.append(chosenConn) 
    return finalRoute 

def setEnds (object):
    for direction in object.getGeometry: 
        in direction==True and object.hasNoConnections(direction): 
            object.end.append(direction)

for object in roadList: 
    in len(object.connections) < 2 and (object.typ == "TL" or object.typ == "RD" or object.typ = "TN"): 
        endList.append(object) 
        setEnds(object) 

    elif len(object.connections) < 3 and (object.typ == "TJ"): 
        endList.append(object) 
        setEnds(object) 
    
    elif len(object.connections) < 4 and (object.typ == "4J"): 
        endList.append(object) 
        setEnds(object)

def GUI(win, clock, bigListy, timePassed, groupList, frameRate, simulationLength, rate, endList):
	pygame.display.set_caption('GUI Simulation')
	totalTimePassed=0
	tempFraction=0
	carList=[]

	while simulationLength>totalTimePassed:
		clock.tick(frameRate)
		x, y = pygame.mouse.get_pos()

		newCars=(rateOfCars*time)+tempFraction
		tempFraction=newCars%1
		newCars=math.trunc(newCars)

		for newCarNeeded in range(newCars):
			temp=1
			while temp:
				temp=0
				entryPoint=random.randint(0, len(endList)-1)
				for car in carList:
					if car.roadObject == endList[entryPoint] and car.distanceIntoRoadObject > car.carLength:
						temp=1

			if not temp: 
				exitPoint=random.randint(0, (len(endList)-1)) 
				route=findRoute(endList[entryPoint], endList[exitPoint]) 

				newCar=Car(endList[entryPoint], route) 
				endList[entryPoint].carList.append(newCar.id) 
				carList.append(newCar)

		newCarList = carList 
		for car in carList: 
			newCarList = car.tick(timePassed, newCarList) 
		carList = newCarList

		d.drawGUI(win, x, y, bigListy)
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				print("Goodbye!")
				pygame.quit()
				sys.exit()

		pygame.display.flip()

def MRS(win):
	pass


GUI(w, c, itemList, float(time/FRAMERATE), groupList, FRAMERATE, SIMLENGTH, RATEOFCARS, endList)