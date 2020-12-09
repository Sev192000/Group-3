import pygame, random, sys, self
from pygame.locals import *
from os import path


# Set up pygame, the window, and the mouse cursor.
pygame.init()
...
self.load_data()
#faut mettre la def de load_data juste en dessous apparement
def load_data(self):
    self.dir = path.dirname(__file__)
    # load highscore
    with open(path.join(self.dir , HS_FILE), 'w') as f:
        try:
            self.highscore = int(f.read())
        except:
            self.highscore = 0

# Set up images.
playerImage = pygame.image.load('bol.png')
...
broccoli = pygame.image.load('broccoli.png')

#a mettre juste en dessous

#Set up files
HS_FILE = 'highscore.txt'

...

# Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()
    if self.score > self.highscore:
        self.highscore = self.score
        self.draw_text("New High Score!")
        with open(path.join(self.dir, HS_FILE), 'w') as f:
            f.write(str(self.score))


