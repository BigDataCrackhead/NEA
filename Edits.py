import pygame, sys
import Draw as d
import Click as c
import listenToHarry as classy

""" def onTop(obj, listy):
	objCoords=obj.getXY
	for item in listy:
		itemCoords=item.getXY()
		print(itemCoords, objCoords)
		if itemCoords==objCoords:
			return True
	return False """
	
def checkForSchnap(e1, e2):
	const=10
	
	if type(e1[0])==int:
		if type(e2[0])==int:
			if e1[0]>(e2[0]-const) and e1[0]<(e2[0]+const):
				midOne=(e1[1][0]+e1[1][1])/2
				midTwo=(e2[1][0]+e2[1][1])/2
				if midOne>(midTwo-const) and midOne<(midTwo+const):
					return True
		return False
	else:
		if type(e2[0])==tuple:
			if e1[1]>(e2[1]-const) and e1[1]<(e2[1]+const):
				midOne=(e1[0][0]+e1[0][1])/2
				midTwo=(e2[0][0]+e2[0][1])/2

				if midOne>(midTwo-const) and midOne<(midTwo+const):
					return True
		return False

def snap(w, itemList, obj):
	typ=obj.typ
	
	if not (typ=="ET" or typ=="TM" or typ=="RO"):
		for tempObj in itemList:
			if tempObj!=obj:
				for edge in obj.getGeometry():
					for tempEdge in tempObj.getGeometry():
						if checkForSchnap(edge, tempEdge):
							obj.snap(tempObj, edge, w)
							tempObj.addConnection(obj.id)

def groupEdit(w, g, l):
	print("Printing Group Passed Into Group Edit", g)
	g=d.groupEdit(w, g, l)
	return g

def createNewGroup(pygameWindow, instancedObj, l):
	groupName=d.groupNameDraw(pygameWindow)

	if not groupName:
		return

	newGroup=classy.Group(groupName)

	group=d.mainGroupElementDraw(newGroup, pygameWindow, l)
	if group:
		group=d.groupMemberEditDraw(pygameWindow, group, l)
		if group:
			g=d.groupEdit(pygameWindow, group, l)
			return g

def edit(w, obj, listy):
	if obj.typ=="RD" or obj.typ=="TN":
		pygame.display.set_caption('Road Menu')
		obj=d.roadMenu(w, obj, listy)

	elif obj.typ=="TL":
		if obj.inGroup():
			group=obj.getGroup()
			obj=groupEdit(w, group, listy)
		else:
			obj=createNewGroup(w, obj, listy)

	elif obj.typ=="4J" or obj.typ=="TJ":
		pygame.display.set_caption('Junction Menu')
		obj=d.junctionMenu(w, obj, listy)

	return obj
	""" pygame.display.set_caption('Edit Menu')

	if obj.typ=="RD" or obj.typ=="TN":
		titleOne="Length"
		titleTwo=["Lane Distrobution One", "Lane Distrobution Two"]

	elif obj.typ=="TL":
		titleOne="Time On"
		titleTwo="Time Off"

	elif obj.typ=="4J" or "TJ":
		while True:
			x, y = pygame.mouse.get_pos()

			d.editJunction(w, x, y, obj.x, obj.y, obj, obj.rot, obj.states, obj.exits)

			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					print("Goodbye!")
					pygame.quit()
					sys.exit()

	valueOne, valueTwo=obj.getSpecial()

	if not valueOne:
		valueOne=500
	if not valueTwo:	
		valueTwo=500

	savedX=obj.x+(obj.width/2)
	savedY=obj.y+(obj.height/2)

	image = pygame.transform.scale(obj.img, (150, 150))

	rotation=obj.rotation

	lastMove=False

	lines=[savedX, savedY, rotation]
	
	if type(valueOne)==int:
		lines.append(valueOne)
	else:
		for i in valueOne:
			lines.append(i)
	if type(valueTwo)==int:
		lines.append(valueTwo)
	else:
		for i in valueTwo:
			lines.append(i)
	
	print(lines)

	while True:

		moveCheck=False

		x, y = pygame.mouse.get_pos()

		tempList=d.drawEdit(w, x, y, lines[0], lines[1], image, lines[2], valueOne, valueTwo, titleOne, titleTwo)

		if pygame.mouse.get_pressed()[0]:
			if lastMove:
				if x>=350 and x<=850:
					lines[lineID]=x
				elif x<350:
					lines[lineID]=350
				elif x>850:
					lines[lineID]=850
				moveCheck=True
				
			else:
				print(lines, tempList, x, y)

				lineID=0
				dontRepeat=False
				userAssist=8

				for item in tempList:
					
					if c.checkWithin(x, y, item[0]-userAssist, item[1]-userAssist, userAssist*2, userAssist*2) and dontRepeat==False:
						print("Click")

						lines[lineID]=x

						moveCheck=True
						dontRepeat=True

					if not dontRepeat:
						lineID+=1

				if c.checkWithin(x, y, 0, 10, 160, 20) and dontRepeat==False:
					break
				
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				print("Goodbye!")
				pygame.quit()
				sys.exit()

		lastMove=moveCheck """

def time(w, time):
	if not time:
		time=500

	pygame.display.set_caption('Time Menu')

	lastMove=False

	while True:
		if type(time)==list:
			time=time[0]
		moveCheck=False

		x, y = pygame.mouse.get_pos()

		if pygame.mouse.get_pressed()[0]:
			if lastMove:
				if x>=350 and x<=850:
					time=x
				elif x<350:
					time=350
				elif x>850:
					time=850

				moveCheck=True
			else:
				
				if x>time-8 and x<time+8:
					if y>492 and y<508:
						time=x
						moveCheck=True
				if c.checkWithin(x, y, 0, 10, 160, 20):
					#return time conversion here
					return time
				elif c.checkWithin(x, y, 560, 580, 80, 40):
					#return time conversion here
					return time

		d.drawTime(w, x, y, time)

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				print("Goodbye!")
				pygame.quit()
				sys.exit()

		lastMove=moveCheck
	
