import openai
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_caption(caption: str) -> str:

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = f"Summarize this Instagram caption into a tweet (max 280 characters): {caption}"
    response = model.generate_content(prompt)
    print(response)

    if response.candidates:
        first_candidate = response.candidates[0]
        if first_candidate.content.parts:
            print(first_candidate.content.parts[0].text.strip())
            return first_candidate.content.parts[0].text.strip()

    return str(response.text)
