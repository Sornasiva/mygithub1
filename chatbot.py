import google.generativeai as genai

#API Key
API_KEY = "AIzaSyBkBQN6BCfsMZP5I-Aqq5N2B0OliEm74Ts"

#Configure the API
genai.configure(api_key=API_KEY)

#Create a  new model
model = genai.GenerativeModel("gemini-1.5-pro")
chat = model.start_chat()

while True:
    message = input("You: ")
    if message.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    try:
        response = chat.send_message(message)
        print("Chatbot:", response.text)
    except Exception as e:
        print("Error:",e)