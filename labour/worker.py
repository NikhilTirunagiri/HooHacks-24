# Set up your OpenAI API credentials
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Create a new instance of the OpenAI class 
client = OpenAI(
    api_key= os.getenv("OPENAI_API_KEY"),
)

major = input("Major? ") 
location = input("location? ")
in_or_out= input("In state or out-of-state? ")

prompt = f"Provide output in JSON. i am interested in {major}, and my location is {location}. Give out universities, including acceptance rate of the univeristies as well,{in_or_out} fee and location. "
response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106", # gpt-4-1106-preview, 0125
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output in valid JSON, and give out universities, including acceptance rate of the univeristies as well, and location ."},
    {"role": "user", "content": prompt}
  ]
)
print(response.choices[0].message.content)
