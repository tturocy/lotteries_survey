from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    pass

class Page2(Page):
    pass

class Page3(Page):
    pass

class Page4(Page):
    pass

class Page5(Page):
    pass

class Page6(Page):
    pass

class Page7(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Page1,
                 Page2,
                 Page3,
                 Page4,
                 Page5,
                 Page6,
                 Page7,
                 ResultsWaitPage,
                 Results]
