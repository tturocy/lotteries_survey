from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

SESSION_CONFIGS = [
     dict(
         name='baseline',
         display_name="Baseline",
         num_demo_participants=1,
         app_sequence=[
             #'instructions',
             'decisions',
             #'numeracy',
             #'demographics',
             'endpage',
         ],
         show_expected=False,
         show_risk=False,
         first_seed=1000,
     ),
     dict(
         name='treatment_e',
         display_name="Treatment E",
         num_demo_participants=1,
         app_sequence=[
             'instructions',
             'decisions',
             'numeracy',
             'demographics',
             'endpage',
         ],
         show_expected=True,
         show_risk=False,
         first_seed=1000,
     ),
     dict(
         name='treatment_r',
         display_name="Treatment R",
         num_demo_participants=1,
         app_sequence=[
             'instructions',
             'decisions',
             'numeracy',
             'demographics',
             'endpage',
         ],
         show_expected=False,
         show_risk=True,
         first_seed=1000,
     ),
     dict(
         name='treatment_er',
         display_name="Treatment ER",
         num_demo_participants=1,
         app_sequence=[
             'instructions',
             'decisions',
             'numeracy',
             'demographics',
             'endpage',
         ],
         show_expected=True,
         show_risk=True,
         first_seed=1000,
     ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'oz^0n!db3v6r3%92vdm-m=cm4-il00+g17^7=4=e@tf5w89@k_'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
