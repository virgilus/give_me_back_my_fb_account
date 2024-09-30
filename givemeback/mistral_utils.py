import os
from mistralai import Mistral

from givemeback import c, credentials

MISTRAL_KEY = credentials['MISTRAL_KEY']

def ask_mistral(prompt="Hey, what are you ?"):
    model = "mistral-large-latest"
    client = Mistral(api_key=MISTRAL_KEY)

    chat_response = client.chat.complete(
        model = model,
        messages = [
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )

    print(chat_response.choices[0].message.content)
    return chat_response