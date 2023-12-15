import google.generativeai as genai
import speech_recognition as sr
import os
import webbrowser
import datetime
import requests
import random
import pyttsx3
import mysql.connector
import pprint
import csv
from google.generativeai import chat

genai.configure(api_key="your Gemini Api Key")

# Set up the Gemini model and configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
)

def chat(query):
    response = model.generate_content([query])
    return response.text
chat_history_file = "chat_history.csv"  # CSV file to store chat history
header = ['user_input', 'bot_response']


def create_chat_history_file():
    # Create the chat history CSV file with headers if it doesn't exist
    if not os.path.exists(chat_history_file):
        with open(chat_history_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)

def save_chat(user_input, bot_response):
    # Save the conversation to the CSV file
    with open(chat_history_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([user_input, bot_response])


def reset_chat():
    # Delete the existing chat history CSV file if it exists
    if os.path.exists(chat_history_file):
        os.remove(chat_history_file)
    # Create a new chat history CSV file
    create_chat_history_file()
def retrieve_chat():
    # Retrieve all conversations from the CSV file
    conversations = []
    try:
        with open(chat_history_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Skip the header row
            next(reader)
            for row in reader:
                conversations.append(row)
    except FileNotFoundError:
        pass  # Return an empty list if the file doesn't exist
    return conversations
# Create the chat history CSV file with headers if it doesn't exist
create_chat_history_file()

def ai(prompt):
    response = model.generate_content([prompt])
    return response.text

def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Change the index to use a different voice
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            #query = r.recognize_google(audio, language="hi-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Luna"


def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    weather = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_c"]
    return f"The weather in {city} is {weather} with a temperature of {temperature}°C."


if __name__ == '__main__':
    print('Welcome To Luna A.I')
    say("Hello, soumya")
    is_active = True  # Variable to control the conversation loop
    while is_active:
        print("Listening...")
        query = takeCommand().lower()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"],["chat GPT", "https://chat.openai.com"], ["youtube music", "https://music.youtube.com/"],
                ]
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = r"C:\Users\SOUMYA\Music"
            os.startfile(musicPath)
        if "open android studio" in query:
            androidPath = r"C:\PerfLogs\android studio\bin\studio64.exe"
            os.startfile(androidPath)

        elif "the time" in query:
            now = datetime.datetime.now()
            time = now.strftime("%I:%M %p")
            say(f"Sir, the time is {time}.")

        elif "weather" in query:
            city = "Bhubaneswar"  # Replace with user-provided city or implement speech recognition
            weather_info = get_weather(city)
            say(weather_info)

        elif "open calculator" in query:
            # Modify the path to the desired application or remove this block if not applicable
            calculator = r"C:\Windows\System32\calc.exe"
            os.startfile(calculator)

        elif "open notepad" in query:
            # Modify the path to the desired application or remove this block if not applicable
            notepad = r"C:\Windows\System32\notepad.exe"
            os.startfile(notepad)

        elif "open whatsapp" in query:

             whatsappPath = r"C:\Path\to\WhatsApp.exe"

             os.startfile(whatsappPath)


        elif "open mail" in query:

             mailPath = r"C:\Path\to\Mail.exe"

             os.startfile(mailPath)


        elif "open file explorer" in query:

            explorerPath = r"C:\Windows\explorer.exe"

            os.startfile(explorerPath)


        elif "open microsoft store" in query:

            storePath = r"C:\Windows\System32\ms-store://"

            os.startfile(storePath)


        elif "open settings" in query:

            settingsPath = r"C:\Windows\System32\control.exe"

            os.startfile(settingsPath)
        elif "open cmd" in query:
            # Modify the path to the desired application or remove this block if not applicable
            cmdpath = r"C:\Windows\System32\cmd.exe"
            os.startfile(cmdpath)
        elif "open control panel" in query:
            # Modify the path to the desired application or remove this block if not applicable
            controlePath = r"C:\Windows\System32\control.exe"
            os.startfile(controlePath)
        elif "open task manager" in query:
            # Modify the path to the desired application or remove this block if not applicable
            taskPath = r"C:\Windows\System32\Taskmgr.exe"
            os.startfile(taskPath)
        elif "open voice access" in query:
            # Modify the path to the desired application or remove this block if not applicable
            voicePath = r"C:\Windows\System32\VoiceAccess.exe"
            os.startfile(voicePath)

        elif "translate" in query:
            api_key = "YOUR_TRANSLATION_API_KEY"
            say("Sure, what would you like to translate?")
            text_to_translate = takeCommand().lower()  # Capture user input for text to translate
            say("Great! Which language would you like to translate it to?")
            target_language = takeCommand().lower()  # Capture user input for target language
            url = f"https://translation.googleapis.com/language/translate/v2?key={api_key}"
            params = {
                "q": text_to_translate,
                "target": target_language
            }
            response = requests.post(url, params=params)
            data = response.json()
            translated_text = data["data"]["translations"][0]["translatedText"]
            say(f"The translation is: {translated_text}")

        elif "using artificial intelligence" in query:
            ai(prompt=query)

        elif "stop" in query:
            say("Luna is now inactive.")
            is_active = False  # Set the conversation loop variable to False to exit the loop

        elif "luna" in query:
            print("Luna is now active.")

        elif "reset chat" in query:
            reset_chat()
            say("Chat history has been reset.")

        elif "restore chat" in query:
            conversations = retrieve_chat()
            if len(conversations) == 0:
                say("No chat history found.")
            else:
                say("Chat history:")
                for user_input, bot_response in conversations:
                    print(f"User: {user_input}")
                    print(f"Luna: {bot_response}")
                    print("------------------------")

        elif "shutdown" in query:
            say("Are you sure you want to shut down your computer?")
            confirm = takeCommand().lower()

            if "yes" in confirm:
                say("Shutting down your computer...Bye Boss")
                os.system("shutdown /s /t 0")
            else:
                say("Shutdown canceled.")
        else:
            print("Chatting...")
            response = chat(query)
            print(response)  # Display the response on the screen
            say(response)
