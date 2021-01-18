from otree.api import (
    models,
    # widgets,
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

    answer1 = models.IntegerField()

    def answer1_error_message(self, answer):
        if answer!=10:
            return 'Answer is incorrect, please try again'

    answer2 = models.IntegerField()

    def answer2_error_message(self, answer):
        if answer!=20:
            return 'Answer is incorrect, please try again'

    answer3 = models.IntegerField()

    def answer3_error_message(self, answer):
        if answer!=1:
            return 'Answer is incorrect, please try again'

    answer4 = models.IntegerField()

    def answer4_error_message(self, answer):
        if answer!=25:
            return 'Answer is incorrect, please try again'

    answer8 = models.IntegerField()

    def answer8_error_message(self, answer):
        if answer!=1:
            return 'Answer is incorrect, please try again'

    answer9 = models.IntegerField()

    def answer9_error_message(self, answer):
        if answer!=4:
            return 'Answer is incorrect, please try again'