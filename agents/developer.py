import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def develop(requirement):

    prompt = f"""
You are a Senior Software Developer.

Project:
{requirement}

Return ONLY valid JSON.

{{
  "Frontend": [
    "Technology 1",
    "Technology 2"
  ],
  "Backend": [
    "Technology 1",
    "Technology 2"
  ],
  "Database": [
    "Database Technology"
  ]
}}
"""

    response = model.generate_content(prompt)

    text = response.text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)