import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze(requirement):

    prompt = f"""
You are a Software Requirement Analyst.

Project:
{requirement}

Return ONLY valid JSON.
Keep every point short.
Maximum 5 words per point.

{{
"Functional Requirements":[
"...",
"...",
"...",
"...",
"..."
],
"Non Functional Requirements":[
"...",
"...",
"...",
"...",
"..."
]
}}
"""

    response = model.generate_content(prompt)

    text = response.text.replace("```json","").replace("```","").strip()

    return json.loads(text)
    report lab