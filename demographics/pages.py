from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class DemographicsIntro(Page):
    pass


class DemographicsPage1(Page):
    template_name = "Demographics/GeneralDemographics.html"
    form_model = 'player'
    form_fields = ['gender',
                   'genderother'
                   ]

class DemographicsPage2(Page):
    template_name = "Demographics/GeneralDemographics.html"
    form_model = 'player'
    form_fields = ['age']

class DemographicsPage3(Page):
    template_name = "Demographics/GeneralDemographics.html"
    form_model = 'player'
    form_fields = ['countryborn']

class DemographicsPage4(Page):
    template_name = "Demographics/GeneralDemographics.html"
    form_model = 'player'
    form_fields = ['countrynow']

class DemographicsPage5(Page):
    template_name = "Demographics/GeneralDemographics.html"
    form_model = 'player'
    form_fields = ['department']

class DemographicsPage6(Page):
    template_name = "Demographics/GeneralDemographics.html"
    form_model = 'player'
    form_fields = ['degree',
                   'degreeother',
                   ]

class DemographicsPage7(Page):
    template_name = "Demographics/GeneralDemographics.html"
    form_model = 'player'
    form_fields = ['timeuea']



page_sequence = [DemographicsIntro,
                 DemographicsPage1,
                 DemographicsPage2,
                 DemographicsPage3,
                 DemographicsPage4,
                 DemographicsPage5,
                 DemographicsPage6,
                 DemographicsPage7,
                 ]
