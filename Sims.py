import pygame, random, math, sys
import Draw as d
import Pack as p
import Variables as v
import listenToHarry as classy

pygame.display.init()
pygame.font.init()

WIDTH=1200
HEIGHT=800
FRAMERATE=30
SIMLENGTH=120
RATEOFCARS=0.25
endList=[]

w = pygame.display.set_mode((WIDTH, HEIGHT))

c=pygame.time.Clock()

roadList, time, groupList=p.unpack(1)

TIME = 5

def findRoute(entry, ext, itemList):
	print(entry.id)
	print(ext.id)
	finalRoute=[]
	unvisitedNodes=itemList
	visitableNodes=[]
	visitedNodes=[]
	currentNode=entry
	howToGetThere={node: [] for node in itemList}
	howToGetThereNumbers={node.id: [] for node in itemList}

	distanceToNode={node: float("inf") for node in itemList}

	distanceToNode[currentNode]=currentNode.length
	howToGetThere[currentNode]=[currentNode]
	howToGetThereNumbers[currentNode.id]=[currentNode.id]

	for irrelevantNumber in itemList:
		print("Current Node: "+str(currentNode.id))
		for connection in currentNode.conns:
			for obj in itemList:
				if obj.id==connection:
					connection=obj
			visitableNodes.append(connection)
			routeLength=distanceToNode[currentNode]+connection.length
			if routeLength<distanceToNode[connection]:
				distanceToNode[connection]=routeLength
				tempList=howToGetThere[currentNode]
				tempList.append(connection)
				howToGetThere[connection]=tempList
				tempList=howToGetThereNumbers[currentNode.id]
				tempList.append(connection.id)
				howToGetThereNumbers[connection.id]=tempList
			print()
			print(howToGetThereNumbers)
			print("========")
		unvisitedNodes.remove(currentNode)
		visitedNodes.append(currentNode)
		currentNode=visitableNodes[0]

	finalRoute=howToGetThere[ext]

	print("==========")
	print(finalRoute)
	print("==========")	
	
		
	

	


	""" finalRoute.append(entry) 
	attempts=0
	print()
	print(entry.id, end="")
	while finalRoute[-1] != ext and attempts<1000:
		attempts+=1
		tempConns=finalRoute[-1].getConns() 
		chosenConn=random.randint(0, (len(tempConns)-1))

		if tempConns[chosenConn] == finalRoute[-2].id:
			finalRoute = [entry]
		else:
			chosenConn=tempConns[chosenConn]
			for obj in itemList:
				if obj.id == chosenConn:
					print(obj.id, end=", ")
					finalRoute.append(obj)
			
	print() """
	return finalRoute 

def setEnds(obj, listy):
	geometry=obj.getGeometry()
	print(geometry)
	for direction in geometry:
		if obj.hasNoConnections(direction, listy): 
			obj.end.append(direction)

for obj in roadList: 
	print()
	print(str(obj.id), end=": ")
	for conn in obj.conns:
		print(str(conn), end=" ")

	if len(obj.conns) < 2 and (obj.typ == "TL" or obj.typ == "RD" or obj.typ == "TN"):
		endList.append(obj)
		setEnds(obj, roadList)

	elif len(obj.conns) < 3 and (obj.typ == "TJ"): 
		endList.append(obj) 
		setEnds(obj, roadList) 

	elif len(obj.conns) < 4 and (obj.typ == "4J"): 
		endList.append(obj) 
		setEnds(obj, roadList)
	print()
	print("Endlist: "+ str(endList))

def GUI(win, clock, bigListy, timePassed, groupList, frameRate, simulationLength, rate, endList):
	pygame.display.set_caption('GUI Simulation')
	totalTimePassed=0
	tempFraction=0
	carList=[]

	while simulationLength>totalTimePassed:
		print(str(totalTimePassed))
		d.drawText(win, str(totalTimePassed), 1000, 200, 25, v.PINK)
		clock.tick(frameRate)
		x, y = pygame.mouse.get_pos()

		newCars=((rate*timePassed)+tempFraction)
		tempFraction=newCars%1
		newCars=math.trunc(newCars)

		for newCarNeeded in range(newCars):
			counter=0
			temp=1
			while temp and counter<11:
				temp=0
				entryPoint=random.randint(0, len(endList)-1)
				for car in carList:
					if car.roadObject == endList[entryPoint] and car.distanceIntoRoadObject > car.carLength:
						temp=1
						counter+=1

			if counter<11:
				exitPoint=0

				while exitPoint==entryPoint:
					exitPoint=random.randint(0, (len(endList)-1))
				route=findRoute(endList[entryPoint], endList[exitPoint], bigListy) 

				newCar=classy.Car(endList[entryPoint], route) 
				endList[entryPoint].carList.append(newCar) 
				carList.append(newCar)

		totalTimePassed+=timePassed
		newCarList = carList 
		for car in carList: 
			newCarList = car.tick(timePassed, newCarList) 
		carList = newCarList

		d.drawGUI(win, x, y, bigListy, carList)
		
		d.drawText(win, str(len(carList)), 700, 50, 20, v.BLUE)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				print("Goodbye!")
				pygame.quit()
				sys.exit()

		pygame.display.flip()

def MRS(win):
	pass

GUI(w, c, roadList, float(TIME/FRAMERATE), groupList, FRAMERATE, SIMLENGTH, RATEOFCARS, endList)