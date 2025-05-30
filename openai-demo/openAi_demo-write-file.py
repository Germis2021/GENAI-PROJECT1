






import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables

#def write_joke_to_file(joke):

# from .env file
# Load the GitHub token from the environment variable
# Ensure you have a .env file with the following line:



token = os.getenv("SECRET")
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
            "content": "What is the capital of Latvia?",
        }
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
)

joke = response.choices[0].message.content


# Write the joke to a file
with open("joke.txt", "w") as file:
    file.write(joke)#type: ignore

