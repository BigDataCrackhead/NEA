import pygame
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

w = pygame.display.set_mode((WIDTH, HEIGHT))

c=pygame.time.Clock()

itemList, time, groupList=p.unpack(1)

if not time:
	time=1

def GUI(win, clock, bigListy, timePassed, groupList, frameRate, simulationLength, rate):
	pygame.display.set_caption('GUI Simulation')
	totalTimePassed=0
	endList=[]
	tempFraction=0
	carList

	while simulationLength>totalTimePassed:
		clock.tick(frameRate)
		x, y = pygame.mouse.get_pos()

		d.drawGUI(win, x, y, bigListy)
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				print("Goodbye!")
				pygame.quit()
				sys.exit()

		pygame.display.flip()

def MRS(win):
	pass


GUI(w, c, itemList, float(time/FRAMERATE), groupList, FRAMERATE, SIMLENGTH, RATEOFCARS)