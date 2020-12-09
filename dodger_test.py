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

# nos images

playerImage = pygame.image.load('bol.png')

# player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImage
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH / 2, HEIGHT - 50)
# movement
    def update(self):
        self.rect.x += 5


    if moveLeft and playerRect.left > 0:
        self.rect.move_ip(-1 * PLAYERMOVERATE, 0)
    if moveRight and playerRect.right < WINDOWWIDTH:
        self.rect.move_ip(PLAYERMOVERATE, 0)
    if moveUp and playerRect.top > 0:
        self.rect.move_ip(0, -1 * PLAYERMOVERATE)
    if moveDown and playerRect.bottom < WINDOWHEIGHT:
        self.rect.move_ip(0, PLAYERMOVERATE)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()