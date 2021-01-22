from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class InstructionsPage1(Page):
    pass

class InstructionsPage2(Page):
    form_model = 'player'
    form_fields = ['answer1']

    def vars_for_template(self):
        return {
            'question': "How much would you earn if the number 38 was drawn?"
        }


class InstructionsPage3(Page):
    form_model = 'player'
    form_fields = ['answer2']

    def vars_for_template(self):
        return {
            'question': "How much would you earn if the number drawn was between 61 and 100?"
        }


class InstructionsPage4(Page):
    form_model = 'player'
    form_fields = ['answer3']

class InstructionsPage5(Page):
    form_model = 'player'
    form_fields = ['answer4']

class InstructionsPage6(Page):
    pass

class InstructionsPage7(Page):
    pass

class InstructionsPage8(Page):
    form_model = 'player'
    form_fields = ['answer8']

class InstructionsPage9(Page):
    form_model = 'player'
    form_fields = ['answer9']

class InstructionsPage10(Page):
    pass

page_sequence = [InstructionsPage1,
                InstructionsPage2,
                InstructionsPage3,
                InstructionsPage4,
                InstructionsPage5,
                InstructionsPage6,
                InstructionsPage7,
                InstructionsPage8,
                InstructionsPage9,
                InstructionsPage10,
                 ]
