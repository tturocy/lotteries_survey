from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Demographics1(Page):
    form_model = 'player'
    form_fields = ['gender',
                   'genderother',
                   'age',
                   'countryborn',
                   'countrynow',
                   'department',
                   'degree',
                   'degreeother',
                   'timeuea',
                   ]


class Demographics2(Page):
    pass


class Results(Page):
    pass


page_sequence = [Demographics1,
                 Demographics2,
                 ]
