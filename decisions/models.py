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
    name_in_url = 'part1'
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
    def __init__(self, session, player):
        self.session = session
        rnd = random.Random(self.session.config['first_seed'] + player)
        menus = rnd.sample(range(1, 26), 25)
        self.sequence = {period + 1: menu
                         for (period, menu) in enumerate(menus)}
        self.order = {period: rnd.sample(['p', 'q'], 2)
                       for period in self.sequence.keys()}

    def get_menu(self, round_number):
        menu_number = self.sequence[round_number]
        order = self.order[round_number]
        return [
            MenuItem(
                f"decisions/lottery_{lottery_name}{menu_number}.jpg",
                self.session.vars['lotteries'].loc[f"p{menu_number}"]
            )
            for lottery_name in order
        ]


class Subsession(BaseSubsession):
    def creating_session(self):
        if 'lotteries' not in self.session.vars:
            self.session.vars['lotteries'] = (
                pd.read_csv("decisions/lotteries.csv",
                            index_col='roll')
                .transpose()
            )
        if self.round_number == 1:
            for (i, player) in enumerate(self.get_players()):
                player.participant.vars['menu_seq'] = (
                    MenuSequence(self.session, i)
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
        self.menu_number = self.participant.vars['menu_seq'].get_menu(self.round_number)
        self.roll = random.randint(1, 100)
        item = self.get_menu()[self.lotterychoice]
        if 'choices' not in self.participant.vars:
            self.participant.vars['choices'] = {}
        self.participant.vars['choices'][self.round_number] = (
            PlayerChoice(item, self.roll)
        )
