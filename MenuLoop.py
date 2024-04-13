import pygame
import pygame_gui


class MenuLoop:
    def __init__(self, screen):
        self.screen = screen
        self.manager = pygame_gui.UIManager((800, 800))
        self.messageHandler = None
        self.map1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                 text='Map 1',
                                                 manager=self.manager)

        self.map2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 325), (100, 50)),
                                                 text='Map 2',
                                                 manager=self.manager)

    def tick(self):
        self.screen.fill((68, 85, 90))
        self.manager.draw_ui(self.screen)

    def handleMenuEvents(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if self.messageHandler is None:
                print("Button clicked, but there is no hanlder to handle it!")
                return

            if event.ui_element == self.map1:
                data = {"id": "HOST GAME", "mapName": "./resources/map1.txt"}
                self.messageHandler(data)
            if event.ui_element == self.map2:
                data = {"id": "HOST GAME", "mapName": "./resources/map2.txt"}
                self.messageHandler(data)

    def listenForMessages(self, messageHandler):
        self.messageHandler = messageHandler
