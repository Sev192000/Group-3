# Pygame template - skeleton for a new pygame project
import pygame
import random
import math

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
GoodiesImageList = [chocolate,flour,milk,egg]
Winning = pygame.image.load('winning.png')

# menu screen
def show_go_screen():
    screen.blit(Instructions, (-15,0))
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT: # Pressing ESC quits.
                    pygame.quit()
                return
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# gameover screen
def show_end_screen():
    if score <= 5:
        screen.blit(EndSmallCake, (-32, 0))
    if score > 5:
        if score < 7:
            screen.blit(EndMediumCake, (-32, 0))
    if score >7:
        if score < 10:
            screen.blit(EndBigCake, (-52.5, 0))
    if score >10 :
        screen.fill(BACKGROUNDCOLOR)
        draw_text(screen, 'Score: %s' % (str(score)), 18, 20, 10)
        screen.blit(Winning, (-32, 0))

    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT: # Pressing ESC quits.
                    pygame.quit()
                return

# texte
font_name = pygame.font.match_font('Berlin Sans FB')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,BLACK)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x,y)
    surf.blit(text_surface, text_rect)

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
        self.GoodiesImageList = [chocolate,flour,milk,egg,cherry]
        self.image = random.choice(self.GoodiesImageList)
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
            self.image = random.choice(self.GoodiesImageList)

# new class Mushrooms
class Mush (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mushroom
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
            self.image = mushroom

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# set up sounds
background_music = pygame.mixer.music.load('VolDuBourdon.wav')
explosion_sound = pygame.mixer.Sound('ExplosionSound.wav')

# Game loop
game_over = True
running = True

show_go_screen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_over:
        game_over = False
        pygame.mixer.music.play(loops=-1)
        all_sprites = pygame.sprite.Group()
        baddies = pygame.sprite.Group()  # groupe des méchants
        goodies = pygame.sprite.Group()  # groupe des goodies
        mushs = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(5):  # baddies updated automatiquement. maintenant dans all sprites on a le player et les baddies
            b = Baddie()
            all_sprites.add(b)
            baddies.add(b)
        for n in range(5):
            g = Goodie()
            all_sprites.add(g)
            goodies.add(g)
        for j in range(1):
            m = Mush()
            all_sprites.add(m)
            mushs.add(m)

        score = 0

    # keep loop running at the right speed
    clock.tick(FPS)

    # Update
    all_sprites.update()

    # Pressing ESC quits.
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
        running = False

    # mettre la  musique en pause
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                pygame.mixer.music.pause()  # couper la musique
            if event.key == pygame.K_n:
                pygame.mixer.music.unpause()  # remettre la musique

    # Check if Player has hit Baddie
    hits_Baddie = pygame.sprite.spritecollide(player,baddies,False)
    if hits_Baddie:
        pygame.mixer.music.stop()
        explosion_sound.play()
        show_end_screen()
        game_over = True


    # Check if Player has hit Goodie
    hits_Goodie = pygame.sprite.spritecollide(player, goodies, True)
    if hits_Goodie:
        g = Goodie()
        all_sprites.add(g)
        goodies.add(g)
        score = score + 1
        if score > 10:
            pygame.mixer.music.stop()
            game_over = True
            show_end_screen()


    # Check if Player has hit Mush
    hits_Mush = pygame.sprite.spritecollide(player, mushs, True)
    if hits_Mush:
        m = Mush()
        all_sprites.add(m)
        mushs.add(m)
        score = score + 10
        if score > 10:
            pygame.mixer.music.stop()
            show_end_screen()
            game_over = True



    # Draw / render
    screen.fill(BACKGROUNDCOLOR)
    all_sprites.draw(screen)
    draw_text(screen, 'Score: %s' % (str(score)), 18, 20, 10)


    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()