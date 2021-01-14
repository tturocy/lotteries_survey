from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    pass

class Page2(Page):
    pass

class Page3(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Page1,
                 Page2,
                 Page3,
                 ResultsWaitPage,
                 Results]
