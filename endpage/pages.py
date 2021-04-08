# from otree.api import Currency as c, currency_range
from ._builtin import Page
# from .models import Constants


class RealisePage(Page):
    def before_next_page(self):
        self.player.realise_paid_period()


class SummaryPage(Page):
    pass


class EarningsPage(Page):
    pass


page_sequence = [
    RealisePage,
    SummaryPage,
    EarningsPage,
]
