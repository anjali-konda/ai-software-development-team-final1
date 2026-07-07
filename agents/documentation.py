import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def document(requirement):

    prompt = f"""
You are a Software Documentation Expert.

Project:
{requirement}

Return ONLY valid JSON.

{{
"Documents":[
"Software Requirement Specification (SRS)",
"System Design Document",
"Database Design Document",
"Test Plan",
"User Manual"
]
}}
"""

    response = model.generate_content(prompt)

    text = response.text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)