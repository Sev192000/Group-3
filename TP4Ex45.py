import pygame, random, sys
from pygame.locals import *

GOODIEMINSIZE = 15
GOODIEMAXSIZE = 30


def falling_goodie():
    global GOODIEMINSIZE, GOODIEMAXSIZE
    GOODIEMAXSIZE = GOODIEMAXSIZE + 2
    WINDOW.coords(chocolateImage, (GOODIEMINSIZE, GOODIEMAXSIZE))
    detect_catch()
    if GOODIEMAXSIZE > WINDOWHEIGHT:
        GOODIEMAXSIZE = 30
        GOODIEMINSIZE = random.randint(25, WINDOWWIDTH - 25)
    window.afer(20, falling_goodie())


def detect_catch():
    global score, screen_score, GOODIEMINSIZE, GOODIEMAXSIZE
    if GOODIEMINSIZE > playerImage - 50 and GOODIEMINSIZE < playerImage + 50 and GOODIEMAXSIZE >= WINDOWHEIGHT - 100:
        window.delete(screen_score)
        score = score + 1
        screen_score = window.create_text(WINDOWWIDTH / 2, 50, text=score, font=("Helvetica", 70, "bold"),
                                          fill="lightgreen")
        GOODIEMAXSIZE = -25
        GOODIEMINSIZE = random.randint((25, WINDOWWIDTH - 25))