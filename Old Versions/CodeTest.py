import pygame

pygame.display.init()
WIDTH=1200
HEIGHT=800

win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill(pygame.Color("#EAEAEA"))

pygame.display.flip()

while True:
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                