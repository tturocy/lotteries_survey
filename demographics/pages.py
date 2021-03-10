# from otree.api import Currency as c, currency_range
from ._builtin import Page  # , WaitPage
# from .models import Constants


class Introduction(Page):
    pass


class QuestionPage(Page):
    template_name = "demographics/GeneralDemographics.html"
    form_model = 'player'


class Page1(QuestionPage):
    form_fields = ['gender']


class Page2(QuestionPage):
    form_fields = ['age']


class Page3(QuestionPage):
    form_fields = ['countryborn']


class Page4(QuestionPage):
    form_fields = ['countrynow']


class Page5(QuestionPage):
    form_fields = ['degree']


class Page6(QuestionPage):
    form_fields = ['department']

    def is_displayed(self):
        # Only display if participant responded and gave a degree course
        return self.player.degree is not None and self.player.degree <= 5


class Page7(QuestionPage):
    form_fields = ['timeuea']


page_sequence = [
    Introduction,
    Page1,
    Page2,
    Page3,
    Page4,
    Page5,
    Page6,
    Page7,
]
