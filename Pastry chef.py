# Pygame template - skeleton for a new pygame project
import pygame
import random
import math #needed for the ai

WIDTH = 600 # size of the screen
HEIGHT = 600
FPS = 60 # speed of the game

# define colors
BACKGROUNDCOLOR = (200, 255, 255) # light blue
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
EndSmallCake = pygame.image.load('EndSmallCake.png')
EndMediumCake = pygame.image.load('EndMediumCake.png')
EndBigCake = pygame.image.load('EndBigCake.png')
Instructions = pygame.image.load('Instructions.png')
GoodiesImageList = [chocolate,flour,milk,egg]
Winning = pygame.image.load('winning.png')

# menu screen
def show_go_screen(): #sets the first screen of the game with the instructions
    screen.blit(Instructions, (-15,0))
    pygame.display.flip()
    waiting = True
    while waiting: # waits for the player to press a key to start or quit
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT: # Pressing ESC quits.
                    pygame.quit()
                return

# gameover screen
def show_end_screen(): # sets the different ends possible and the different images
    if score <= 5: # end with a bad score
        screen.fill(BACKGROUNDCOLOR) # clears screen
        draw_text(screen, 'Score: %s' % (str(score)), 18, 20, 10) # draws the score
        screen.blit(EndSmallCake, (-32, 0))
    if score > 5:
        if score < 7:
            screen.fill(BACKGROUNDCOLOR)
            draw_text(screen, 'Score: %s' % (str(score)), 18, 20, 10)
            screen.blit(EndMediumCake, (-32, 0))
    if score >7:
        if score < 10:
            screen.fill(BACKGROUNDCOLOR)
            draw_text(screen, 'Score: %s' % (str(score)), 18, 20, 10)
            screen.blit(EndBigCake, (-52.5, 0))
    if score >49 : # end screen when you won the game
        screen.fill(BACKGROUNDCOLOR)
        draw_text(screen, 'Score: %s' % (str(score)), 18, 20, 10)
        screen.blit(Winning, (-32, 0))

    pygame.display.flip() # changes the screen
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
def draw_text(surf, text, size, x, y): # useful to write some text
    font = pygame.font.Font(font_name,size) # police
    text_surface=font.render(text,True,BLACK)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x,y)
    surf.blit(text_surface, text_rect)

#new class player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImage
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH / 2, HEIGHT - 50)
        self.speedx = 0 # speed of the player
        Player.rect = self.rect

    def update(self): #function definition
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

#new class Baddies
class Baddie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = baddieImage #image definition
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width) #spawning is random
        self.rect.y = random.randrange(-100, -40)  #random so they don't go to the same place
        self.speedy = random.randrange(1,8) #baddies' speed
        self.speedx = random.randrange(-3,3) # diagonal movement

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy #move up to down
        # respawn the baddie when it goes offscreen.
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# new class Goodies
class Goodie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.GoodiesImageList = [chocolate,flour,milk,egg,cherry] #add images
        self.image = random.choice(self.GoodiesImageList)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width) #spawning is random
        self.rect.y = random.randrange(-100, -40)  #random so they don't go to the same place
        self.speedy = random.randrange(1,8) #goodies' speed

    def update(self):
        self.rect.y += self.speedy #move up to down
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
        self.image = mushroom #image definition
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width) #spawning is random
        self.rect.y = random.randrange(-100, -40)  #random so they don't go to the same place
        self.speedy = random.randrange(1, 8)  #mushrooms' speed
        self.speedx = random.randrange(-8, -1) #mushrooms' movement
        Mush.rect = self.rect

    def update(self):
        dx, dy = Player.rect.x - Mush.rect.x, Player.rect.y - Mush.rect.y  #Find direction vector (dx, dy) between enemy and player.
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        Mush.rect.x += dx * self.speedx
        Mush.rect.y += dy * self.speedy
        # respawn the mushroom when it goes offscreen.
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.image = mushroom

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #screen size
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# set up sounds
background_music = pygame.mixer.music.load('VolDuBourdon.wav')
explosion_sound = pygame.mixer.Sound('ExplosionSound.wav')

game_over = True
running = True

show_go_screen() # show instructions

while running: # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit game if press esc key
            running = False

    if game_over: # defining game over
        game_over = False
        pygame.mixer.music.play(loops=-1) # music loop
        all_sprites = pygame.sprite.Group() # creating group with all sprites
        baddies = pygame.sprite.Group()  # group of the bombs
        goodies = pygame.sprite.Group()  # group of the food
        mushs = pygame.sprite.Group() # group of the mushrooms
        player = Player()
        all_sprites.add(player)
        for i in range(5):  # baddies updated automatically
            b = Baddie()
            all_sprites.add(b) # adding baddies to all sprites group
            baddies.add(b)
        for n in range(5):
            g = Goodie()
            all_sprites.add(g)
            goodies.add(g)
        for j in range(1):
            m = Mush()
            all_sprites.add(m)
            mushs.add(m)

        score = 0 # defining beginning score

    # keep loop running at the right speed
    clock.tick(FPS)

    # Update
    all_sprites.update() # updating all sprites

    # Pressing ESC quits.
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
        running = False

    # Sounds pause and play
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                pygame.mixer.music.pause()  # couper la musique
            if event.key == pygame.K_n:
                pygame.mixer.music.unpause()  # remettre la musique

    # Check if Player has hit Baddie (bomb)
    hits_Baddie = pygame.sprite.spritecollide(player,baddies,False)
    if hits_Baddie:
        pygame.mixer.music.stop() # stop music
        explosion_sound.play() # start game over sound
        show_end_screen() # show game over screen
        game_over = True # start loop "if game over"

    # Check if Player has hit Goodie (food)
    hits_Goodie = pygame.sprite.spritecollide(player, goodies, True)
    if hits_Goodie:
        g = Goodie()
        all_sprites.add(g)
        goodies.add(g)
        score = score + 1 # updating score
        if score > 49: # player wins if its score is > 50
            pygame.mixer.music.stop() # stopping music
            game_over = True # start loop "if game over"
            show_end_screen() # show winning screen

    # Check if Player has hit Mushroom
    hits_Mush = pygame.sprite.spritecollide(player, mushs, True)
    if hits_Mush:
        m = Mush()
        all_sprites.add(m)
        mushs.add(m)
        score = score + 10
        if score > 49: # player wins
            pygame.mixer.music.stop()
            show_end_screen()
            game_over = True

    # Draw / render
    screen.fill(BACKGROUNDCOLOR)
    all_sprites.draw(screen)
    draw_text(screen, 'Score: %s' % (str(score)), 18, 20, 10) # draw score on screem

    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit() # end game