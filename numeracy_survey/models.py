from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'numeracy_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    answer1 = models.IntegerField()

    def answer1_error_message(self, answer):
        if answer != 150:
            return 'Answer is incorrect, please try again'

    answer2 = models.IntegerField()

    def answer2_error_message(self, answer):
        if answer != 100:
            return 'Answer is incorrect, please try again'

    answer3 = models.IntegerField()

    def answer3_error_message(self, answer):
        if answer != 9000:
            return 'Answer is incorrect, please try again'

    answer4 = models.IntegerField()

    def answer4_error_message(self, answer):
        if answer != 400000:
            return 'Answer is incorrect, please try again'

    answer5 = models.IntegerField()

    def answer5_error_message(self, answer):
        if answer != 242:
            return 'Answer is incorrect, please try again'

    answer6 = models.IntegerField()

    def answer6_error_message(self, answer):
        if answer != 1:
            return 'Answer is incorrect, please try again'

    answer7 = models.IntegerField()

    def answer7_error_message(self, answer):
        if answer != 1:
            return 'Answer is incorrect, please try again'