# from otree.api import Currency as c, currency_range
from ._builtin import Page  # , WaitPage
from .models import Constants


class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['lotterychoice']

    def vars_for_template(self):
        return {
            'num_rounds': Constants.num_rounds,
            'images': [
                f"decisions/lottery_p{self.round_number}.jpg",
                f"decisions/lottery_q{self.round_number}.jpg"
            ]
        }

    def before_next_page(self):
        self.player.process_decision()


class ResultsPage(Page):
    def vars_for_template(self):
        choice = ["p", "q"][self.player.lotterychoice]
        return {
            'num_rounds': Constants.num_rounds,
            'image':
                f"decisions/lottery_{choice}{self.round_number}.jpg"
        }


page_sequence = [
    DecisionPage,
    ResultsPage,
]
