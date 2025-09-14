import random

class WebService:
    def __init__(self):
        # Don't load environment variables to avoid potential issues
        self.openweather_api_key = None
    
    def search_web(self, query):
        """Search the web - mock version"""
        print(f"Would search for: {query}")
        return f"Searching for {query}"
    
    def get_weather(self, city="New York"):
        """Get weather information - mock version"""
        return f"Weather information for {city} would appear here with API setup"
    
    def tell_joke(self):
        """Tell a joke - safe version"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a bear with no teeth? A gummy bear!"
        ]
        return random.choice(jokes)