from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InstructionsPage1(Page):
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


class InstructionsPage6(Page):
    pass

class InstructionsPage7(Page):
    pass

class InstructionsPage8(Page):
    form_model = 'player'
    form_fields = ['answer8']

class InstructionsPage9(Page):
    form_model = 'player'
    form_fields = ['answer9']

class InstructionsPage10(Page):
    pass


page_sequence = [
    InstructionsPage1,
    OptionComprehension1,
    OptionComprehension2,
    OptionComprehension3,
    OptionComprehension4,
    InstructionsPage6,
    InstructionsPage7,
    InstructionsPage8,
    InstructionsPage9,
    InstructionsPage10,
]
