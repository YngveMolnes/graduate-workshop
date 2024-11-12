from dotenv import load_dotenv
import os
from typing import List
from pydantic import BaseModel, HttpUrl
import requests
import instructor
from openai import OpenAI
# Load environment variables from the .env file
load_dotenv()

# Patch OpenAI client with instructor
client = instructor.from_openai(OpenAI())

class GeocodedLocation(BaseModel):
    name: str
    latitude: float
    longitude: float

class Tweet(BaseModel):
    locations: List[GeocodedLocation]
    description: str
    urls: List[HttpUrl]

def geocode_location(location: str) -> GeocodedLocation:
    """Geocode a location string using Mapbox API"""
    base_url = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    params = {
        "access_token": os.getenv("MAPBOX_ACCESS_TOKEN"),
        "limit": 1
    }

    response = requests.get(f"{base_url}/{location}.json", params=params)
    data = response.json()

    if data["features"]:
        feature = data["features"][0]
        return GeocodedLocation(
            name=location,
            longitude=feature["center"][0],
            latitude=feature["center"][1]
        )
    return GeocodedLocation(name=location, latitude=0, longitude=0)

def parse_tweet(tweet_text: str) -> Tweet:
    """Parse tweet text into Tweet model using LLM"""
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=Tweet,
        messages=[{
            "role": "user",
            "content": f"Extract locations, description and URLs from this tweet: {tweet_text}"
        }]
    )

# Read and parse tweets
with open('./data.txt', 'r') as file:
    tweets = []
    for line in file:
        tweet = parse_tweet(line.strip())
        # Geocode all locations
        tweet.locations = [geocode_location(loc.name) for loc in tweet.locations]
        tweets.append(tweet)
        # Print transformed data
        print("Tweet:")
        print(tweet.model_dump())
        print()
