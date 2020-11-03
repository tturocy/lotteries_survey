import random
from otree.api import (
    models,
    # widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    # currency_range,
)
import pandas as pd


author = 'Prachi Hejib'

doc = "Lotteries_survey"
"Investment decisions modelled as lottery choices"


class Constants(BaseConstants):
    name_in_url = 'ph1'
    players_per_group = None
    num_rounds = 2


class Subsession(BaseSubsession):
    def creating_session(self):
        if 'lotteries' not in self.session.vars:
            self.session.vars['lotteries'] = (
                pd.read_csv("decisions/lotteries.csv",
                            index_col='roll')
                .transpose()
            )


class Group(BaseGroup):
    pass


class PlayerChoice:
    def __init__(self, lottery, roll, imagepath):
        self.lottery = lottery
        self.roll = roll
        self.imagepath = imagepath

    @property
    def payoff(self):
        return c(int(self.lottery[self.roll]))


class Player(BasePlayer):
    lotterychoice = models.IntegerField()
    # Dice rolls are determined at subsession initialisation
    roll = models.IntegerField()

    def process_decision(self):
        self.roll = random.randint(1, 100)
        choice = ["p", "q"][self.lotterychoice]
        lottery = (
            self.session.vars['lotteries'].loc[f"{choice}{self.round_number}"]
        )
        if 'choices' not in self.participant.vars:
            self.participant.vars['choices'] = {}
        self.participant.vars['choices'][self.round_number] = (
            PlayerChoice(lottery, self.roll,
                         f"decisions/lottery_{choice}{self.round_number}.jpg")
        )
