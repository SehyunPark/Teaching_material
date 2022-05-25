import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    mousepos = []

    while True:
        SURFACE.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousepos.append(event.pos)
        
        for pos in mousepos:
            pygame.draw.circle(SURFACE, (3, 252, 123), pos, 8)
        
        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()


    