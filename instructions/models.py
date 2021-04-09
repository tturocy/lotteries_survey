import django.forms.widgets

from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    # Currency as c,
    # currency_range,
)


author = 'Prachi Hejib'

doc = "Instructions for guidance in investment decisions"


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class CurrencyInput(django.forms.widgets.NumberInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render(self, *args, **kwargs):
        return (
            '<div class="input-group">'
            '<span class="input-group-text">£</span>'
            f'{super().render(*args, **kwargs)}'
            '</div>'
        )


class Player(BasePlayer):
    answer1 = models.IntegerField(
        label="How much would you earn if ball number 38 was drawn?",
        widget=CurrencyInput
    )
    answer2 = models.IntegerField(
        label="How much would you earn if a ball number between 61 and 100 was drawn?",
        widget=CurrencyInput
    )
    answer3 = models.IntegerField(
        label="Which ball is more likely to be drawn, ball number 4 or ball number 72?",
        choices=[
            [1, "Ball number 4 is more likely"],
            [2, "Ball number 72 is more likely"],
            [3, "Ball number 4 and ball number 72 are equally likely"],
        ],
        widget=widgets.RadioSelect
    )
    answer4 = models.IntegerField(
        label="How many balls out of the 100 would result in earnings of £10?"
    )
    answer8 = models.IntegerField(
        label="How many rounds will be selected for payment?"
    )
    answer9 = models.IntegerField(
        label="How likely is it that a given round will be selected for payment?",
        choices=[
            [1, "A round with a higher ball drawn is more likely to be selected"],
            [2, "Later rounds are more likely to be selected"],
            [3, "All rounds are equally likely to be selected"]
        ],
        widget=widgets.RadioSelect
    )

    @staticmethod
    def answer1_error_message(answer):
        if answer != 10:
            return [
                "To find the answer, "
                "use the numbers along the bottom of the bar, and find the segment "
                "containing the number 38."
            ]

    @staticmethod
    def answer2_error_message(answer):
        if answer != 20:
            return [
                "To find the answer, "
                "use the numbers along the bottom of the bar, and find the segment "
                "with the range from 61 and 100."
            ]

    @staticmethod
    def answer3_error_message(answer):
        if answer != 3:
            return [
                "Remember that the selected ball will be drawn "
                "from a virtual bag "
                "containing balls numbered 1 to 100, where each ball is equally likely to be drawn."
            ]

    @staticmethod
    def answer4_error_message(answer):
        if answer != 25:
            return [
                "To find the answer, "
                "use the numbers along the top of the bar, and find the segment "
                "corresponding to earnings of £10."
            ]

    @staticmethod
    def answer8_error_message(answer):
        if answer != 1:
            return [
                "One of the 25 rounds will be selected for payment."
            ]

    @staticmethod
    def answer9_error_message(answer):
        if answer != 3:
            return [
                "At the end of the experiment, one of the 25 decision rounds "
                "will be selected at random to determine your earnings for "
                "the experiment. "
                "Each round is equally likely to be selected."
            ]
