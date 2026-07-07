import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def test(requirement):

    prompt = f"""
You are a Software QA Tester.

Project:
{requirement}

Return ONLY valid JSON.

{{
"Test Cases":[
"Test Case 1",
"Test Case 2",
"Test Case 3",
"Test Case 4",
"Test Case 5"
]
}}
"""

    response = model.generate_content(prompt)

    text = response.text.replace("```json","").replace("```","").strip()

    return json.loads(text)