#Name: Ben Holland
#Date: 16 April 2024
#Basic PyGame Setup Code
import pygame,sys,objects.movable,objects.images


pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

#Setup of Starting objects
goal_img = pygame.image.load('maze/images/flower.jpg')
goal_img = pygame.transform.scale(goal_img, (50, 32))
goal_font = pygame.font.SysFont('Comic sans', 60)
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
bg = objects.images.still(0,0,WINDOW_WIDTH,WINDOW_HEIGHT,'maze_2/images/background.png')
player = objects.movable.movable(25,25,45,30,1.25,'maze_2/images/bumble.jpg')      #feeding in custom object

pygame.display.set_caption("Bumblebee maze 1.0")
def display():
    global goals
    goals=[]
    bg.draw(window)
    player.draw(window) #new places character
    goals.append(window.blit(goal_img, (285, 465)))
   
def gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT):
        spacer = 20
        font = pygame.font.SysFont('Consolas', 10)
        for gridX in range(0, WINDOW_WIDTH, spacer):        
            window.blit(pygame.transform.rotate(font.render(str(gridX), True, (0, 0, 0)),90),(gridX,0))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            window.blit(font.render(str(gridY), True, (0, 0, 0)), (0, gridY))
        for gridX in range(0, WINDOW_WIDTH, spacer):
            pygame.draw.line(window,(255,0,0),(gridX,0),(gridX,WINDOW_HEIGHT))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            pygame.draw.line(window,(255,0,0),(0,gridY),(WINDOW_WIDTH,gridY))     
def collision(object1, object2):
    return object1.colliderect(object2)

def win():
    global speed
    speed = 0
    window.blit(goal_font.render("You win!", True, (92, 5, 2)), (200, 355))

while True:
    player.move()
    #circ_1_move += 2
    #if circ_1_move > WINDOW_WIDTH:
    #  circ_1_move = 0
    
    #value name---pygame check if keys down---->Create a variable that is set to all the key values
    #key_input = pygame.key.get_pressed()

    
    #var--------value name-----key Left---speed value--value name------key Right---speed value      
    #movex = (key_input[pygame.K_a] * -speed) + (key_input[pygame.K_d] * speed)
    #movey = (key_input[pygame.K_w] * -speed) + (key_input[pygame.K_s] * speed)

    #x-location + x-speed = new x-location
    #player_x += movex

    #y-location + y-speed = new y-location
    #player_y += movey
    
    display()
    #for wall in walls:
    #  if collision(player_char,wall):
    #    player_x -= movex
    #    player_y -= movey
    #    display()
    #for goal in goals:
    #    if collision(player_char,goal):
    #        win()

    for event in pygame.event.get():
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw