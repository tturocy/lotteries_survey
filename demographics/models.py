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
        label="1.	What gender do you identify as?",
        choices = [
        [1, 'Male'],
        [2, 'Female'],
        [3, 'Other'],
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    genderother = models.StringField(
        label="If other please specify:",
        blank = True,
    )

    age = models.IntegerField(
        label="2.	How old are you?",
        blank=True,
    )

    countryborn = models.StringField(
        label="3.	Which country (or countries) were you a citizen of when you were born?",
        blank=True,
    )

    countrynow = models.StringField(
        label="4.	In which country is your current permanent residence? "
              "(If you are in the UK on a student visa, this is where “home” is.)",
        blank=True,
    )

    department = models.StringField(
        label="5.	In which School are you currently enrolled? (For example, BIO, ECO, EDU…)",
        blank=True,
    )

    degree = models.IntegerField(
        label="6.	What type of degree course are you currently enrolled on?",
        choices = [
            [1, 'INTO'],
            [2, 'Bachelor'],
            [3, 'PG Diploma'],
            [4, 'Master'],
            [5, 'PhD'],
            [6, 'Staff'],
            [7, 'Other'],
            ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    degreeother = models.StringField(
        label="If other please specify:",
        blank=True,
    )


    timeuea = models.IntegerField(
        label="7.	How long have you been at UEA?",
        choices=[
            [1, 'less than 1 year'],
            [2, '1-2 years'],
            [3, '2-3 years'],
            [4, '3-4 years'],
            [5, ' more than 4 years'],
            ],
            widget = widgets.RadioSelect,
        blank=True,
    )