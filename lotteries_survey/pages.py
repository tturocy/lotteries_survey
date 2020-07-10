from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['lotterychoice']


class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['lotterychoice']

    def vars_for_template(self):
        return {'num_rounds': Constants.num_rounds}


class ResultsPage(Page):
    pass


page_sequence = [DecisionPage, ResultsPage]
