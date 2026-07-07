import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def plan(requirement):

    prompt = f"""
You are a Software Project Manager.

Project:
{requirement}

Return ONLY valid JSON.

{{
  "Timeline":"12 Weeks",
  "Modules":[
    "Module 1",
    "Module 2",
    "Module 3",
    "Module 4",
    "Module 5"
  ]
}}
"""

    response = model.generate_content(prompt)

    text = response.text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)