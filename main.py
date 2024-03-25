import pygame
from Gameloop import Gameloop


def main(windowSize=800):
    print('start')
    pygame.init()
    game = Gameloop(windowSize)
    game.start()

if __name__ == '__main__':
    main()