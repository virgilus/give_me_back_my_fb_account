import os
from mistralai import Mistral

from givemeback import c, credentials

MISTRAL_KEY = credentials['MISTRAL_KEY']

def ask_mistral(prompt: str, api_key: str=MISTRAL_KEY) -> str:
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model = model,
        messages = [
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )

     #print(chat_response.choices[0].message.content)
    return chat_response.choices[0].message.content