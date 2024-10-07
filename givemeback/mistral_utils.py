import os
from mistralai import Mistral

from givemeback import c, credentials, logging

MISTRAL_KEY = credentials['MISTRAL_KEY']
TWITTER_CHARACTERS_LIMIT = c['TWITTER_CHARACTERS_LIMIT']

def ask_mistral(prompt: str, api_key: str=MISTRAL_KEY) -> str:
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model = model,
        messages = [{
                      "role": "user",
                      "content": prompt,
                  },]
                                        )
    tweet = chat_response.choices[0].message.content

    if tweet[0]  ==  '"': tweet = tweet[1:]
    if tweet[-1] ==  '"': tweet = tweet[:-1]

    tweet_len = len(tweet)
    if tweet_len > TWITTER_CHARACTERS_LIMIT:
        logging.critical(f'String too long ({tweet_len} characters where as limit is {TWITTER_CHARACTERS_LIMIT}). Generating a new one.')
        ask_mistral(prompt, MISTRAL_KEY)
    return tweet