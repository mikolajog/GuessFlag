import random
import math

class Question:
    def __init__(self, text, inverted = False):
        self.text = text
        self.inverted = inverted

simple_countable_object_mapper = {
    'bars': 'vertical bars',
    'stripes': 'horizontal stripes',
    'colours': 'colors',
    'circles': 'circles',
    'triangle': 'triangles',
    'icon': 'inanimate icons or emblems',
    'animate': 'animate icons',
    'text': 'text',
    'sunstars': 'stars or suns',
    'crosses': 'upright crosses',
    'saltires': 'diagonal crosses',
    'quarters': 'quarter sections',
    'crescent': 'crescent moon symbols'
}

colors = ['white', 'black', 'red', 'green', 'gold/yellow', 'blue', 'orange/brown']

class QuestionProvider:
    def __init__(self, classifier):
        self.clf = classifier
        self.colors = self.clf.features

        self.delayed_question_mainhue_color = None
        self.was_mainhue_none_asked = False
        self.has_mainhue = None

    def get_question(self):
        if self.delayed_question_mainhue_color != None:
            return self.get_mainhue_question(self.delayed_question_mainhue_color)

        return self.map_question(*self.clf.get_question())

    def map_question(self, feature, threshold):
        if feature in simple_countable_object_mapper:
            mapped_name = simple_countable_object_mapper[feature]
            if threshold <= 1:
                return Question(f'Are there any {mapped_name} in the flag?', True)

            seed = random.randrange(0, 2)
            if seed == 0:
                return Question(f'Is the number of {mapped_name} more than {math.floor(threshold)}?', True)
            if seed == 1:
                return Question(f'Does it have more than {math.floor(threshold)} {mapped_name}', True)

        if feature in colors:
            return Question(f'Does it contain {feature} elements?', True)

        if 'topleft_' in feature:
            color = feature[len('topleft_'):]
            return Question(f'Does it contain {color} color in the top left corner?', True)

        if 'botright_' in feature:
            color = feature[len('botright_'):]
            return Question(f'Does it contain {color} color in the bottom right corner?', True)

        if 'mainhue_' in feature:
            color = feature[len('mainhue_'):]
            if color != "none":
                if self.was_mainhue_none_asked:
                    if self.has_mainhue:
                        return self.get_mainhue_question(color)

                    self.clf.apply_answer(True)
                    return self.map_question(*self.clf.get_question())

                delayed_question_mainhue_color = color
                self.was_mainhue_none_asked = True
            else:
                if self.was_mainhue_none_asked:
                    self.clf.apply_answer(not self.has_mainhue)
                    return self.map_question(*self.clf.get_question())
                self.was_mainhue_none_asked = True
            
            return Question(f'Does the flag have a leading color?')

        raise ValueError(f'Question mapping not found for feature {feature} and threshold {threshold}')

    def answer(self, question, is_fulfilled):
        if self.was_mainhue_none_asked and self.has_mainhue == None:
            self.has_mainhue = is_fulfilled

        real_answer = is_fulfilled

        if question.inverted:
            real_answer = not real_answer

        if self.delayed_question_mainhue_color == None:
            self.clf.apply_answer(real_answer)
            return

        if not real_answer: #no leading color
            self.clf.apply_answer(False)
        
        # if leading color exists skip this answer to allow for the specific color question


    def get_mainhue_question(self, color):
        return Question(f'Is {color} the leading color of the flag?', True)