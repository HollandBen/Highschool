#Name: Ben Holland
#Date: 16 April 2024
#Basic PyGame Setup Code
import pygame,sys,objects.movable,objects.images, objects.buttons

def output(WINDOW_WIDTH, WINDOW_HEIGHT, fpsClock, fps, window):
    global done
    font = pygame.font.SysFont('Consolas', 30)
    def next():
        global done
        done = True
    btn_next = objects.buttons.no_background(1, 400, "Consolas", 30, (255, 0, 0), (0, 255, 0), "Test", next)
    done = False
    while not done:
        window.fill((255,255,255))
        window.blit(font.render("Welcome to the maze", True, (0, 0, 0)), (100, 250))
        btn_next.draw(window)
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            btn_next.update(pos, event)
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw