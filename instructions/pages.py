from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class OptionComprehension1(Page):
    template_name = "instructions/OptionComprehension.html"
    form_model = 'player'
    form_fields = ['answer1']


class OptionComprehension2(Page):
    template_name = "instructions/OptionComprehension.html"
    form_model = 'player'
    form_fields = ['answer2']


class OptionComprehension3(Page):
    template_name = "instructions/OptionComprehension.html"
    form_model = 'player'
    form_fields = ['answer3']


class OptionComprehension4(Page):
    template_name = "instructions/OptionComprehension.html"
    form_model = 'player'
    form_fields = ['answer4']


class DecisionRounds(Page):
    pass


class DeterminingEarnings(Page):
    pass


class GeneralComprehension1(Page):
    template_name = "instructions/GeneralComprehension.html"
    form_model = 'player'
    form_fields = ['answer8']


class GeneralComprehension2(Page):
    template_name = "instructions/GeneralComprehension.html"
    form_model = 'player'
    form_fields = ['answer9']


class Summary(Page):
    pass


page_sequence = [
    Introduction,
    OptionComprehension1,
    OptionComprehension2,
    OptionComprehension3,
    OptionComprehension4,
    DecisionRounds,
    DeterminingEarnings,
    GeneralComprehension1,
    GeneralComprehension2,
    Summary,
]
