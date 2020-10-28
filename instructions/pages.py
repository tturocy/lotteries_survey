from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class InstructionsPage1(Page):
    pass

class InstructionsPage2(Page):
    pass

class ComprehensionPage(Page):
    form_model = 'player'
    form_fields = ['answer']


page_sequence = [InstructionsPage1,
                 InstructionsPage2,
                 ComprehensionPage]
