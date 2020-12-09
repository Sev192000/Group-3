import pygame, random, sys
import math
from pygame.locals import *


WINDOWWIDTH = 600 #largeur fenêtre de jeu
WINDOWHEIGHT = 600 #longeur fenêtre
TEXTCOLOR = (0,0,0) #couleur du texte
BACKGROUNDCOLOR = (200, 255, 255) #couleur du fond
FPS = 60 #images par seconde

BADDIEMINSIZE = 30 #taille min des méchants
BADDIEMAXSIZE = 40 #taille max des méchants
BADDIEMINSPEED = 1 #vitesse min des méchants
BADDIEMAXSPEED = 8 #vitesse max des méchants
ADDNEWBADDIERATE = 100 #taux/vitesse ajout des méchants
PLAYERMOVERATE = 5 #taux/vitesse déplacement joueur

GOODIEMINSIZE = 30
GOODIEMAXSIZE = 40
GOODIEMINSPEED = 1
GOODIEMAXSPEED = 8
ADDNEWGOODIERATE = 20

MUSHSIZE = 40
MUSHSPEED = 3
ADDNEWMUSHRATE = 100

def terminate(): #fin du jeu
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def playerHasHitGoodie(playerRect, goodies):
    for g in goodies:
        if playerRect.colliderect(g['rect']):
            return True
    return False

def playerHasHitMush(playerRect, mushs):
    for m in mushs:
        if playerRect.colliderect(m['rect']):
            return True
    return False

def drawText(text, font,surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class Enemy(object):
    def __init__(self,x,y):  # initial position
        self.x = x
        self.y = y
    def move(self, speed=5): # chase movement
        # Movement along x direction
        if self.x > px:
            self.x -= speed
        elif self.x < px:
            self.x += speed
        # Movement along y direction
        if self.y < py:
            self.y += speed
        elif self.y > py:
            self.y -= speed

class Enemy(object):
    def move_towards_player(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

# Set up pygame, the window, and the mouse cursor.
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

# Set up the fonts.
font = pygame.font.SysFont('Berlin Sans FB', 37)

# Set up sounds.
gameOverSound = pygame.mixer.Sound('ExplosionSound.wav')
pygame.mixer.music.load('VolDuBourdon.wav')

# Set up images.
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
GoodiesImageList = (chocolate,flour,milk,egg,cherry)
EndSmallCake = pygame.image.load('EndSmallCake.png')
EndMediumCake = pygame.image.load('EndMediumCake.png')
EndBigCake = pygame.image.load('EndBigCake.png')
Instructions = pygame.image.load('Instructions.png')
broccoli = pygame.image.load('broccoli.png')

# Show instructions
windowSurface.fill(BACKGROUNDCOLOR)
windowSurface.blit(Instructions, (-15,0)) # faut voir l'emplacement
pygame.display.update()
waitForPlayerToPressKey()

# Show the "Start" screen.
windowSurface.fill(BACKGROUNDCOLOR)
windowSurface.blit(HomeImage, (0,0)) # faut voir l'emplacement
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0
while True:
    # Set up the start of the game.
    baddies = []
    goodies = []
    mushs =[]
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    GoodieAddcounter = 0
    MushAddcounter = 0
    pygame.mixer.music.play(-1, 0.0)

    timer = 0
    while True: # The game loop runs while the game part is playing.
        timer = timer - 1
        if timer < 0 :
            slowCheat = False

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverseCheat = True
                if event.key == K_x:
                    slowCheat = True
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True
                if event.key == K_m:
                    pygame.mixer.music.pause() #couper la musique
                if event.key == K_n:
                    pygame.mixer.music.unpause() #remettre la musique

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    score = 0
                if event.key == K_x:
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False


        # Add new baddies and goodies at the top of the screen, if needed.
        if not reverseCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                        }

            baddies.append(newBaddie)

        if not reverseCheat:
            GoodieAddcounter += 1
        if GoodieAddcounter == ADDNEWGOODIERATE:
            GoodieAddcounter = 0
            goodieSize = random.randint(GOODIEMINSIZE, GOODIEMAXSIZE)
            goodieImage = GoodiesImageList[random.randint(0, len(GoodiesImageList) - 1)]
            newGoodie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - goodieSize), 0 - goodieSize, goodieSize, goodieSize),
                        'speed': random.randint(GOODIEMINSPEED, GOODIEMAXSPEED),
                        'surface':pygame.transform.scale(goodieImage, (goodieSize, goodieSize)),
                         }
            goodies.append(newGoodie)


        if not reverseCheat and not slowCheat:
            MushAddcounter += 1
        if MushAddcounter == ADDNEWMUSHRATE:
            MushAddcounter = 0
            mushSize = MUSHSIZE
            newMush = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - mushSize), 0 - mushSize, mushSize, mushSize),
                        'speed': MUSHSPEED,
                        'surface':pygame.transform.scale(mushroom, (mushSize, mushSize)),
                         }

            mushs.append(newMush)

        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        # Move the baddies down.
        for b in baddies:
            if not reverseCheat and not slowCheat:
                move_towards_player
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        # Move the goodies down.
        for g in goodies:
            if not reverseCheat and not slowCheat:
                g['rect'].move_ip(0, g['speed'])
            elif reverseCheat:
                g['rect'].move_ip(0, -5)
            elif slowCheat:
                g['rect'].move_ip(0, 1)

        # Move the mush down.
        for m in mushs:
            if not reverseCheat and not slowCheat:
                m['rect'].move_ip(0, m['speed'])
            elif reverseCheat:
                m['rect'].move_ip(0, -5)
            elif slowCheat:
                m['rect'].move_ip(0, 1)


        # Delete baddies that have fallen past the bottom.
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)

        # Delete goodies that have fallen past the bottom.
        for g in goodies[:]:
            if g['rect'].top > WINDOWHEIGHT:
                goodies.remove(g)

        # Delete mushs that have fallen past the bottom.
        for m in mushs[:]:
            if m['rect'].top > WINDOWHEIGHT:
                mushs.remove(m)

        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)

        # Draw the player's rectangle.
        windowSurface.blit(playerImage, playerRect)

        # Draw each baddie.
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Draw each goodie.
        for g in goodies:
            windowSurface.blit(g['surface'], g['rect'])

        pygame.display.update()

        # Draw each mush.
        for m in mushs:
            windowSurface.blit(m['surface'], m['rect'])

        pygame.display.update()

        # Check if any of the baddies have hit the player.
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score # set new top score
            break

        mainClock.tick(FPS)

        # Check if any of the goodies have hit the player.
        if playerHasHitGoodie(playerRect, goodies):
            score = score + 1
            if score >= topScore:
                topScore = score # set new top score

        for g in goodies:
            if playerRect.colliderect(g['rect']):
                goodies.remove(g)

        mainClock.tick(FPS)

        # Check if any of the Mushs have hit the player.

        if playerHasHitMush(playerRect, mushs):
            timer = 100
            slowCheat = True


            #pygame.time.set_timer(slowCheat = True, 5000) # 5 sec
            #why isn't it working ?



        for m in mushs:
            if playerRect.colliderect(m['rect']):
                mushs.remove(m)

        mainClock.tick(FPS)


    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()


    if score <= 5:
        windowSurface.blit(EndSmallCake, (-32, 0))
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
    if score > 5:
        if score < 10:
            windowSurface.blit(EndMediumCake, (-32, 0))
    if score >= 10:
        windowSurface.blit(EndBigCake, (-52.5, 0))
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()

