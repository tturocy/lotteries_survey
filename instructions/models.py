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

doc = "Lotteries_survey"
"Investment decisions modelled as lottery choices"


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
        label="Is it it more likely that ball number 4 is drawn than ball number 27?",
        choices = [
            [1, "Yes, 4 is more likely"],
            [2, "No, 27 is more likely"],
            [3, "No, both 4 and 27 are equally likely to be drawn"],
        ],
        widget = widgets.RadioSelect
    )
    answer4 = models.IntegerField(
        label="Of the 100 balls, how many of them would result in you earning £10 if drawn?"
    )
    answer8 = models.IntegerField(
        label="How many rounds will be selected for payment?"
    )
    answer9 = models.IntegerField(
        label="How likely is it that a given round will be selected for payment?",
        choices = [
            [1, "A 1 in 25 chance"],
            [2, "4%"],
            [3, "All rounds are equally likely to be selected"],
            [4, "All of the above"]
        ],
        widget = widgets.RadioSelect
    )

    def answer1_error_message(self, answer):
        if answer != 10:
            return [
                f"Your earnings in this case would not be £{answer}.",
                f"Look again at the bar."
            ]

    def answer2_error_message(self, answer):
        if answer != 20:
            return (
                f"Your earnings in this case would not be {answer}. "
                f"Look again at the bar."
            )


    def answer3_error_message(self, answer):
        if answer!=3:
            return 'Answer is incorrect, please try again'


    def answer4_error_message(self, answer):
        if answer!=25:
            return 'Answer is incorrect, please try again'


    def answer8_error_message(self, answer):
        if answer!=1:
            return 'Answer is incorrect, please try again'


    def answer9_error_message(self, answer):
        if answer!=4:
            return 'Answer is incorrect, please try again'