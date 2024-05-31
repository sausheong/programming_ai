import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.5-flash-latest')
chat = model.start_chat(history=[])

response = chat.send_message("Why is the sky blue?")
print(response.text)
