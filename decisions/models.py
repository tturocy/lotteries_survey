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


class MenuItem:
    def __init__(self, imagepath, lottery):
        self.imagepath = imagepath
        self.lottery = lottery

    def expected(self):
        return f"{self.lottery.mean():.2f}"

    def risk(self):
        return f"{self.lottery.std():.2f}"


class MenuSequence:
    def __init__(self, session, menu_seq, parity):
        self.session = session
        self.sequence = {period: menu
                         for (period, (menu,)) in menu_seq.iterrows()}
        self.parity = parity

    def get_menu(self, round_number):
        menu_number = self.get_menu_number(round_number)
        if round_number % 2 == self.parity:
            return [
                MenuItem(
                    f"decisions/lottery_p{menu_number}.jpg",
                    self.session.vars['lotteries'].loc[f"p{menu_number}"]
                ),
                MenuItem(
                    f"decisions/lottery_q{menu_number}.jpg",
                    self.session.vars['lotteries'].loc[f"q{menu_number}"]
                )
            ]
        else:
            return [
                MenuItem(
                    f"decisions/lottery_q{menu_number}.jpg",
                    self.session.vars['lotteries'].loc[f"q{menu_number}"]
                ),
                MenuItem(
                    f"decisions/lottery_p{menu_number}.jpg",
                    self.session.vars['lotteries'].loc[f"p{menu_number}"]
                )
            ]

    def get_menu_number(self, round_number):
        return self.sequence[round_number]


class Subsession(BaseSubsession):
    def creating_session(self):
        if 'lotteries' not in self.session.vars:
            self.session.vars['lotteries'] = (
                pd.read_csv("decisions/lotteries.csv",
                            index_col='roll')
                .transpose()
            )
        if self.round_number == 1:
            orderings = (
                pd.read_csv("decisions/orderings.csv",
                            index_col='period')
            )
            for (menu_seq, player) in enumerate(self.get_players()):
                player.participant.vars['menu_seq'] = (
                    MenuSequence(self.session,
                                 orderings[[str(menu_seq + 1)]],
                                 menu_seq % 2)
                )


class Group(BaseGroup):
    pass


class PlayerChoice:
    def __init__(self, item, roll):
        self.item = item
        self.roll = roll

    @property
    def payoff(self):
        return c(int(self.item.lottery[self.roll]))


class Player(BasePlayer):
    menu_number = models.IntegerField()
    lotterychoice = models.IntegerField()
    # Dice rolls are determined at subsession initialisation
    roll = models.IntegerField()

    def get_menu(self):
        return self.participant.vars['menu_seq'].get_menu(self.round_number)

    def process_decision(self):
        self.menu_number = self.participant.vars['menu_seq'].get_menu_number(self.round_number)
        self.roll = random.randint(1, 100)
        item = self.get_menu()[self.lotterychoice]
        if 'choices' not in self.participant.vars:
            self.participant.vars['choices'] = {}
        self.participant.vars['choices'][self.round_number] = (
            PlayerChoice(item, self.roll)
        )
