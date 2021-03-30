import django.forms.widgets

from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    # currency_range,
)


author = 'Prachi Hejib'

doc = "Numeracy inventory"


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class CurrencyInput(django.forms.widgets.NumberInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render(self, *args, **kwargs):
        return (
            '<div class="input-group">'
            '<span class="input-group-text">£</span>'
            f'{super().render(*args, **kwargs)}'
            '</div>'
        )


questions = [
    {
        'text': (
            "In a sale, a shop is selling all items at half price. "
            "Before the sale, a sofa costs £300. "
            "How much will it cost during the sale?"
        ),
        'answer': 150
    },
    {
        'text': (
            "If the chance of getting a disease is 10 per cent, "
            "how many people out of 1000 would be expected to get the disease?"
        ),
        'answer': 100
    },
    {
        'text': (
            "A second hand car dealer is selling a car for £6000. "
            "This is two-thirds of what it cost new. "
            "How much did the car cost new?"
        ),
        'answer': 9000
    },
    {
        'text': (
            "If 5 people all have the winning numbers in the lottery "
            "and the prize is £2 million, how much will each of them get?"
        ),
        'answer': 400000
    },
    {
        'text': (
            "Let's say you have £200 in a savings account. "
            "The account earns ten per cent interest per year. "
            "How much will you have in the account at the end of two years?"
        ),
        'answer': 242
    },
    {
        'text': (
            "Imagine that the interest rate on your savings account "
            "was 1% per year and inflation was 2% per year. "
            "After 1 year, how much would you be able to buy with the money "
            "in this account?"
        ),
        'choices': [
            [1, "More than today"],
            [2, "Exactly the same as today"],
            [3, "Less than today"],
        ],
        'answer': 3,
    },
    {
        'text': (
            "Suppose that in the year 2030, your income has doubled and "
            "prices of all goods have doubled too. In 2030, "
            "how much will you be able to buy with your income?"
        ),
        'choices': [
            [1, "More than today"],
            [2, "Exactly the same as today"],
            [3, "Less than today"],
        ],
        'answer': 2,
    }
]


class Player(BasePlayer):
    answer1 = models.IntegerField(
        label=questions[0]['text'],
        widget=CurrencyInput
    )
    answer2 = models.IntegerField(
        label=questions[1]['text'],
    )
    answer3 = models.IntegerField(
        label=questions[2]['text'],
        widget=CurrencyInput
    )
    answer4 = models.IntegerField(
        label=questions[3]['text'],
        widget=CurrencyInput
    )
    answer5 = models.IntegerField(
        label=questions[4]['text'],
        widget=CurrencyInput
    )
    answer6 = models.IntegerField(
        label=questions[5]['text'],
        choices=questions[5]['choices'],
        widget=widgets.RadioSelect
    )
    answer7 = models.IntegerField(
        label=questions[6]['text'],
        choices=questions[6]['choices'],
        widget=widgets.RadioSelect
    )

    def get_answers(self):
        """Return the answers as a list"""
        return [self.answer1, self.answer2, self.answer3, self.answer4,
                self.answer5, self.answer6, self.answer7]

    def get_scores(self):
        """Return earnings per question."""
        return [
            c(1.00) if q['answer'] == p else c(0.00)
            for (p, q) in zip(self.get_answers(), questions)]

    def process_answers(self):
        self.participant.payoff += sum(self.get_scores())
