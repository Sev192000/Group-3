# Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 600
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BACKGROUNDCOLOR = (200, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)

# nos images

playerImage = pygame.image.load('bol.png')
baddieImage = pygame.image.load('Bombe.png')

# player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImage
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH / 2, HEIGHT - 50)
        self.speedx = 0 # speed of the player

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed() #movements when pressing keys
        if keystate[pygame.K_LEFT]:
            self.speedx = -8 # negative is moving left
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8 # positive is moving right
        self.rect.x += self.speedx

        if self.rect.right > WIDTH: #setting the edges of the screen
            self.rect.right = WIDTH
        if self.rect.left < 0: # left edge
            self.rect.left = 0

#nouvelle classe baddies

class Baddie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = baddieImage
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width) #le spawn est aléatoire
        self.rect.y = random.randrange(-100, -40)  #random pour pas quils arrivent tous au meme endroit
        self.speedy = random.randrange(1,8) #vitesse des baddies

        if self.rect.top > HEIGHT + 10 : #disparaitre quand ils arrivent en bas. quand un disparait un réaparait randomly
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


    def update(self):
        self.rect.y += self.speedy #faire bouger de haut en bas



# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
baddies = pygame.sprite.Group() # groupe des méchants
player = Player()
all_sprites.add(player)
for i in range(8): # baddies updated automatiquement. maintenant dans all sprites on a le player et les baddies
    b = Baddie()
    all_sprites.add(b)
    baddies.add(b)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BACKGROUNDCOLOR)
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
##