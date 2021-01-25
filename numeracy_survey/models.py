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

doc = "Lotteries_survey"
"Investment decisions modelled as lottery choices"


class Constants(BaseConstants):
    name_in_url = 'numeracy_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    answer1 = models.IntegerField(
        label="In a sale, a shop is selling all items at half price. Before the sale, a sofa costs $300. How much will it cost in the sale?"
    )
    answer2 = models.IntegerField(
        label="If the chance of getting a disease is 10 per cent, "
              "how many people out of 1,000 would be expected to get the disease?"
    )
    answer3 = models.IntegerField(
        label="A second hand car dealer is selling a car for $6,000. "
              "This is two-thirds of what it cost new. How much did the car cost new?"
    )
    answer4 = models.IntegerField(
        label="If 5 people all have the winning numbers in the lottery "
              "and the prize is $2 million, how much will each of them get?"
    )
    answer5 = models.IntegerField(
        label="Let’s say you have $200 in a savings account. "
              "The account earns ten per cent interest per year. "
              "How much will you have in the account at the end of two years?"
    )
    answer6 = models.IntegerField(
        label="Imagine that the interest rate on your savings account "
              "was 1% per year and inflation was 2% per year. "
              "After 1 year, how much would you be able to buy with the money "
              "in this account? More than today, exactly the same as today, or less than today?"
    )
    answer7 = models.IntegerField(
        label="Suppose that in the year 2020, your income has doubled and "
              "prices of all goods have doubled too. In 2020, "
              "how much will you be able to buy with your income? "
              "More than today, exactly the same as today, or less than today?"
    )
