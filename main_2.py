import webbrowser
import pyttsx3
from datetime import datetime
import re

# Initialize TTS engine
engine = pyttsx3.init()

# Constants
BASE_URL = "https://"
GOOGLE_SEARCH_URL = "https://www.google.com/search?q="
YOUTUBE_SEARCH_URL = "https://www.youtube.com/results?search_query="
CHATGPT_URL = "https://chat.openai.com/"
CALCULATOR_URL = "https://www.calculator.net/"
CHESS_URL = "https://www.chess.com/"

def speak(text):
    print(f"\nJarvis 🧠: {text}")
    engine.say(text)
    engine.runAndWait()

def get_text_input(prompt="Type your command: "):
    return input(f"\n🧠 {prompt}").lower()

def open_chess():
    webbrowser.open(CHESS_URL)
    speak("Opening Chess.com")

def open_website(website):
    url = f"{BASE_URL}{website}.com"
    webbrowser.open(url)
    speak(f"Opening {website}")

def open_calculator():
    webbrowser.open(CALCULATOR_URL)
    speak("Opening calculator")

def open_chatgpt():
    webbrowser.open(CHATGPT_URL)
    speak("Opening ChatGPT")

def search(query):
    url = f"{GOOGLE_SEARCH_URL}{query}"
    webbrowser.open(url)
    speak(f"Searching for {query}")

def play_music(song):
    url = f"{YOUTUBE_SEARCH_URL}{song}"
    webbrowser.open(url)
    speak(f"Playing music: {song}")

def tell_time():
    current_time = datetime.now().strftime("%H:%M")
    speak(f"The current time is {current_time}")

def tell_date_and_time():
    now = datetime.now()
    date_time = now.strftime("Today is %A, %d %B %Y, and the current time is %H:%M")
    speak(date_time)

def tell_joke():
    joke = "Why don't scientists trust atoms? Because they make up everything!"
    speak(joke)

def process_command(command):
    if "open" in command and "chatgpt" in command:
        open_chatgpt()

    elif "open" in command:
        website = re.search(r'open (.+)', command)
        if website:
            open_website(website.group(1).strip().replace(" ", ""))
        else:
            speak("Please specify a website to open.")
            new_cmd = get_text_input("Enter the website name:")
            open_website(new_cmd.strip().replace(" ", ""))

    elif "search" in command:
        query = re.search(r'search (.+)', command)
        if query:
            search(query.group(1).strip())
        else:
            speak("Please specify a search query.")
            new_query = get_text_input("What do you want to search for?")
            search(new_query.strip())

    elif "play music" in command:
        song = re.search(r'play music (.+)', command)
        if song:
            play_music(song.group(1).strip())
        else:
            speak("Please specify a song to play.")
            new_song = get_text_input("Which song do you want to play?")
            play_music(new_song.strip())

    elif "what time is it" in command or "current time" in command:
        tell_time()

    elif "date and time" in command or "what's the date" in command:
        tell_date_and_time()

    elif "tell me a joke" in command:
        tell_joke()

    elif "exit" in command or "quit" in command:
        speak("Goodbye! See you soon.")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")

# Main Loop
if __name__ == "__main__":
    speak("VA is initialized and ready.")

    while True:
        command = get_text_input("Type Secret key to activate me: ")
        
        if "jarvis" in command:
            speak("Paddy is activated. How can I help you?")
            user_command = get_text_input("Enter your command: ")
            process_command(user_command)
        else:
            speak("Type 'Secret Key' to activate me.")
