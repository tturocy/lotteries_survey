# from otree.api import Currency as c, currency_range
from ._builtin import Page  # , WaitPage
from .models import Constants


class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['lotterychoice']

    def before_next_page(self):
        self.player.process_decision()


page_sequence = [
    DecisionPage,
]
