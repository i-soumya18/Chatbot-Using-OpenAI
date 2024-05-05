from openai import OpenAI
import speech_recognition as sr
import os
import webbrowser
import datetime
import random
import pyttsx3
import requests
import mysql.connector

# Initialize the OpenAI client with the local server's base URL and API key
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

api_key = "Enter your API key here"
mysql_config = {
    'user': 'root',
    'password': 'soumya',
    'host': 'localhost',
    'database': 'chatbot_chats',
}
chat_history_table = "conversations"

conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()

create_table_query = f'''CREATE TABLE IF NOT EXISTS {chat_history_table}
                         (user_input TEXT, bot_response TEXT)'''
cursor.execute(create_table_query)
conn.commit()


def save_chat(user_input, bot_response):
    insert_query = f"INSERT INTO {chat_history_table} (user_input, bot_response) VALUES (%s, %s)"
    cursor.execute(insert_query, (user_input, bot_response))
    conn.commit()


def reset_chat():
    delete_query = f"DELETE FROM {chat_history_table}"
    cursor.execute(delete_query)
    conn.commit()


def retrieve_chat():
    select_query = f"SELECT * FROM {chat_history_table}"
    cursor.execute(select_query)
    return cursor.fetchall()


def chat(query):
    response = get_bot_response(query)
    say(response)
    save_chat(query, response)
    return response


def get_bot_response(user_input):
    completion = client.chat.completions.create(
        model="LM Studio Community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=[{"role": "user", "content": user_input}],
        temperature=0.7,
        stream=True
    )

    bot_response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            bot_response += chunk.choices[0].delta.content

    return bot_response


def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
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
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Some Error Occurred. Sorry from Luna")
            return None



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
    is_active = True

    while is_active:
        print("Listening...")
        query = takeCommand()

        if query is not None:
            query = query.lower()

            if "the time" in query:
                now = datetime.datetime.now()
                time = now.strftime("%I:%M %p")
                say(f"Sir, the time is {time}.")

            elif "weather" in query:
                city = "Bhubaneswar"
                weather_info = get_weather(city)
                say(weather_info)

            elif "stop" in query:
                say("Luna is now inactive.")
                is_active = False

            else:
                print("Chatting...")
                chat(query)
