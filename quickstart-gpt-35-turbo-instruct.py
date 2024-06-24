import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv('API_KEY')
api_version = os.getenv('API_VERSION')
azure_endpoint = os.getenv('AZURE_ENDPOINT')
deployment_name = os.getenv('DEPLOYMENT_NAME')

client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=azure_endpoint
)

# Send a completion call to generate an answer
print('Sending a test completion job')
start_phrase = 'What is the length of the the longest mountain in the world?'
response = client.completions.create(model=deployment_name, prompt=start_phrase, max_tokens=10)
print(start_phrase + response.choices[0].text)
