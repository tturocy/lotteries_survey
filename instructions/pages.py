# from otree.api import Currency as c, currency_range
from ._builtin import Page  # , WaitPage
# from .models import Constants


class Welcome(Page):
    pass


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


class MenuItem:
    def __init__(self, imagepath, lottery):
        self.imagepath = imagepath
        self.lottery = lottery

    def expected(self):
        return f"{self.lottery.mean():.2f}"

    def risk(self):
        return f"{self.lottery.std():.1f}"


class DecisionExample(Page):
    is_live = False

    def vars_for_template(self):
        menu_number = 26
        return {
            'menu': [
                MenuItem(
                    f"instructions/lottery_{lottery_name}{menu_number}.jpg",
                    self.session.vars['lotteries'].loc[f"{lottery_name}{menu_number}"]
                )
                for lottery_name in ['p', 'q']
            ],
            'is_live': self.is_live
        }


class DecisionRounds(DecisionExample):
    is_live = False


class ChoosingOption(DecisionExample):
    is_live = True


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
    Welcome,
    Introduction,
    OptionComprehension1,
    OptionComprehension2,
    OptionComprehension3,
    OptionComprehension4,
    DecisionRounds,
    ChoosingOption,
    DeterminingEarnings,
    GeneralComprehension1,
    GeneralComprehension2,
    Summary,
]
