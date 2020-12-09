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
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.image = playerImage
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH / 2, HEIGHT - 50)
        self.speedx = 0
# movement
    def update(self):
        self.rect.x += self.speedx


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
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
##