from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv() 

GENAI_KEY = os.getenv('GENAI_KEY')

genai.configure(api_key=GENAI_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")

print(response.text)
