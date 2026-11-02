from google.genai import types

get_weather_declaration = types.FunctionDeclaration(
    name="get_weather",
    description=(
        "Get the current weather for the Bushenyi tea estate: temperature in "
        "Celsius, humidity percent, whether it is raining now, and expected "
        "rain over the next 6 hours. Use this when the user asks about "
        "weather, conditions, rain, or whether today is good for harvesting "
        "or other outdoor field work. Do not use it for general questions "
        "that do not depend on today's conditions."
    ),
)

weather_tool = types.Tool(function_declarations=[get_weather_declaration])