from langchain_community.llms import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2")

# The LLM takes a prompt as an input and outputs a completion
our_query = "What is the currency of India?"

#Submit prompt to the LLM
completion = llm.invoke(our_query)
print("\nResponse:", completion)