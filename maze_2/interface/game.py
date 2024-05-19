#Name: Ben Holland
#Date: 16 April 2024
#Basic PyGame Setup Code
import pygame,sys,objects.movable,objects.images


def output(WINDOW_WIDTH, WINDOW_HEIGHT, fpsClock, fps, window):
    #Setup of Starting objects
    bg = objects.images.still(0,0,WINDOW_WIDTH,WINDOW_HEIGHT,'maze_2/images/pixilart-drawing.png') #feeding in background
    player = objects.movable.movable(90,50,45,30,1.25,'maze_2/images/bumble.jpg')      #feeding in custom object as the player character
    goal = objects.images.still(300,50,50,32,'maze_2/images/flower.jpg') #feed in the goal image
    
    def display():
        window.fill((255,255,255)) #whatever colour the background is normally
        bg.draw(window) #places background
        player.draw(window) #new places character
        goal.draw(window)

    while True:
        player.move() #constantly run player movement
        display()
        if pygame.sprite.collide_mask(player, bg): #when the player collides with a background element
            player.move_back()
            display()
        if pygame.sprite.collide_mask(player,goal): 
            break
             
        for event in pygame.event.get():
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw