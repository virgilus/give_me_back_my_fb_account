from os.path import join, dirname
from yaml import safe_load

# Loading config
# So all your modules have access to the same variables

CONFIG_PATH = join(dirname(dirname(__file__)), 'config.yaml')
with open(CONFIG_PATH, 'rb') as file:
    c = safe_load(file) # c is now a global dict config

SECRETS_PATH = join(dirname(dirname(__file__)), 'secrets/credentials.yaml')
with open(SECRETS_PATH, 'rb') as file:
    credentials = safe_load(file) # credentials is now a global dict config

PROMPTS_PATH = join(dirname(dirname(__file__)), 'prompts/atp_prompts.yaml')
with open(PROMPTS_PATH, 'rb') as file:
    p = safe_load(file) # credentials is now a global dict config