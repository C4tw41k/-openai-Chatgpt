# Note: you need to be using OpenAI Python v0.27.0 for the code below to work

import os
import openai
openai.organization = "org-DZn6MOgACWIbxxYLzuk2MdHz" #填你自己的OpenAI-Organization，这里获得：https://platform.openai.com/account/org-settings
openai.api_key = os.getenv("OPENAI_API_KEY") #填你自己的api_key，这里获得：https://platform.openai.com/account/api-keys
openai.Model.list()


map=[]
user = {"role": "user", "content": ""}
system = {"role": "system", "content": ""}
user["content"] = input('请问您想了解什么？\n')

while True:
    map.append(user)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = map
    )
    
    re = response['choices'][0]['message']['content']
    
    re.encode('unicode_escape').decode('utf-8')

    print(re + "\n")

    system["content"] = re

    map.append(system)

    user = {"role": "user", "content": ""}
    system = {"role": "system", "content": ""}

    


    user["content"] = input()