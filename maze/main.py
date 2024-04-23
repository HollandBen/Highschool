#Name: Ben Holland
#Date: 16 April 2024
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
player_char_img = pygame.transform.scale(player_char_img, (45, 30))  #resize image Where 35 ,35 is the size, (x,y)
goal_img = pygame.image.load('maze/images/flower.jpg')
goal_img = pygame.transform.scale(goal_img, (50, 32))
player_x = 25
player_y = 25
goal_font = pygame.font.SysFont('Comic sans', 60)
#setting a variable named speed to what we want the speed of the object
speed = 1.25
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Bumblebee maze 1.0")
def display():
    global player_char, walls, goals
    walls=[]
    goals=[]
    window.fill((52, 207, 35)) #green background
    #gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    #border walls
    walls.append(pygame.draw.rect(window,(110, 102, 92),(0,0,20,500))) #left wall
    walls.append(pygame.draw.rect(window,(110, 102, 92),(0,0,500,20))) #top wall
    #walls.append(pygame.draw.rect(window,(110, 102, 92),(0,480,500,20))) #bottom wall
    walls.append(pygame.draw.rect(window,(110, 102, 92),(480,0,20,500))) #right wall
    #centre fountain
    walls.append(pygame.draw.circle(window, (108, 107, 112), (250,250), 50)) #outer fountain
    walls.append(pygame.draw.circle(window, (72, 161, 219), (250,250), 43)) #water
    walls.append(pygame.draw.circle(window, (108, 107, 112), (250,250), 16)) #fountain pillar
    #maze walls
    walls.append(pygame.draw.rect(window,(23, 110, 13),(20,60,100,20))) #hedge
    walls.append(pygame.draw.rect(window,(23, 110, 13),(200,20,20,130))) #hedge
    walls.append(pygame.draw.rect(window,(23, 110, 13),(300,140,20,200))) #hedge
    walls.append(pygame.draw.rect(window,(23, 110, 13),(280,70,140,20))) #hedge
    walls.append(pygame.draw.rect(window,(23, 110, 13),(320,140,100,20))) #hedge
    walls.append(pygame.draw.rect(window,(23, 110, 13),(380,220,100,20))) #hedge
    walls.append(pygame.draw.rect(window,(23, 110, 13),(20,425,260,20))) #hedge
    walls.append(pygame.draw.rect(window,(23, 110, 13),(340,425,140,20))) #hedge
    walls.append(pygame.draw.rect(window,(23, 110, 13),(300,340,80,20))) #hedge
    walls.append(pygame.draw.rect(window,(23, 110, 13),(260,445,20,55))) #hedge
    walls.append(pygame.draw.rect(window,(23, 110, 13),(340,445,20,55))) #hedge
    #benches
    walls.append(pygame.draw.rect(window,(105, 80, 37),(80,130,35,150))) #bench
    walls.append(pygame.draw.rect(window,(105, 80, 37),(80,340,150,35))) #bench
    walls.append(pygame.draw.rect(window,(105, 80, 37),(435,260,35,150))) #bench
    #tree stump
    walls.append(pygame.draw.circle(window, (69, 51, 21), (350,310), 30)) #stump bark
    walls.append(pygame.draw.circle(window, (201, 146, 54), (350,310), 25)) #stump inner
    walls.append(pygame.draw.circle(window, (217, 175, 106), (350,310), 9)) #stump core
    
    walls.append(pygame.draw.rect(window,(138, 116, 81),(30,450,220,50))) #dirt
    walls.append(pygame.draw.rect(window,(138, 116, 81),(370,450,100,50))) #dirt
    #player
    player_char=window.blit(player_char_img,(player_x, player_y))
    
    #goal
    goals.append(window.blit(goal_img, (285, 465)))
    #(pygame.draw.rect(window,(255, 255, 255),(305,480,10,10))) #goal
   
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
    for goal in goals:
        if collision(player_char,goal):
            win()

    for event in pygame.event.get():
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw