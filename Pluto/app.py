import tkinter as tk
from main import greet_me, take_command, speak, start_listening,pause_listening
from online import find_my_ip, search_on_wikipedia, search_on_google, youtube, send_email, get_news, weather_forecast
from conv import random_text
def start_listening():
    query = take_command().lower()
    if "how are you" in query:
        speak("I am absolutely fine sir. What about you")
    elif "open command prompt" in query:
        speak("Opening command prompt")
        os.system('start cmd')
    elif "open camera" in query:
        speak("Opening camera sir")
        sp.run('start microsoft.windows.camera:', shell=True)
    elif "open notepad" in query:
        speak("Opening Notepad for you sir")
        notepad_path = "C:\\Windows\\notepad.exe"
        os.startfile(notepad_path)
    elif "spotify" in query:
        speak("Opening Spotify for you sir")
        spotify_path = "C:\\Users\\vishw\\AppData\\Roaming\\Spotify\\Spotify.exe"
        os.startfile(spotify_path)
    elif "open CapCut" in query:
        speak("Opening CapCut for you sir")
        CapCut_path = "C:\\Users\\vishw\\AppData\\Local\\CapCut\\Apps\\CapCut.exe"
        os.startfile(CapCut_path)
    elif 'ip address' in query:
        ip_address = find_my_ip()
        speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
        print(f'Your IP Address is {ip_address}')
    elif "open youtube" in query:
        speak("What do you want to play on youtube sir?")
        video = take_command().lower()
        youtube(video)
    elif "open google" in query:
        speak(f"What do you want to search on google {USER}")
        query = take_command().lower()
        search_on_google(query)
    elif "wikipedia" in query:
        speak("what do you want to search on wikipedia sir?")
        search = take_command().lower()
        results = search_on_wikipedia(search)
        speak(f"According to wikipedia,{results}")
        speak("I am printing in on terminal")
        print(results)
    elif "send an email" in query:
        speak("On what email address do you want to send sir?. Please enter in the terminal")
        receiver_add = input("Email address:")
        speak("What should be the subject sir?")
        subject = take_command().capitalize()
        speak("What is the message ?")
        message = take_command().capitalize()
        if send_email(receiver_add, subject, message):
            speak("I have sent the email sir")
            print("I have sent the email sir")
        else:
            speak("something went wrong Please check the error log")
    elif "give me news" in query:
        speak(f"I am reading out the latest headline of today,sir")
        news_headlines = get_news()
        speak(". ".join(news_headlines))
        speak("I am printing it on screen sir")
        print(*news_headlines, sep='\n')
    elif 'weather' in query:
        speak("Tell me the name of your city")
        city = take_command().lower()
        speak(f"Getting weather report for your city {city}")
        weather, temp, feels_like = weather_forecast(city)
        speak(f"The current temperature is {temp}, but it feels like {feels_like}")
        speak(f"Also, the weather report talks about {weather}")
        speak("For your convenience, I am printing it on the screen sir.")
        print(f"Description: {weather}\nTemperature: {temp}\nFeels like: {feels_like}")

root = tk.Tk()
root.title("Voice Assistant App")

label = tk.Label(root, text="Click the button and start speaking:")
label.pack()

button = tk.Button(root, text="Start Listening", command=start_listening)
button.pack()

greet_me()

root.mainloop()
