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

doc = """
Demographics Survey
"""


class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(
        choices = [
        [1, 'Male'],
        [2, 'Female'],
        [3, 'Other'],
        ],
        widget=widgets.RadioSelect
    )

    genderother = models.StringField(
        label="",
        blank = True,
    )

    age = models.IntegerField(
        label="",
    )

    countryborn = models.StringField(
        label="",
    )

    countrynow = models.StringField(
        label="",
    )

    department = models.StringField(
        label="",
    )

    degree = models.IntegerField(
        choices = [
            [1, 'INTO'],
            [2, 'Bachelor'],
            [3, 'PG Diploma'],
            [4, 'Master'],
            [5, 'PhD'],
            [6, 'Staff'],
            [7, 'Other'],
            ],
        widget=widgets.RadioSelect
    )

    degreeother = models.StringField(
        label="",
    )


    timeuea = models.IntegerField(
        label="",
    )