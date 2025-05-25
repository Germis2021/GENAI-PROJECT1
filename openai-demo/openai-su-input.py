#You will practice Openai Python client usage:
# -- Advanced, optional
# 8. Update this script to be a console application, 
# where you can enter a question and AI would give you an answer.
# 9. Force AI to always answer in Lithuanian language.
# 10. If 'exit' command is given, exit the application instead of calling ai.
# 11. Whole conversation should be taken into context.

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Paimamos reikšmės iš .env failo

token = os.getenv("SECRET")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

print("Uzduok savo klausima (Jei nori išeiti spausk'exit' arba 'quit' ):")

while True:
    user_question = input("Tu: ")

    if user_question.lower() in ["exit", "quit"]:
        print("Iki!")
        break

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": user_question + " (Please answer in Lithuanian.)",
            }
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )

    print("Asistentas:", response.choices[0].message.content)


