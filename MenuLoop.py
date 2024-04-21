import pygame
import pygame_gui


class MenuLoop:
    def __init__(self, screen,connection):
        self.screen = screen
        self.connection = connection
        self.screen_rect = screen.get_rect()
        self.manager = pygame_gui.UIManager((800, 800))
        self.messageHandler = None
        self.hostGamePanel = pygame_gui.elements.UIPanel(relative_rect=self.screen_rect,
                                                             manager=self.manager)

        self.map1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                 text='Map 1',
                                                 manager=self.manager,
                                                 container=self.hostGamePanel)

        self.map2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 325), (100, 50)),
                                                 text='Map 2',
                                                 manager=self.manager,
                                                 container=self.hostGamePanel)

        self.map3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 375), (100, 50)),
                                                 text='Map 3',
                                                 manager=self.manager,
                                                 container=self.hostGamePanel)

        self.hostGamePanel.hide()

        self.mainMenuPanel = pygame_gui.elements.UIPanel(relative_rect=self.screen_rect,
                                                         manager=self.manager)

        self.titleLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 100), (100, 100)),
                                                      text='BOMBERMAN',
                                                      manager=self.manager,
                                                      container=self.mainMenuPanel)

        self.hostGameButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 200), (200, 100)),
                                                            text='Host game',
                                                            manager=self.manager,
                                                            container=self.mainMenuPanel)

        self.joinGameButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 300), (200, 100)),
                                                           text='Join game',
                                                           manager=self.manager,
                                                           container=self.mainMenuPanel)



    def tick(self):
        self.screen.fill((68, 85, 90))
        self.manager.draw_ui(self.screen)

    def handleMenuEvents(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if self.messageHandler is None:
                print("Button clicked, but there is no hanlder to handle it!")
                return

            if event.ui_element == self.joinGameButton:
                data = {"id": "JOIN GAME"}
                self.messageHandler(data)
                self.mainMenuPanel.hide()

            if event.ui_element == self.hostGameButton:
                self.mainMenuPanel.hide()
                self.hostGamePanel.show()

            if event.ui_element == self.map1:
                data = {"id": "HOST GAME", "mapName": "./resources/map1.txt"}
                self.messageHandler(data)
                self.hostGamePanel.hide()

            if event.ui_element == self.map2:
                data = {"id": "HOST GAME", "mapName": "./resources/map2.txt"}
                self.messageHandler(data)
                self.hostGamePanel.hide()

            if event.ui_element == self.map3:
                data = {"id": "HOST GAME", "mapName": "./resources/map3.txt"}
                self.messageHandler(data)
                self.hostGamePanel.hide()

    def listenForMessages(self, messageHandler):
        self.messageHandler = messageHandler
