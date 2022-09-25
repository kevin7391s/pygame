import pygame, sys
import time
pygame.init()

size = width, height = 930, 720
blue = 135, 206, 235
speed = [2,2]

screen = pygame.display.set_mode(size)

ball = pygame.image.load("assets/intro_ball.gif")
ballrect = ball.get_rect()

background = pygame.image.load("assets/gamebackground.jpg")
#bg_rect = background.get_rect(left=0, top = height/1.5, width= 930, height = 100)
bg_rect = pygame.transform.scale(background, (width, height))
count = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ballrect = ballrect.move(speed)
    speed = [speed[0] + 1, speed[1] + 1]
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < (height/4) and count > 0 or ballrect.bottom > (height/1.25):
        speed[1] = -speed[1]
        count += 1
    speed = [speed[0] + 1, speed[1] + 1]
    time.sleep(.1)
    screen.fill(blue)
    screen.blit(background, (0,0))
    screen.blit(ball, ballrect)
    pygame.display.flip()
