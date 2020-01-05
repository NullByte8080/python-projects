import pygame
import time
from random import *

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

surfaceWidth = 1200
surfaceHeight = 800

imageHeight = 150
imageWidth = 500

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))

pygame.display.set_caption('Helicopter')

clock = pygame.time.Clock()
img = pygame.image.load('heli.png')

def blocks(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, white, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, white, [x_block, y_block+block_height+gap, block_width, surfaceHeight])

def replay_or_quit():

    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            continue

        return event.key
    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def helicopter(x, y, image):
    surface.blit(img, (x, y))

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextReact = makeTextObjs(text, largeText)
    titleTextReact.center = surfaceWidth/2, surfaceHeight/2
    surface.blit(titleTextSurf, titleTextReact)

    typeTextSurf, typeTextReact = makeTextObjs('press any key to continue', smallText)
    typeTextReact.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typeTextSurf, titleTextReact)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()

def gameover():
   msgSurface('Kaboom!')



def main():
    x = 150
    y = 150
    y_move = 0

    x_block = surfaceWidth
    y_block = 0

    block_width = 75
    block_height = randint(0, (surfaceHeight / 2))
    gap = imageHeight * 3

    block_move = 3


    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5

        y += y_move


        surface.fill(black)
        helicopter(x, y, img)
        blocks(x_block, y_block, block_width, block_height, gap)
        x_block -= block_move

        if y > surfaceHeight-185 or y < 0:
            gameover()

        if x_block < (-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0, (surfaceHeight / 2))

        if x + imageWidth > x_block:
            if x < x_block + block_width:
                print("possibly within the boundries of x upper")
                if y < block_height:
                    print("y crossover Upper")
                    if x - imageWidth < block_width + x_block:
                        print("game over hit Upper")
                        gameover()

        if x + imageWidth > x_block:
            print("x crossover")

            if y + imageHeight > block_height + gap:
                print("y crossover lower")

                if x < block_width + x_block:
                    print("game over touching lower")
                    gameover()


        pygame.display.update()
        clock.tick(90)
main()
pygame.quit()
quit()