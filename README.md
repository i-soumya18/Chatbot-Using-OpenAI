# Luna A.I-Chat-Bot
Luna A.I. is a chatbot powered by OpenAI's language model. It provides a conversational interface that allows users to interact with the chatbot through speech recognition or text input. The chatbot can perform various tasks such as opening websites, retrieving weather information, translating text, generating AI responses, and more.
# Requirements
Before running the chatbot script, make sure you have the following dependencies installed:
1. Speech Recognition:
>     pip install SpeechRecognition
2. Pyttsx3:
>     pip install pyttsx3
3. requests:
>     pip install requests
You also need to provide your own OpenAI API key in the code (api_key = " INSERT YOUR OPENAI API-KEY HERE ") to utilize the OpenAI language model.

# Usage
To use Luna A.I. chatbot, follow these steps:
1. Clone the repository or download the script file (chatbot.py).
2. Install the required dependencies mentioned in the "Requirements" section.
3. Open the script file in a Python IDE or text editor.
4. Replace the placeholder API key with your own OpenAI API key (api_key = "YOUR_OPENAI_API_KEY").
5. Save the changes to the script file.
6. Run the script in your Python environment.
7. The chatbot will greet you and wait for your input. You can either speak your query or type it in the console.
8. Speak or type your query, and Luna A.I. will respond accordingly.
9. The chatbot supports various commands and functionalities. Refer to the code comments or the code explanation section for details on available commands and functionalities.
10. To stop the chatbot, you can say or type "stop".
# Features 
Speech recognition: The chatbot uses the SpeechRecognition library to listen to user input through a microphone and convert it into text.

Text-to-speech conversion: The chatbot utilizes the pyttsx3 library to convert its responses into speech, providing an interactive conversational experience.

OpenAI integration: The chatbot leverages OpenAI's language model to generate responses based on user input and previous conversations stored in an SQLite database.

Web browsing: The chatbot can open websites such as YouTube, Wikipedia, and Google based on user commands.

Weather information: By providing a city name, the chatbot can retrieve the current weather conditions using the WeatherAPI.

Translation: The chatbot can translate text to different languages using the Google Translate API.

System operations: The chatbot can perform system operations like opening applications, accessing settings, and even shutting down the computer.

# Database
The chatbot stores chat history in an SQLite database file named chat_history.db. Conversations are saved in a table called conversations with columns for user input and bot response.

The reset_chat() function can be used to delete all chat history from the database, and retrieve_chat() function can be used to retrieve and display previous conversations.

#Disclaimer
Luna A.I. is an open-source project developed for educational purposes. It's important to note that the chatbot's functionality heavily relies on external APIs, and proper API keys or credentials should be obtained and used for accessing those services. Use this project responsibly and ensure compliance with the terms and conditions of the utilized APIs.

Feel free to customize and modify the chatbot according to your specific requirements and needs.

# Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or improvements, please open an issue or submit a pull request to contribute to the project.

# Acknowledgments
Special thanks to OpenAI for providing the powerful language model and to the developers of the libraries and APIs used in this project for their contributions.

# Contact
For any inquiries or questions, please contact


[![LinkedIn](https://img.shields.io/badge/LinkedIn-Soumyaranjan%20Sahoo-blue?style=for-the-badge&logo=linkedin)](www.linkedin.com/in/soumya-ranjan-sahoo-b06807248/)
[![Twitter](https://img.shields.io/badge/Twitter-%40soumyaranjan__s-blue?style=for-the-badge&logo=twitter)](https://twitter.com/soumya78948)
[![Instagram](https://img.shields.io/badge/Instagram-%40i_soumya18-orange?style=for-the-badge&logo=instagram)](https://www.instagram.com/i_soumya18/)
[![HackerRank](https://img.shields.io/badge/HackerRank-sahoosoumya24201-brightgreen?style=for-the-badge&logo=hackerrank)](https://www.hackerrank.com/sahoosoumya24201)

Happy chatting with Luna A.I.!
