import openai
import os

<<<<<<< HEAD
# Set up API key from environment variables
openai.api_key = os.getenv("your_openai_api_key")
=======
openai.api_key = os.getenv('OPENAI_API_KEY')
>>>>>>> 0d76a77bbe6c40bded660cbead1c0d3a027768c6

def dramatize_text(text, drama_level):
    messages = [
        {"role": "system", "content": "You are a creative writer who dramatizes stories."},
        {"role": "user", "content": f"Make the following story more dramatic based on the level {drama_level}:\n{text}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=300
    )
    return response.choices[0].message['content'].strip()
