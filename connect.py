from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#Create client
client = OpenAI(
  api_key = os.getenv("OPEN_API_KEY"),
  organization='org-xZJB52SQV2aw111S37z0NZy6',
  project='proj_GmInn6mPCJSlTsrJ394sqAck',
)

#List models available
models_response = client.models.list()
print("Available Models:", models_response)

#Not executable because it exceeds quota
stream = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")