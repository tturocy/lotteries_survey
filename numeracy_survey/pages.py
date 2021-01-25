from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class NumeracyPage1(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer1']

class NumeracyPage2(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer2']

class NumeracyPage3(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer3']

class NumeracyPage4(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer4']

class NumeracyPage5(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer5']

class NumeracyPage6(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer6']

class NumeracyPage7(Page):
    template_name = "numeracy_survey/GeneralNumeracy.html"
    form_model = 'player'
    form_fields = ['answer7']

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [NumeracyPage1,
                 NumeracyPage2,
                 NumeracyPage3,
                 NumeracyPage4,
                 NumeracyPage5,
                 NumeracyPage6,
                 NumeracyPage7,
                 ResultsWaitPage,
                 Results]
