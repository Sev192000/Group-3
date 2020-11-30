import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 600  # width of the game window
WINDOWHEIGHT = 600  # height of game window
TEXTCOLOR = (0, 0, 0)  # color of the text
BACKGROUNDCOLOR = (200, 255, 255)  # backgroun color
FPS = 60  # pictures per seconds
BADDIEMINSIZE = 30  # min size of baddie
BADDIEMAXSIZE = 40  # max size of baddie
BADDIEMINSPEED = 1  # min speed of baddie
BADDIEMAXSPEED = 8  # max speed of baddie
ADDNEWBADDIERATE = 100  # speed/rate of new baddie
PLAYERMOVERATE = 5  # speed/rate of player movement
GOODIEMINSIZE = 30  # min size of goodie
GOODIEMAXSIZE = 40  # max size of goodie
GOODIEMINSPEED = 1  # min speed of goodie
GOODIEMAXSPEED = 8  # max speed of goodie
ADDNEWGOODIERATE = 100  # speed/rate of new goodie


# this function terminates the game
def terminate():
    pygame.quit()
    sys.exit()


# this function waits till the player presses a key
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()  # calls the function terminate
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Pressing ESC quits.
                    terminate()  # calls the function terminate
                return


# this function returns true if the player has hit a baddie
# input parameters: playerRect, baddies
def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False  # returns false if the player hasn't hit a baddie


# this function returns true if the player has hit a goodie
# input parameters : playerRect, baddies
def playerHasHitGoodie(playerRect, goodies):
    for g in goodies:
        if playerRect.colliderect(g['rect']):
            return True
    return False  # returns false if the player hasn't hit a goodie


# this function helps to visualize the text
# input parameters: text, font, surface, x, y
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


if __name__ == "__main__":
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
    playerImage = pygame.image.load('bol.png')  # load player image
    playerRect = playerImage.get_rect()  # define the player rect
    baddieImage = pygame.image.load('Bombe.png')  # load baddie image
    goodieImage = pygame.image.load('chocolate.png')  # load goodie image
    pastryGirl = pygame.image.load('pastrygirl.png')  # load pastry girl image
    textbubble = pygame.image.load('textbubble.png')  # load picture of text bubble
    bigCake = pygame.image.load('BigCake.png')  # load big cake image
    mediumCake = pygame.image.load('GirlMediumCake.png')  # load medium cake image
    smallCake = pygame.image.load('SmallCake.png')  # load small cake image

    # Show the "Start" screen.
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(pastryGirl, (30, 360))  # faut voir l'emplacement de la fille
    windowSurface.blit(textbubble, (120, 100))
    drawText('Running pastry chef', font, windowSurface, (WINDOWWIDTH / 4), (WINDOWHEIGHT / 3.3))
    drawText('Press a key to start', font, windowSurface, (WINDOWWIDTH / 2.9) - 30, (WINDOWHEIGHT / 3.5) + 70)
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

        while True:
            # The game loop runs while the game part is playing.

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
                newBaddie = {
                    'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize, baddieSize,
                                        baddieSize),
                    'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                    'surface': pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                    }

                baddies.append(newBaddie)

            if not reverseCheat and not slowCheat:
                GoodieAddcounter += 1
            if GoodieAddcounter == ADDNEWGOODIERATE:
                GoodieAddcounter = 0
                goodieSize = random.randint(GOODIEMINSIZE, GOODIEMAXSIZE)
                newGoodie = {
                    'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - goodieSize), 0 - goodieSize, goodieSize,
                                        goodieSize),
                    'speed': random.randint(GOODIEMINSPEED, GOODIEMAXSPEED),
                    'surface': pygame.transform.scale(goodieImage, (goodieSize, goodieSize)),
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
                    topScore = score  # set new top score
                break

            mainClock.tick(FPS)

            # Check if any of the goodies have hit the player.
            if playerHasHitGoodie(playerRect, goodies):
                score = score + 1
                if score >= topScore:
                    topScore = score  # set new top score

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
            windowSurface.blit(pastryGirl, (30, 360))
        if score > 5:
            if score < 10:
                windowSurface.blit(baddieImage, (30, 360))
        if score >= 10:
            windowSurface.blit(pastryGirl, (30, 360))
        pygame.display.update()
        waitForPlayerToPressKey()

        gameOverSound.stop()

# TODO chocolat qui clignote

# TODO ajouter les autres images de goodies
# TODO bonus champignon
# TODO ajouter l'image du gateau qu'on obtient par rapport à notre score

# TODO Aajouter le compteur de vie??
