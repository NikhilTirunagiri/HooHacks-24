from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
client = OpenAI(api_key="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")

@app.route('/', methods=['GET', 'POST'])
def home():
    outputtu = ""
    if request.method == 'POST':
        # Simulating fetching data from form and OpenAI's response
        major = request.form.get('major', '')
        location = request.form.get('location', '')
        in_or_out = request.form.get('in_or_out', '')

        # Example prompt, replace with your actual OpenAI call if needed
        prompt = f"Provide output in JSON. I am interested in {major}, and my location is {location}. Give out universities, including acceptance rate of the universities as well, {in_or_out} fee and location."

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",  # Use an appropriate model
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to output in JSON, and give out universities, including acceptance rate of the universities as well, and location."},
                {"role": "user", "content": prompt}
            ]
        )
        outputtu = response.choices[0].message.content
    return render_template('index.html', message=outputtu)

if __name__ == '__main__':
    app.run(debug=True)
