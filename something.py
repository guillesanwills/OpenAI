from openai import OpenAI
import os
from dotenv import load_dotenv
#from langchain_community.llms import OpenAI
from langchain_openai import OpenAI

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

#Create LLM model
llm = OpenAI(model_name = "gpt-3.5-turbo-instruct")

#a
query = "What is the capital of the United States?"
completion = llm(query)

print(completion)