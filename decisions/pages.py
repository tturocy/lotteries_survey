# from otree.api import Currency as c, currency_range
from ._builtin import Page  # , WaitPage
from .models import Constants


class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['lotterychoice']

    def before_next_page(self):
        self.player.process_decision()


class ResultsPage(Page):
    def vars_for_template(self):
        return {
            'item': self.participant.vars['choices'][self.round_number].item
        }


page_sequence = [
    DecisionPage,
]
