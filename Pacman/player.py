import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)

class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    explosion = False
    game_over = False
    def __init__(self,x,y,filename):
        # Call the parent class (sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        # Load image which will be for the animation
        img = pygame.image.load("walk.png").convert()
        # Create the animations objects
        self.move_right_animation = Animation(img,32,32)
        self.move_left_animation = Animation(pygame.transform.flip(img,True,False),32,32)
        self.move_up_animation = Animation(pygame.transform.rotate(img,90),32,32)
        self.move_down_animation = Animation(pygame.transform.rotate(img,270),32,32)
        # Load explosion image
        img = pygame.image.load("explosion.png").convert()
        self.explosion_animation = Animation(img,30,30)
        # Save the player image
        self.player_image = pygame.image.load(filename).convert()
        self.player_image.set_colorkey(BLACK)

