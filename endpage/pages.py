from otree.api import Currency as c
from ._builtin import Page
# from .models import Constants


class Introduction(Page):
    def before_next_page(self):
        self.player.realise_paid_period()


class SummaryPage(Page):
    pass


class RealisePage(Page):
    pass


class EarningsPage(Page):
    def vars_for_template(self):
        return {'payoff_part2': self.participant.vars.get('part2', c(0)) }


page_sequence = [
    Introduction,
    SummaryPage,
    RealisePage,
    EarningsPage,
]
