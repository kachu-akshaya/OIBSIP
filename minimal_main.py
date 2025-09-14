#!/usr/bin/env python3
"""
Minimal Voice Assistant - No complex dependencies
"""

import speech_recognition as sr
import pyttsx3
import time
import webbrowser
import datetime
import random

class MinimalVoiceAssistant:
    def __init__(self):
        print("🚀 Starting Minimal Voice Assistant...")
        
        # Initialize speech components
        self.setup_speech()
        
        # Command mappings
        self.commands = {
            'time': self.get_time,
            'date': self.get_date,
            'search': self.search_web,
            'joke': self.tell_joke,
            'open': self.open_app,
            'exit': self.exit_app
        }
        
        print("✅ Assistant ready!")
    
    def setup_speech(self):
        """Setup speech components with error handling"""
        try:
            # Text-to-speech
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('rate', 150)
            print("✅ TTS initialized")
        except:
            self.tts_engine = None
            print("❌ TTS failed - using text output")
        
        try:
            # Speech recognition
            self.recognizer = sr.Recognizer()
            print("✅ Speech recognition initialized")
        except:
            self.recognizer = None
            print("❌ Speech recognition failed - using text input")
    
    def speak(self, text):
        """Speak text or print if TTS fails"""
        print(f"🤖: {text}")
        if self.tts_engine:
            try:
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
            except:
                print("❌ TTS failed")
    
    def listen(self):
        """Listen for speech or get text input"""
        if not self.recognizer:
            return input("💬 Type your command: ").lower()
        
        try:
            with sr.Microphone() as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)
            
            print("🔍 Recognizing...")
            text = self.recognizer.recognize_google(audio)
            print(f"👤: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return "sorry"
        except sr.RequestError:
            print("❌ Speech service unavailable")
            return input("💬 Type your command: ").lower()
        except Exception as e:
            print(f"❌ Listening error: {e}")
            return input("💬 Type your command: ").lower()
    
    def get_time(self):
        return datetime.datetime.now().strftime("It's %I:%M %p")
    
    def get_date(self):
        return datetime.datetime.now().strftime("Today is %B %d, %Y")
    
    def search_web(self, query):
        webbrowser.open(f"https://google.com/search?q={query}")
        return f"Searching for {query}"
    
    def tell_joke(self):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a bear with no teeth? A gummy bear!"
        ]
        return random.choice(jokes)
    
    def open_app(self, app_name):
        app_name = app_name.lower()
        if 'chrome' in app_name or 'browser' in app_name:
            webbrowser.open("https://google.com")
            return "Opening browser"
        else:
            return "I can only open the browser for now"
    
    def exit_app(self):
        return "exit"
    
    def process_command(self, command):
        if not command or "sorry" in command:
            return False, "I didn't understand that"
        
        for keyword, action in self.commands.items():
            if keyword in command:
                result = action(command)
                return (result == "exit"), result
        
        return False, "I'm not sure how to help with that"
    
    def run(self):
        self.speak("Hello! I'm your minimal voice assistant")
        
        while True:
            try:
                command = self.listen()
                exit_flag, response = self.process_command(command)
                
                if exit_flag:
                    self.speak("Goodbye!")
                    break
                elif response:
                    self.speak(response)
                
                time.sleep(1)
                
            except KeyboardInterrupt:
                self.speak("Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                self.speak("Sorry, I encountered an error")

if __name__ == "__main__":
    assistant = MinimalVoiceAssistant()
    assistant.run()