# from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
# from .models import Constants


class RealisePage(WaitPage):
    after_all_players_arrive = 'realise_paid_period'


class SummaryPage(Page):
    pass


class EarningsPage(Page):
    pass


page_sequence = [
    RealisePage,
    SummaryPage,
    EarningsPage,
]
