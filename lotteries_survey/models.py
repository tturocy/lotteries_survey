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


author = 'Prachi Hejib'

doc = "Lotteries_survey"
"Investment decisions modelled as lottery choices"


class Constants(BaseConstants):
    name_in_url = 'lotteries_survey'
    players_per_group = None
    num_rounds = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    @property
    def lottery_image_A(self):
        return f"lotteries_survey/lottery_{self.round_number}_A.jpg"

    @property
    def lottery_image_B(self):
        return f"lotteries_survey/lottery_{self.round_number}_B.jpg"


class Player(BasePlayer):
    lotterychoice = models.StringField(
        label= "Which lottery do you prefer?",
        choices=["Lottery A", " Lottery B"],
        widget=widgets.RadioSelect)

