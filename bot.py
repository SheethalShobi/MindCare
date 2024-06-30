import os
import requests
from langchain.prompts import PromptTemplate
from langchain_together import Together

# Set your Together AI API key
together_api_key = '85bfb42456ec12dbaf0efa48b8bf1ed3c12816340cc98c685862a8dea0ba27cc'
llm = Together(together_api_key=together_api_key, model='meta-llama/Meta-Llama-3-70B')

# Define the prompts for different mental health support scenarios
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

def fetch_disease_info(disease_name):
    """
    Fetch information about a disease from Wikipedia.
    """
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{disease_name}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        title = data['title']
        extract = data['extract']
        return f"Title: {title}\n\nDescription: {extract}"
    except requests.exceptions.RequestException as e:
        return f"Sorry, I couldn't fetch information about {disease_name}. Please try again later."

# Function to handle user input and route to appropriate prompt or fetch disease info
def mental_health_chatbot(user_input1, issue_type):
    if issue_type == "anxiety":
        prompt = anxiety_prompt.format(user_input=user_input1)
        response = llm.generate(prompts=[prompt], max_tokens=200)
    elif issue_type == "depression":
        prompt = depression_prompt.format(user_input=user_input1)
        response = llm.generate(prompts=[prompt], max_tokens=200)
    elif issue_type == "ptsd":
        prompt = ptsd_prompt.format(user_input=user_input1)
        response = llm.generate(prompts=[prompt], max_tokens=200)
    else:
        # Fetch information about the disease
        response = fetch_disease_info(issue_type)
    return response

# Function to start the interactive chatbot
def start_chatbot():
    print("Hello! I'm here to help you with any mental health concerns or information about diseases.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! Take care.")
            break
        issue_type = input("What type of issue are you experiencing (anxiety, depression, ptsd) or enter a disease name for information? ")
        response = mental_health_chatbot(user_input, issue_type)
        print(f"Bot: {response}")
        continue_chat = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_chat != "yes":
            print("Goodbye! Take care.")
            break

# Start the interactive chatbot
start_chatbot()
