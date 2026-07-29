import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("openAI_API_KEY")
)

def generate_response(prompt: str) -> str:
    """
    send prompt to OpenAI LLM to return response.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    'role': "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"ERROR: {str(e)}"