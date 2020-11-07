import pygame
import pygame.locals
import pygame_gui

from FlagManager import FlagManager
from Window import Window
from constants import SIZE_FLAG, FLAG_POSITIONS, WORKING_DIR
from documentationOpener import openDocumentationFile


class GuessFlags(object):
    """
    Puts together all parts of the project.
    """

    def __init__(self):
        pygame.init()

        # Initialize board
        self.window = Window()

        # Clock responsible for frequency of displaying flags
        self.fps_clock = pygame.time.Clock()

        # Page of pictures
        self.page = 1

        # Flag manager
        self.flag_manager = FlagManager()

        # Question number
        self.question_number = 1

    def run(self):
        """
        Main loop
        """
        self.window.draw()
        self.draw_flags()
        while not self.handle_events():
            pass

    def handle_events(self):
        """
                Function responsible for handling events in project
                for example mouse clicks
                :return True if the simulation should end
        """

        time_delta = self.fps_clock.tick(1000)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.window.yesButton:
                        print("yes Button pressed!")
                        self.question_number += 1
                        self.update_flags(self.question_number)
                        self.window.draw()
                        self.draw_flags()

                    if event.ui_element == self.window.noButton:
                        print("no Button pressed!")
                        self.question_number += 1
                        self.update_flags(self.question_number)
                        self.window.draw()
                        self.draw_flags()

                    if event.ui_element == self.window.restartButton:
                        print("restart Button pressed!")
                        self.question_number = 1
                        self.window.draw()
                        self.draw_flags()


                    if event.ui_element == self.window.descriptionButton:
                        print("description Button pressed!")
                        openDocumentationFile()

                    if event.ui_element == self.window.rightButton:
                        if self.page <= self.flag_manager.get_possible_pages_number():
                            self.page += 1
                            print("right Button pressed!")
                            self.window.draw()
                            self.draw_flags()

                    if event.ui_element == self.window.leftButton:
                        if self.page>1:
                            self.page -= 1
                            print("left Button pressed!")
                            self.window.draw()
                            self.draw_flags()

            self.window.manager.process_events(event)

        self.window.manager.update(time_delta)
        self.window.manager.draw_ui(self.window.surface)
        pygame.display.update()

        return False

    def draw_flags(self):
        if self.page > self.flag_manager.get_possible_pages_number():
            self.page=self.flag_manager.get_possible_pages_number()
        self.window.questionLablel2.set_text(self.flag_manager.get_next_question(self.question_number))
        flags = self.flag_manager.get_current_flags_page(self.page)
        print(flags)
        number = 0
        for flag in flags:
            img = pygame.image.load(WORKING_DIR+"/img/flags/" + flag + ".png")
            img = pygame.transform.scale(img, SIZE_FLAG)
            self.window.surface.blit(img, FLAG_POSITIONS[number])
            number += 1

    def update_flags(self, number):
        self.flag_manager.list_of_flags = self.flag_manager.list_of_flags[:round(len(self.flag_manager.list_of_flags)/2)]



