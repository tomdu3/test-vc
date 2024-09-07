# code from Rapid Api
import requests
import pprint
from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env


API_KEY = os.environ.get("API_KEY", 'Something went wrong')

print(API_KEY)

url = "https://imdb146.p.rapidapi.com/v1/find/"

querystring = {"query":"Die Hard"}

headers = {
	"X-RapidAPI-Key": os.environ.get("API_KEY"),  # insert your API key
	"X-RapidAPI-Host": "imdb146.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

pprint.pprint(response.json())