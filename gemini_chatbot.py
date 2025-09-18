import google.generativeai as genai

# Your API key
API_KEY = "AIzaSyARR31t4dhmni64RH_Ox9zvH0GPiw9LQls"

# Configure Gemini
genai.configure(api_key=API_KEY)

# ✅ Use the correct model name
model = genai.GenerativeModel("models/gemini-2.0-flash")

print("🤖 Gemini Chatbot: Type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    try:
        response = model.generate_content(user_input)
        print("Chatbot:", response.text)
    except Exception as e:
        print("Error:", e)
