from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .models import questions


class Instructions(Page):
    pass


class QuestionPage(Page):
    template_name = "numeracy/GeneralNumeracy.html"
    form_model = 'player'


class Question1(QuestionPage):
    form_fields = ['answer1']

    def vars_for_template(self):
        return {'question_number': 1}

class Question2(QuestionPage):
    form_fields = ['answer2']

    def vars_for_template(self):
        return {'question_number': 2}


class Question3(QuestionPage):
    form_fields = ['answer3']

    def vars_for_template(self):
        return {'question_number': 3}


class Question4(QuestionPage):
    form_fields = ['answer4']

    def vars_for_template(self):
        return {'question_number': 4}


class Question5(QuestionPage):
    form_fields = ['answer5']

    def vars_for_template(self):
        return {'question_number': 5}


class Question6(QuestionPage):
    form_fields = ['answer6']

    def vars_for_template(self):
        return {'question_number': 6}


class Question7(QuestionPage):
    form_fields = ['answer7']

    def vars_for_template(self):
        return {'question_number': 7}

    def before_next_page(self):
        self.player.process_answers()


class ResultsWaitPage(WaitPage):
    pass


class ResultsPage(Page):
    def vars_for_template(self):
        return {
            'questions': [
                {
                    'text': q['text'],
                    'correct': q['answer'],
                    'answer': p,
                    'earnings': s
                }
                for (p, q, s) in zip(self.player.get_answers(),
                                     questions,
                                     self.player.get_scores())
            ]
        }


page_sequence = [
    Instructions,
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6,
    Question7,
    ResultsWaitPage,
    ResultsPage
]
