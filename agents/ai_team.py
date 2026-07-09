import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_project(requirement):

    prompt = f"""
You are an AI Software Development Team.

Project:
{requirement}

Return ONLY valid JSON.

{{
  "Functional Requirements":[
    "...","...","...","...","..."
  ],

  "Non Functional Requirements":[
    "...","...","...","...","..."
  ],

  "Timeline":"12 Weeks",

  "Modules":[
    "...","...","...","...","..."
  ],

  "Frontend":[
    "...","..."
  ],

  "Backend":[
    "...","..."
  ],

  "Database":[
    "..."
  ],

  "Test Cases":[
    "...","...","...","...","..."
  ],

  "Documents":[
    "...","...","...","...","..."
  ]
}}
"""

    response = model.generate_content(prompt)

    text = response.text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)