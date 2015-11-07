import pygame
from pygame.locals import *

windowSize = [800,800]

screen = pygame.display.set_mode((windowSize[0],windowSize[1]))
pygame.init()

finish = False
log = True
writeLog = False
user = ""

police = pygame.font.SysFont("broadway",50,bold=False,italic=False)

pygame.draw.rect(screen, (255,255,255), (0, 0, windowSize[0], windowSize[1]))

pygame.draw.rect(screen, (175,175,175), (windowSize[0]/2-150, windowSize[0]/2-50, 300, 50))

screen.blit(police.render("Pseudo : ",1,(0,0,0)), (windowSize[0]/2-150,windowSize[1]/2-100))

pygame.display.flip()

while finish==False:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if log == True:
                if screen.get_at((event.pos[0], event.pos[1])) == (175, 175, 175, 255):
                    pygame.draw.rect(screen, (0, 0, 0), (windowSize[0]/2+130, windowSize[0]/2-40, 10, 30))
                    writeLog = True
                else:
                    pygame.draw.rect(screen, (175,175,175), (windowSize[0]/2-150, windowSize[0]/2-50, 300, 50))
                    writeLog = False

        if event.type == KEYDOWN:
            if writeLog == True:
                if event.key <= 127:
                    user+=chr(event.key)
                if event.key == K_RETURN:
                    pygame.draw.rect(screen, (175,175,175), (windowSize[0]/2-150, windowSize[0]/2-50, 300, 50))
                    writeLog = False
                
                screen.blit(police.render(user,1,(0,0,0)), (windowSize[0]/2-140,windowSize[1]/2-40))

        if event.type == QUIT:
            finish = True

    pygame.display.flip()
