import time
import google.generativeai as genai
import PIL.Image
import os
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
chat = model.start_chat()
response = chat.send_message("Solve for x: 2x + 4 + 67")
print(response.text)
response = chat.send_message("What is the current status of the AAPL stock?")
print(response.text)
