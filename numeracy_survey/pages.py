from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer1']

class Page2(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer2']

class Page3(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer3']

class Page4(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer4']

class Page5(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer5']

class Page6(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer6']

class Page7(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer7']

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
