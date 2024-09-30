from givemeback import c, p
import givemeback.tweeter_utils as tu
import givemeback.mistral_utils as mu

if __name__ == "__main__":
    print(c)
    # tu.post('Hi, this an other API test, will it show up now?')
    mu.ask_mistral(p[1])