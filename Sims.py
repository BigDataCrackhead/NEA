import pygame
import Draw as d

pygame.display.init()
pygame.font.init()

WIDTH=1200
HEIGHT=800

w = pygame.display.set_mode((WIDTH, HEIGHT))

c=pygame.time.Clock()

def GUI(win, clock):
	pygame.display.set_caption('GUI Simulation')

	while True:
		clock.tick(60)
		x, y = pygame.mouse.get_pos()

		d.drawGUI(win)

		pygame.display.flip()

def MRS(win):
	pass


GUI(w, c)