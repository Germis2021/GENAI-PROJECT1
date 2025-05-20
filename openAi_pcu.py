#You will practice Openai Python client usage:

#1. Please create a public Github repository for this projects.
#2. Ensure .gitignore (for Python)is added.
#3. Ensure you have a Github user created.
#4. Go to https://github.com/marketplace/models and copy the usage code to your repo.
#5. Ensure python-dotenv and openai are installed.
#5.2 Create a Github Classic access token.
#6. Add .env with SECRET key. (ensure you .env is not being committed).
#7. Test that everything works.

import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables

# from .env file
# Load the GitHub token from the environment variable
# Ensure you have a .env file with the following line:



token = os.environ["SECRET"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"



client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
)

print(response.choices[0].message.content)

