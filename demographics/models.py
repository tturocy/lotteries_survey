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
    name_in_url = 'aboutyou'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(
        label="What gender do you identify as?",
        choices=[
            [1, "Male"],
            [2, "Female"],
            [3, "Other"],
            [4, "Prefer not to say"]
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    age = models.IntegerField(
        label="How old are you?",
        blank=True,
    )

    countryborn = models.StringField(
        label="Which country (or countries) were you a citizen of when you were born?",
        blank=True,
    )

    countrynow = models.StringField(
        label="In which country is your current permanent residence? "
              "(If you are in the UK on a student visa, this is the country where 'home' is.)",
        blank=True,
    )

    department = models.StringField(
        label="In which School are you currently enrolled? (For example, BIO, ECO, EDU, ...)",
        blank=True,
    )

    degree = models.IntegerField(
        label="What type of degree course are you currently enrolled on?",
        choices=[
            [1, 'INTO'],
            [2, 'Bachelor'],
            [3, 'PG Diploma'],
            [4, 'Master'],
            [5, 'PhD'],
            [6, 'I am a member of staff'],
            [7, 'Other degree course or affiliation'],
            [8, 'Prefer not to say']
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    timeuea = models.IntegerField(
        label="How long have you been at UEA?",
        choices=[
            [1, "This is my first year"],
            [2, "This is my second year"],
            [3, "This is my third year"],
            [4, "This is my fourth year"],
            [5, "I have been here more than four years"],
            [6, "Prefer not to say"]
            ],
        widget=widgets.RadioSelect,
        blank=True,
    )
