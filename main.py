from givemeback import c, p
import givemeback.tweeter_utils as tu
import givemeback.mistral_utils as mu

from time import sleep

if __name__ == "__main__":

    while True:
        text = mu.ask_mistral(p[1])
        print("Mistral text --->>>", text)
        tu.post(text)
        sleep(12)