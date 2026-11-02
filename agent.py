import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

from weather_tool import get_weather
from tool_definition import weather_tool
from system_prompt import SYSTEM_PROMPT

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-3.1-flash-lite"
MAX_STEPS = 5

TOOL_FUNCTIONS = {
    "get_weather": get_weather,
}

config = types.GenerateContentConfig(
    system_instruction=SYSTEM_PROMPT,
    tools=[weather_tool],
)


def run_agent(question):
    """Answer one question, using tools if Gemini asks for them."""
    contents = [
        types.Content(role="user", parts=[types.Part(text=question)])
    ]
    tools_used = []

    for step in range(MAX_STEPS):
        response = client.models.generate_content(
            model=MODEL,
            contents=contents,
            config=config,
        )

        if not response.function_calls:
            return response.text, tools_used

        contents.append(response.candidates[0].content)

        result_parts = []
        for call in response.function_calls:
            print(f"   [tool requested: {call.name}]")
            tools_used.append(call.name)

            function = TOOL_FUNCTIONS.get(call.name)
            if function is None:
                result = {"error": f"Unknown tool: {call.name}"}
            else:
                result = function(**(call.args or {}))

            result_parts.append(
                types.Part.from_function_response(
                    name=call.name,
                    response={"result": result},
                )
            )

        contents.append(types.Content(role="user", parts=result_parts))

    return "Sorry, I could not finish answering that. Please try again.", tools_used


if __name__ == "__main__":
    question = input("Ask the harvest advisor: ")
    print()
    answer, _ = run_agent(question)
    print(answer)