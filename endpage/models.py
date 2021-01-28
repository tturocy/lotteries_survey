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


author = 'Prachi Hejib'

doc = """
Summary page for payments
"""


class Constants(BaseConstants):
    name_in_url = 'endpage'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def realise_paid_period(self):
        print("Realising paid period")
        for player in self.get_players():
            player.realise_paid_period()


class Player(BasePlayer):
    paid_period = models.IntegerField()

    def realise_paid_period(self):
        self.paid_period = random.randint(
            1, len(self.participant.vars['choices'])
        )
        self.participant.payoff += (
            self.participant.vars['choices'][self.paid_period].payoff
        )
