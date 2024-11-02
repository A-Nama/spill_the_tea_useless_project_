import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def dramatize_text(text, drama_level):
    prompt = f"Make the following story more dramatic based on the level {drama_level}:\n{text}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()
