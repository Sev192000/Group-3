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

# nos images

playerImage = pygame.image.load('bol.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('Bombe.png')
chocolate = pygame.image.load('chocolate.png')
cherry = pygame.image.load('cherry.png')
flour = pygame.image.load('flour.png')
milk = pygame.image.load('milk.png')
egg = pygame.image.load('egg.png')
mushroom = pygame.image.load('mushroom.png')
pastryGirl = pygame.image.load('pastrygirl.png')
textbubble = pygame.image.load('textbubble.png')
BigCake = pygame.image.load('GirlBigCake.png')
MediumCake = pygame.image.load('GirlMediumCake.png')
SmallCake = pygame.image.load('GirlSmallCake.png')
HomeImage = pygame.image.load('imagedb.png')
EndSmallCake = pygame.image.load('EndSmallCake.png')
EndMediumCake = pygame.image.load('EndMediumCake.png')
EndBigCake = pygame.image.load('EndBigCake.png')
Instructions = pygame.image.load('Instructions.png')
broccoli = pygame.image.load('broccoli.png')

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
        self.speedx = random.randrange(-3,3) # diagonal movement


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy #faire bouger de haut en bas.
        # respawn the baddie when it goes offscreen.
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# new class Goodies
class Goodie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.GoodiesImageList = (chocolate,flour,milk,egg,cherry)
        self.image = self.GoodiesImageList[random.randint(0, len(self.GoodiesImageList) - 1)]
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width) #le spawn est aléatoire
        self.rect.y = random.randrange(-100, -40)  #random pour pas quils arrivent tous au meme endroit
        self.speedy = random.randrange(1,8) #vitesse des goodies

    def update(self):
        self.rect.y += self.speedy #faire bouger de haut en bas.
        # respawn the goodie when it goes offscreen.
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
baddies = pygame.sprite.Group() # groupe des méchants
goodies = pygame.sprite.Group() # groupe des goodies
player = Player()
all_sprites.add(player)
for i in range(5): # baddies updated automatiquement. maintenant dans all sprites on a le player et les baddies
    b = Baddie()
    all_sprites.add(b)
    baddies.add(b)
for n in range(5):
    g = Goodie()
    all_sprites.add(g)
    goodies.add(g)

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

    # Check if Player has hit Baddie
    hits_Baddie = pygame.sprite.spritecollide(player,baddies,False)
    if hits_Baddie:
        running = False

    # Check if Player has hit Goodie
    hits_Goodie = pygame.sprite.spritecollide(player, goodies, False)

    # Draw / render
    screen.fill(BACKGROUNDCOLOR)
    all_sprites.draw(screen)

    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
##