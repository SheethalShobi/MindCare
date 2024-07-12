import os
from langchain.prompts import PromptTemplate
from langchain_together import Together
together_api_key='TOGETHER-API-KEY'
llm=Together(together_api_key=together_api_key,
             model='meta-llama/Meta-Llama-3-70B',
             tags=['mental-health'],
             temperature=0.9,
                )
anxiety_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="The user is feeling anxious. Respond empathetically and suggest a calming activity.\n\nUser: {user_input}\nBot:",
)
depression_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="The user is feeling depressed. Respond empathetically and offer support.\n\nUser: {user_input}\nBot:",
)

ptsd_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="The user is experiencing PTSD symptoms. Respond empathetically and suggest grounding techniques.\n\nUser: {user_input}\nBot:",
)
disease_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="The user is experiencing disease symptoms. Respond empathetically and suggest solutions.\n\nUser: {user_input}\nBot:",
)
def mental_health_chatbot(user_input1, issue_type):
    if issue_type == "anxiety":
        prompt=anxiety_prompt.format(user_input=user_input1)
        response = llm.generate(prompts=[prompt],tags=['anxiety'])
    elif issue_type == "depression":
        prompt=depression_prompt.format(user_input=user_input1)
        response = llm.generate(prompts=[prompt],tags=['depression'])
    elif issue_type == "ptsd":
        prompt=ptsd_prompt.format(user_input=user_input1)
        response = llm.generate(prompts=[prompt],tags= ['ptsd'])
    elif issue_type == "disease":
        prompt=disease_prompt.format(user_input=user_input1)
        response = llm.generate(prompts=[prompt],tags=['disease'])
    else:
        response = "I'm here to help. Can you tell me more about what you're experiencing?"
    return str(response.generations[0])
user_input=input('Enter your problem:')
issue_type=input('Enter your issue type:')
response = mental_health_chatbot(user_input, issue_type)
print(response[17:-1])
