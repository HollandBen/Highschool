import pygame
import sys
#custom object for copys of walls
class movable(pygame.sprite.Sprite):
    def __init__(self,start_x,start_y,width,height,speed,load_path): #delete wallColor/ since its an image #add speed variable
        super().__init__() 
        img_load = pygame.image.load(load_path) 
        self.image = pygame.transform.scale(img_load , (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(start_x,start_y))
        self.speed = speed #set the speed
    
    def draw(self,window):
        window.blit(self.image,(self.rect.x, self.rect.y))
    def move_back(self):
          #x-location + x-speed = new x-location
        self.rect.x -= self.movex # make these act on self

        #y-location + y-speed = new y-location
        self.rect.y -= self.movey
    def move(self):
            #value name---pygame check if keys down---->Create a variable that is set to all the key values
        key_input = pygame.key.get_pressed()

        
        #var--------value name-----key Left---speed value--value name------key Right---speed value      
        self.movex = (key_input[pygame.K_a] * -self.speed) + (key_input[pygame.K_d] * self.speed) #speed -> self.speed
        self.movey = (key_input[pygame.K_w] * -self.speed) + (key_input[pygame.K_s] * self.speed)

        #x-location + x-speed = new x-location
        self.rect.x += self.movex # make these act on self

        #y-location + y-speed = new y-location
        self.rect.y += self.movey