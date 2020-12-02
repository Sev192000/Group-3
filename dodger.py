import pygame, random, sys
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
ADDNEWGOODIERATE = 100

MUSHMINSIZE = 40
MUSHMAXSIZE = 40
MUSHMINSPEED = 1
MUSHMAXSPEED = 3
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

def playerHasHitMush(playerRect, mush):
    for m in mush:
        if playerRect.colliderect(m['rect']):
            return True
    return False

def drawText(text, font,surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Set up pygame, the window, and the mouse cursor.
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

# Set up the fonts.
font = pygame.font.SysFont('Bradley Hand ITC', 37)

# Set up sounds.
gameOverSound = pygame.mixer.Sound('ExplosionSound.wav')
pygame.mixer.music.load('VolDuBourdon.wav')

# Set up images.
playerImage = pygame.image.load('bol.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('Bombe.png')
goodieImage = pygame.image.load('chocolate.png')
cherry = pygame.image.load('cherry.png')
flour = pygame.image.load('flour.png')
milk = pygame.image.load('milk.png')
egg = pygame.image.load('egg.png')
mushroom = pygame.image.load('mushroom.png')
pastryGirl = pygame.image.load('pastrygirl.png')
textbubble = pygame.image.load('textbubble.png')
BigCake = pygame.image.load('BigCake.png')
MediumCake = pygame.image.load('GirlMediumCake.png')
SmallCake = pygame.image.load('SmallCake.png')
himage = pygame.image.load('imagedb.png')
GoodiesImageList = (goodieImage,flour,milk,egg,cherry)

# Show the "Start" screen.
windowSurface.fill(BACKGROUNDCOLOR)
windowSurface.blit(himage, (0,0)) # faut voir l'emplacement
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0
while True:
    # Set up the start of the game.
    baddies = []
    goodies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    GoodieAddcounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # The game loop runs while the game part is playing.

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
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                        }

            baddies.append(newBaddie)

        if not reverseCheat and not slowCheat:
            GoodieAddcounter += 1
        if GoodieAddcounter == ADDNEWGOODIERATE:
            GoodieAddcounter = 0
            goodieSize = random.randint(GOODIEMINSIZE, GOODIEMAXSIZE)
            newGoodie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - goodieSize), 0 - goodieSize, goodieSize, goodieSize),
                        'speed': random.randint(GOODIEMINSPEED, GOODIEMAXSPEED),
                        'surface':pygame.transform.scale(goodieImage, (goodieSize, goodieSize)),
                         }

            goodies.append(newGoodie)

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
                b['rect'].move_ip(0, b['speed'])
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

        # Delete baddies that have fallen past the bottom.
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)

        # Delete goodies that have fallen past the bottom.
        for g in goodies[:]:
            if g['rect'].top > WINDOWHEIGHT:
                goodies.remove(g)

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

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3.3), (WINDOWHEIGHT / 2))
    drawText('Press a key to play again', font, windowSurface, (WINDOWWIDTH / 3.3) - 80, (WINDOWHEIGHT / 3.3) + 50)

    if score <= 5:
        windowSurface.blit(SmallCake, (30, 360))
    if score > 5:
        if score < 10:
            windowSurface.blit(MediumCake, (30, 360))
    if score >= 10:
        windowSurface.blit(BigCake, (30, 360))
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()


#TODO ajouter les autres images de goodies
#TODO bonus champignon
#TODO ajouter l'image du gateau qu'on obtient par rapport à notre score

#TODO Aajouter le compteur de vie??

#TODO Ajouter un boss : chef patissier/animal
# TODO : Menu