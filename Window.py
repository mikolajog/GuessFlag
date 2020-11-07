import netCDF4

import pygame
import pygame.locals
import pygame_gui

from constants import *


class Window(object):
    """
    Simulation board responsible for:
    providing window (__init__)
    drawing(draw)
    """

    def __init__(self):
        # Initialize surface, background
        self.surface = pygame.display.set_mode(RESOLUTION, 0, 32)
        pygame.display.set_caption('Guess Flag Project')
        self.background = pygame.Surface(RESOLUTION)

        # Initialize manager for buttons
        self.manager = pygame_gui.UIManager(RESOLUTION)

        # Initialize Menu buttons
        self.restartButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_RESTARTBUTTON, SIZE_RESTARTBUTTON),
            text='Restart',
            manager=self.manager)

        self.descriptionButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_DESCRIPTIONBUTTON, SIZE_DESCRIPTIONBUTTON),
            text='TROLOOLOLOOO',
            manager=self.manager)

        self.yesButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_YESBUTTON, SIZE_YESBUTTON),
            text='YES',
            manager=self.manager)

        self.noButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_NOBUTTON, SIZE_NOBUTTON),
            text='NO',
            manager=self.manager)

        self.leftButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_LEFTBUTTON, SIZE_LEFTBUTTON),
            text='<<',
            manager=self.manager)

        self.rightButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_RIGHTBUTTON, SIZE_RIGHTBUTTON),
            text='>>',
            manager=self.manager)



        # Initlialize labels
        self.titleLablel = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_TITLELABEL, SIZE_TITLELABEL),
            text='GUESS FLAGS PROJECT',
            manager=self.manager,
            tool_tip_text="This is a project of guessing flag basing on up to 9 questions. Authors: M.Ogarek, K.Polarczyk, K.Rychter, Z.Śmiech")

        self.questionLablel1 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_QUESTIONLABEL1, SIZE_QUESTIONLABEL1),
            text='QUESTION:',
            manager=self.manager)

        self.questionLablel2 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_QUESTIONLABEL2, SIZE_QUESTIONLABEL2),
            text='Which is your flag?',
            manager=self.manager)



    def draw(self):
        # setting background
        img = pygame.image.load("img/background.jpg")
        img = pygame.transform.scale(img, (1350, 760))
        self.surface.blit(img, (0,0))


        img = pygame.image.load("img/logoagh.jpg")
        img = pygame.transform.scale(img, (100, 100))
        self.surface.blit(img, (275, 610))

        pygame.display.update()


