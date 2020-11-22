import pygame
import Draw as d
import Pack as p

pygame.display.init()
pygame.font.init()

WIDTH=1200
HEIGHT=800
FRAMERATE=60

w = pygame.display.set_mode((WIDTH, HEIGHT))

c=pygame.time.Clock()

itemList, time, groupList=p.unpack(1)

def GUI(win, clock, bigListy, timePassed, groupList, frameRate):
	pygame.display.set_caption('GUI Simulation')
	totalTimePassed=0
	
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


GUI(w, c, itemList, float(time/FRAMERATE), groupList, FRAMERATE)