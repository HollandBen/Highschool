#Name: Ben Holland
#Date: 16 April 2024
#Basic PyGame Setup Code
import pygame,sys,interface.game, interface.intro, interface.outro
pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Bumblebee maze 2.0")

while True:
    interface.intro.output(WINDOW_WIDTH, WINDOW_HEIGHT, fpsClock, fps, window)
    interface.game.output(WINDOW_WIDTH, WINDOW_HEIGHT, fpsClock, fps, window)
    interface.outro.output(WINDOW_WIDTH,WINDOW_HEIGHT,fpsClock,fps,window)