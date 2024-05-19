import pygame
import sys
#custom object for copys of walls
class movable(pygame.sprite.Sprite):
    def __init__(self,start_x,start_y,width,height,speed,load_path): #delete wallColor/ since its an image #add speed variable
        super().__init__() #import all the basic features from a Sprite
        img_load = pygame.image.load(load_path) #load path here is the image to be loaded, if wallcolour than it would be RGB values
        self.image = pygame.transform.scale(img_load , (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(start_x,start_y))
        self.speed = speed #set the speed
    
    def draw(self,window):
        window.blit(self.image,(self.rect.x, self.rect.y))
    
    #collision here, moves the object back
    def move_back(self):
          #x-location + x-speed = new x-location
        self.rect.x -= self.movex # make these act on self

        #y-location + y-speed = new y-location
        self.rect.y -= self.movey
    
    #standard movement stuff
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