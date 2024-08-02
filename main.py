import json
import os 
from pprint import pprint
import requests
from os import environ as env
from dotenv import load_dotenv
load_dotenv()

# Add your Bing Search V7 subscription key and endpoint to your environment variables.
subscription_key = env['BING_SEARCH_V7_SUBSCRIPTION_KEY']
endpoint = env['BING_SEARCH_V7_ENDPOINT'] + "v7.0/search"

# Query term(s) to search for. 
query = "CNN news"

# Construct a request
mkt = 'en-US'
params = { 'q': query, 'mkt': mkt }
headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

# Call the API
try:
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()

    print("Headers:")
    print(response.headers)

    print("JSON Response:")
    pprint(response.json())

except Exception as ex:
    raise ex
    