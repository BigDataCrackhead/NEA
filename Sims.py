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

roadList, time, groupList=p.unpack(1)

if not time:
	time=1

def findRoute(entry, ext, itemList):
	finalRoute=[] 
	tempRoute=[]
	tempRoute.append(entry) 
	for obj in itemList
	while tempRoute[-1] != ext:
		tempConns=finalRoute[-1].getConns() 
		chosenConn=random.randint(0, (len(tempConns)-1))
		if tempConns[chosenConn] != finalRoute[-1]:
			chosenConn=tempConns[chosenConn] 
			finalRoute.append(chosenConn) 
	return finalRoute 

def setEnds(obj, listy):
	geometry=obj.getGeometry()
	print(geometry)
	for direction in geometry: 
		if obj.hasNoConnections(direction, listy): 
			obj.end.append(direction)

for obj in roadList: 
    if len(obj.conns) < 2 and (obj.typ == "TL" or obj.typ == "RD" or obj.typ == "TN"): 
        endList.append(obj) 
        setEnds(obj, roadList) 

    elif len(obj.conns) < 3 and (obj.typ == "TJ"): 
        endList.append(obj) 
        setEnds(obj, roadList) 
    
    elif len(obj.conns) < 4 and (obj.typ == "4J"): 
        endList.append(obj) 
        setEnds(obj, roadList)

def GUI(win, clock, bigListy, timePassed, groupList, frameRate, simulationLength, rate, endList):
	pygame.display.set_caption('GUI Simulation')
	totalTimePassed=0
	tempFraction=0
	carList=[]

	while simulationLength>totalTimePassed:
		clock.tick(frameRate)
		x, y = pygame.mouse.get_pos()

		newCars=(rate*time)+tempFraction
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
				route=findRoute(endList[entryPoint], endList[exitPoint], bigListy) 

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


GUI(w, c, roadList, float(time/FRAMERATE), groupList, FRAMERATE, SIMLENGTH, RATEOFCARS, endList)