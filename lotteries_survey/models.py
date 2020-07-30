import random
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
import pandas as pd


author = 'Prachi Hejib'

doc = "Lotteries_survey"
"Investment decisions modelled as lottery choices"


class Constants(BaseConstants):
    name_in_url = 'lotteries_survey'
    players_per_group = None
    num_rounds = 2


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.roll = random.randint(1, 100)
        if 'lotteries' not in self.session.vars:
            self.session.vars['lotteries'] = (
                pd.read_csv("lotteries_survey/lotteries.csv",
                            index_col='roll')
                .transpose()
            )


class Group(BaseGroup):
    @property
    def lottery_image_A(self):
        return f"lotteries_survey/lottery_p{self.round_number}.jpg"

    @property
    def lottery_image_B(self):
        return f"lotteries_survey/lottery_q{self.round_number}.jpg"


class Player(BasePlayer):
    lotterychoice = models.StringField()
    # Dice rolls are determined at subsession initialisation
    roll = models.IntegerField()



