from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class InstructionsPage1(Page):
    pass

class InstructionsPage2(Page):
    form_model = 'player'
    form_fields = ['answer']

class InstructionsPage2(Page):
    form_model = 'player'
    form_fields = ['answer1']

class InstructionsPage3(Page):
    form_model = 'player'
    form_fields = ['answer2']

class InstructionsPage4(Page):
    form_model = 'player'
    form_fields = ['answer3']

class InstructionsPage5(Page):
    form_model = 'player'
    form_fields = ['answer4']

class InstructionsPage6(Page):
    pass

page_sequence = [#InstructionsPage1,
                #InstructionsPage2,
                #InstructionsPage3,
                #InstructionsPage4,
                #InstructionsPage5,
                InstructionsPage6,
                 ]
