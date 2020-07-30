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

    def before_next_page(self):
        if self.player.lotterychoice == "A":
            self.player.payoff = (
                self.session.vars['lotteries']
                .loc[f"p{self.player.round_number}", self.player.roll]
            )

class ResultsPage(Page):
    pass


page_sequence = [DecisionPage, ResultsPage]
