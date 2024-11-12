from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the variables
print("Use these credentials to get stuff done:")
print("OpenAI Key:", os.getenv("OPENAI_API_KEY"))
print("Mapbox Access token:", os.getenv("MAPBOX_ACCESS_TOKEN"))
print("\n")

# Print line for line of the data.txt file
print("The following data is stored in the data.txt file for parsing")
with open('./data.txt', 'r') as file:
    for line in file:
        print(line.strip())
