# Create an AI application which would read information from file and would answer a question about Birzai.

# 1. Load data as string from birzai.txt (u can change to your hometown)
# 2. Setup openai client.
# 3. Make a completion with openai client and pass the question and context in the completion.
# 4. Print the answer.




import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Paimamos reikšmės iš .env failo

with open("birzai.txt", "r", encoding="utf-8") as file:
    birzai_info = file.read()

print(birzai_info)



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
    




    



