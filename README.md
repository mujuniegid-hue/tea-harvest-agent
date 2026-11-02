# Tea Estate Harvest Advisor

A simple AI agent for a tea estate in Bushenyi, Uganda. The field supervisor
types a question each morning. If the question is about weather or harvesting,
the agent checks live weather and gives a practical recommendation.
Otherwise it answers directly.

## How it works

1. The supervisor asks a question.
2. Gemini decides whether it needs the `get_weather` tool.
3. If yes, the code calls the Open-Meteo weather API and returns the result.
4. Gemini reads the result and answers in plain language.

## Harvest rules (in the system prompt)

- Good: no rain in the next 6 hours, 15-25 C, low humidity
- Bad: rain now, or above 28 C
- Between: possible with caution

Note: "low humidity" was not defined, so below 70% is used as an assumption.

## Setup

1. Install Python 3 and create a virtual environment.
2. Run: `pip install google-genai requests python-dotenv`
3. Get a Gemini API key from Google AI Studio.
4. Create a `.env` file containing: `GEMINI_API_KEY=your_key_here`

## Run

    python agent.py

Run the tests:

    python test_agent.py

## Files

- `agent.py`: the agent loop
- `weather_tool.py`: fetches Bushenyi weather from Open-Meteo
- `tool_definition.py`: describes the tool to Gemini
- `system_prompt.py`: instructions and harvest rules
- `test_agent.py`: runs three test questions
- `test_results.md`: saved test output

## Limitations

- The location is fixed to Bushenyi.
- Free-tier Gemini limits can cause temporary errors.
- Three tests show basic behaviour only.