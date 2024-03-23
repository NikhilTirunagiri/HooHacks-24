import os
import requests
import openai # pip install openai

from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

# -- bing web search api test1 --
# python -m pip install azure-cognitiveservices-search-customsearch

from azure.cognitiveservices.search.customsearch import CustomSearchClient
from msrest.authentication import CognitiveServicesCredentials

subscription_key = os.getenv('OPENAI_API_KEY')
endpoint = os.getenv('OPENAI_API_ENDPOINT')