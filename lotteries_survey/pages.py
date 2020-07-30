from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['lotterychoice']

    def vars_for_template(self):
        return {
            'num_rounds': Constants.num_rounds,
            'images': [
                f"lotteries_survey/lottery_p{self.round_number}.jpg",
                f"lotteries_survey/lottery_q{self.round_number}.jpg"
            ]
        }

    def before_next_page(self):
        self.player.realise_payoff()


class ResultsPage(Page):
    def vars_for_template(self):
        choice = ["p", "q"][self.player.lotterychoice]
        return {
            'num_rounds': Constants.num_rounds,
            'image':
                f"lotteries_survey/lottery_{choice}{self.round_number}.jpg"
        }


page_sequence = [DecisionPage, ResultsPage]
