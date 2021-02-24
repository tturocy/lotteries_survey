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


class Player(BasePlayer):
    answer1 = models.IntegerField(
        label="How much would you earn if ball number 38 was drawn?"
    )
    answer2 = models.IntegerField(
        label="How much would you earn if a ball number between 61 and 100 was drawn?"
    )
    answer3 = models.IntegerField(
        label="Is it it more likely that ball number 4 is drawn than 27 ?",
        choices = [
            [1, "yes, 4 is more likely"],
            [2, "no, 27 is more likely"],
            [3, "no, both 4 and 27 are equally likely to be drawn"],
              ],
              widget = widgets.RadioSelect
    )
    answer4 = models.IntegerField(
        label="How many balls out of 100 allow you to earn £10 if they were drawn?"
    )
    answer8 = models.IntegerField(
        label="How many rounds will be selected for payment?"
    )
    answer9 = models.IntegerField(
        label="How likely is a round to be selected for payment?",
        choices = [
            [1, "1/25"],
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