# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

import os
import openai
openai.organization = "org-DZxxxxxxxxxxxxxxdHz" #填你自己的OpenAI-Organization，这里获得：https://platform.openai.com/account/org-settings
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxWt2zEs" #填你自己的api_key，这里获得：https://platform.openai.com/account/api-keys
openai.Model.list()

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[

    {"role": "user", "content": '帮我写一段话，向我朋友问好'}

  ]
)

re = response['choices'][0]['message']['content']

re.encode('unicode_escape').decode('utf-8')
print(re)