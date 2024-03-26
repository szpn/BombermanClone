import pygame
from Gameloop import Gameloop
from Menuloop import Menuloop


def main(windowSize=800):
    print('start')
    pygame.init()
    screen = pygame.display.set_mode((windowSize, windowSize))
    #gameloop = Gameloop(screen)
    menuloop = Menuloop(screen)
    menuloop.start()
    #gameloop.start()

if __name__ == '__main__':
    main()