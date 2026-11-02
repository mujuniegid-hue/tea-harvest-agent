import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from tool_definition import weather_tool

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

config = types.GenerateContentConfig(tools=[weather_tool])

questions = [
    "Is today good for harvesting?",
    "What does plucking mean in tea farming?",
    "Give me one tip for training new pluckers.",
]

for question in questions:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=question,
        config=config,
    )

    if response.function_calls:
        call = response.function_calls[0]
        print(f"Q: {question}")
        print(f"   -> Gemini wants the tool: {call.name} (args: {call.args})\n")
    else:
        print(f"Q: {question}")
        print(f"   -> No tool needed. Answer: {response.text}\n")