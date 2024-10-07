from givemeback import c, p, logging
import givemeback.tweeter_utils as tu
import givemeback.mistral_utils as mu

from random import randint, choice
from time import sleep

TIME_TO_SLEEP = c['TIME_TO_SLEEP']
RANDOM_TIME = c['RANDOM_TIME']
DRY_RUN_TWITTER = c['DRY_RUN_TWITTER']


if __name__ == "__main__":

    while True:
        text = mu.ask_mistral(choice(p))
        logging.info(f"Mistral text generated --->>>  {text}")
        tu.post(text, DRY_RUN_TWITTER)
        sleep(TIME_TO_SLEEP + randint(0, RANDOM_TIME))