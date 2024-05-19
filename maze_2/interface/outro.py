import pygame, sys, objects.movable, objects.images, objects.buttons

def output(WINDOW_WIDTH, WINDOW_HEIGHT, fpsClock, fps, window):
    global done
    font = pygame.font.SysFont('Consolas', 30)
    done = False
    def restart():
        global done
        done = True
    btn_restart = objects.buttons.with_background(100, 400, 300, 40, 'Comic Sans', 25, (0, 0, 0), (255, 255, 255), (255, 255, 0), (0, 0, 0), 'press to restart', restart)
    
    while not done:
        #now make the basic window
        window.fill((255, 255, 255)) #bg colour
        window.blit(font.render("Thanks for playing :)", True, (0,0,0)), (100,250)) #text on screen
        btn_restart.draw(window) #puts the button on the screen
        
        #copy paste below and change the button name
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            btn_restart.update(pos, event)
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw