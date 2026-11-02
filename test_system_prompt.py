import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from system_prompt import SYSTEM_PROMPT

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)

test_cases = [
    ("GOOD", "Weather data: 21C, humidity 55%, not raining now, 0 mm rain in the next 6 hours."),
    ("BAD", "Weather data: 23C, humidity 90%, raining now, 6 mm rain in the next 6 hours."),
    ("HOT", "Weather data: 30C, humidity 50%, not raining now, 0 mm rain in the next 6 hours."),
    ("MIDDLE", "Weather data: 27C, humidity 65%, not raining now, 0 mm rain in the next 6 hours."),
]

for label, fake_weather in test_cases:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"Is today good for harvesting? {fake_weather}",
        config=config,
    )
    print(f"[{label}] {response.text}\n")