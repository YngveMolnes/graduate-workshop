# Setting up env

`python3 -m venv venv`
`source venv/bin/activate`
`pip install pydantic instructor openai python-dotenv`
or
`pip install -r requirements.txt`

Put the API keys in a `.env` file in the root directory. It should follow the format of `.env.example`

# Running script

Ensure `source venv/bin/activate` has been run first.

Run `python3 main.py`


# The task
1. Make a pydantic type that that has one or more locations, a description, and
   one or more urls.
2. Parse the strings in data.txt (mimicking tweets) into the type you just
   defined using instructor
3. BONUS#1: Use the mapbox Geocoding API to get the exact location for the
   location. Extend the pydantic type(s) to include this data.
4. BONUS#2: Implement Geocoding API calls as LLM-function calls.

# Happy coding (-:

Any tools / help is allowed, be it LLMs, web searches or whatever. This is not
an exam, but an opportunity to learn these tools.