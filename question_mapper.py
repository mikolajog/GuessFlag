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
    'triangle': 'a triangle',
    'icon': 'an inanimate icon or emblem',
    'animate': 'an animate icon',
    'text': 'text',
    'sunstars': 'stars or suns',
    'crosses': 'upright crosses',
    'saltires': 'diagonal crosses',
    'quarters': 'quarter sections',
    'crescent': 'a crescent moon symbol'
}

colors = ['white', 'black', 'red', 'green', 'gold/yellow', 'blue', 'orange/brown']
    
class QuestionProvider:
    def __init__(self, classifier):
        self.clf = classifier
        self.colors = self.clf.features

    def get_question(self):
        return self.map_question(*self.clf.get_question())

    def map_question(self, feature, threshold):
        if feature in simple_countable_object_mapper:
            mapped_name = simple_countable_object_mapper[feature]
            if threshold <= 1:
                return Question(f'Are there any {mapped_name} in the flag?', True)

            seed = random.randrange(0, 4)
            if seed == 0:
                return Question(f'Is the number of {mapped_name} less than {math.ceil(threshold)}?')
            if seed == 1:
                return Question(f'Is the number of {mapped_name} more than {math.floor(threshold)}?', True)
            if seed == 2:
                return Question(f'Does it have less than {math.ceil(threshold)} {mapped_name}?')
            if seed == 3:
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
            return Question(f'Is {color} the leading color of the flag?', True)

        if feature == 'hasMainHue':
            return Question(f'Does it have a leading color?', True)

        raise ValueError(f'Question mapping not found for feature {feature} and threshold {threshold}')