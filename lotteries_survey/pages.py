from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['lotterychoice']


class ResultsPage(Page):
    pass


page_sequence = [DecisionPage, ResultsPage]
