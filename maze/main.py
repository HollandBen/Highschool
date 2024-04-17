#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys


pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

#Setup of Starting objects
circ_1_move = 250
player_char_img = pygame.image.load('maze/images/bumble.jpg') #with .png or .jpb included in the name
player_char_img = pygame.transform.scale(player_char_img, (150, 100))  #resize image Where 35 ,35 is the size, (x,y)
player_x = 250
player_y = 400
#setting a variable named speed to what we want the speed of the object
speed = 2
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Test")
def display():
    global player_char, walls
    walls=[]
    window.fill((255,255,255)) #White background
    gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    walls.append(pygame.draw.rect(window,(255,255,0),(0,0,100,100)))
    walls.append(pygame.draw.rect(window,(0,0,0),(20,20,10,30)))
    walls.append(pygame.draw.circle(window, (0,0,255), (circ_1_move,250), 50))
    player_char=window.blit(player_char_img,(player_x, player_y))




   
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


while True:
    circ_1_move += 2
    if circ_1_move > WINDOW_WIDTH:
      circ_1_move = 0
    
    #value name---pygame check if keys down---->Create a variable that is set to all the key values
    key_input = pygame.key.get_pressed()

    
    #var--------value name-----key Left---speed value--value name------key Right---speed value      
    movex = (key_input[pygame.K_a] * -speed) + (key_input[pygame.K_d] * speed)
    movey = (key_input[pygame.K_w] * -speed) + (key_input[pygame.K_s] * speed)

    #x-location + x-speed = new x-location
    player_x += movex

    #y-location + y-speed = new y-location
    player_y += movey
    
    display()
    for wall in walls:
      if collision(player_char,wall):
        player_x -= movex
        player_y -= movey
        display()

    for event in pygame.event.get():
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw