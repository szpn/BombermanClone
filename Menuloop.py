import pygame
import pygame_gui

class Menuloop:
    def __init__(self, screen):
        self.screen = screen
        self.manager = pygame_gui.UIManager((800, 800))
        self.run = True
        map1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                    text='Map 1',
                                                    manager=self.manager)



    def start(self):
        clock = pygame.time.Clock()
        while self.run:
            time_delta = clock.tick(60) / 1000.0
            self.screen.fill((68, 85, 90))

            self.manager.draw_ui(self.screen)

            self.handleEvents()
            pygame.display.update()
            self.manager.update(time_delta)


    def handleEvents(self):
        for event in pygame.event.get():
            self.manager.process_events(event)
            if event.type == pygame.QUIT:
                self.run = False