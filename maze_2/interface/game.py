#Name: Ben Holland
#Date: 16 April 2024
#Basic PyGame Setup Code
import pygame,sys,objects.movable,objects.images


def output(WINDOW_WIDTH, WINDOW_HEIGHT, fpsClock, fps, window):
    #Setup of Starting objects
    bg = objects.images.still(0,0,WINDOW_WIDTH,WINDOW_HEIGHT,'maze_2/images/pixilart-drawing.png')
    player = objects.movable.movable(90,50,45,30,1.25,'maze_2/images/bumble.jpg')      #feeding in custom object

    def display():
        window.fill((255,255,255))
        bg.draw(window)
        player.draw(window) #new places character

    while True:
        player.move()
        display()
        if pygame.sprite.collide_mask(player, bg):
            player.move_back()
            display()
             
        for event in pygame.event.get():
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw