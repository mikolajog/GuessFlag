import pygame
import pygame.locals
import pygame_gui

from FlagManager import FlagPagingManager
from Window import Window
from constants import SIZE_FLAG, FLAG_POSITIONS, WORKING_DIR
from documentationOpener import openDocumentationFile
from classifier import Classifier
import os
from question_mapper import QuestionProvider

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
        self.page = 0

        # Flag manager
        self.flag_manager = FlagPagingManager()

        # Question number
        self.question_number = 1

        self.clf = Classifier()
        self.clf.read('data/flag_data.csv', self.get_supported_country_list())
        self.clf.fit()

        self.question_provider = QuestionProvider(self.clf)

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
                        self.page = 0
                        self.answer(True)

                    if event.ui_element == self.window.noButton:
                        print("no Button pressed!")
                        self.page=0
                        self.answer(False)

                    if event.ui_element == self.window.restartButton:
                        self.__init__()
                        print("restart Button pressed!")
                        self.question_provider = QuestionProvider(self.clf)
                        self.window.draw()
                        self.draw_flags()


                    if event.ui_element == self.window.descriptionButton:
                        print("description Button pressed!")
                        openDocumentationFile()

                    if event.ui_element == self.window.rightButton:
                        if self.page <= self.flag_manager.get_possible_page_count(self.clf.get_current_labels()):
                            self.page += 1
                            print("right Button pressed!")
                            self.window.draw()
                            self.draw_flags()

                    if event.ui_element == self.window.leftButton:
                        if self.page>=1:
                            self.page -= 1
                            print("left Button pressed!")
                            self.window.draw()
                            self.draw_flags()

            self.window.manager.process_events(event)

        self.window.manager.update(time_delta)
        self.window.manager.draw_ui(self.window.surface)
        pygame.display.update()

        return False

    def answer(self, answer):
        self.question_provider.answer(self.question, answer)

        self.window.draw()
        self.draw_flags()

    def draw_flags(self):
        self.question = self.question_provider.get_question()
        self.window.questionLablel2.set_text(self.question.text)

        country_list = self.clf.get_current_labels()
        print(country_list)

        self.page = min(self.page, self.flag_manager.get_possible_page_count(country_list) - 1)

        if(len(country_list)==1):
            self.window.yesButton.disable()
            self.window.noButton.disable()
            self.window.questionLablel1.set_text("Thank you!")
            text = "The winner: " + str(country_list[0])
            self.window.questionLablel2.set_text(text)

        flags = self.flag_manager.get_current_flags_page(country_list, self.page)

        for i, flag in enumerate(flags):
            img = pygame.image.load(WORKING_DIR+"/img/flags/" + flag + ".png")
            img = pygame.transform.scale(img, SIZE_FLAG)
            self.window.surface.blit(img, FLAG_POSITIONS[i])

    # returns names of countries for which flags are included in the img folder
    def get_supported_country_list(self):
        return [f[:-4] for f in os.listdir('img/flags')]
