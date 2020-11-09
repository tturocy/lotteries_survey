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


class MenuItem:
    def __init__(self, imagepath, lottery):
        self.imagepath = imagepath
        self.lottery = lottery

    def expected(self):
        return f"{self.lottery.mean():.2f}"

    def risk(self):
        return f"{self.lottery.std():.2f}"


class Group(BaseGroup):
    def get_menu(self):
        return [
            MenuItem(
                f"decisions/lottery_p{self.round_number}.jpg",
                self.session.vars['lotteries'].loc[f"p{self.round_number}"]
            ),
            MenuItem(
                f"decisions/lottery_q{self.round_number}.jpg",
                self.session.vars['lotteries'].loc[f"q{self.round_number}"]
            )
        ]


class PlayerChoice:
    def __init__(self, item, roll):
        self.item = item
        self.roll = roll

    @property
    def payoff(self):
        return c(int(self.item.lottery[self.roll]))


class Player(BasePlayer):
    lotterychoice = models.IntegerField()
    # Dice rolls are determined at subsession initialisation
    roll = models.IntegerField()

    def process_decision(self):
        self.roll = random.randint(1, 100)
        item = self.group.get_menu()[self.lotterychoice]
        if 'choices' not in self.participant.vars:
            self.participant.vars['choices'] = {}
        self.participant.vars['choices'][self.round_number] = (
            PlayerChoice(item, self.roll)
        )
