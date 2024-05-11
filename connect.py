from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
  api_key = os.getenv("OPEN_API_KEY"),
  organization='org-xZJB52SQV2aw111S37z0NZy6',
  project='proj_GmInn6mPCJSlTsrJ394sqAck',
)
print(client.models())
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")