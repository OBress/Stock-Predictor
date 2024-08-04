import os
import requests
from datetime import datetime


class Bing:

    def __init__(self, subscription_key):
        self.subscription_key = subscription_key
        self.endpoint = 'https://api.bing.microsoft.com/v7.0/search'

    def scan(self, query, output_location):

        # Construct a request
        params = {
            'q': query,
            'mkt': 'en-US',
            'freshness': 'Day',  # Filter for posts within the last 24 hours
            'count': 50          # Maximum # results to return
        }

        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }

        # Call the API
        try:
            response = requests.get(self.endpoint, headers=headers, params=params)
            response.raise_for_status()
            
            json_response = response.json()
            
            with open(output_location, 'w', encoding='utf8') as file:
                for idx, result in enumerate(json_response.get('webPages', {}).get('value', []), start=1):
                    name = result.get('name')
                    url = result.get('url')
                    snippet = result.get('snippet', 'No summary.')
                    file.write(f"{idx}. {name}\n   {url}\n   Summary: {snippet}\n\n")
            
            print(f"Results saved to {output_location}")

        except Exception as ex:
            print(f"An error occurred: {ex}")
