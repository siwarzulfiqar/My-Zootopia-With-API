import requests
import os
from dotenv import load_dotenv

# load the API key from the .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')  # this fetches the API key from the .env file

def fetch_data(animal_name):
    """Fetches the animal data from the API."""

    # construct the URL with the animal name
    url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'

    # use the API_KEY variable loaded from the .env file
    headers = {
        'X-Api-Key': API_KEY
    }

    try:
        # send the GET request to the API
        response = requests.get(url, headers=headers)

        # check if the request was successful
        if response.status_code == 200:
            return response.json()  # return JSON response
        else:
            print(f"Error: Unable to fetch data (HTTP {response.status_code}).")
            return []  # return an empty list if the request fails
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []  # return an empty list if there is a network or request error
