import pyttsx3
import time

class TextToSpeech:
    def __init__(self, voice_id=1, rate=150):
        self.engine = None
        self.setup_tts()
    
    def setup_tts(self):
        """Setup text-to-speech with error handling"""
        try:
            self.engine = pyttsx3.init()
            voices = self.engine.getProperty('voices')
            if voices and len(voices) > 1:
                self.engine.setProperty('voice', voices[1].id)  # Female voice
            self.engine.setProperty('rate', 150)
            print("✅ Text-to-speech initialized!")
            return True
        except Exception as e:
            print(f"❌ Text-to-speech initialization failed: {e}")
            self.engine = None
            return False
    
    def speak(self, text):
        """Convert text to speech with error handling"""
        print(f"🤖 Assistant: {text}")
        
        if not self.engine:
            return  # Skip speech if TTS not available
        
        try:
            self.engine.say(text)
            self.engine.runAndWait()
            time.sleep(0.5)  # Small pause after speaking
        except Exception as e:
            print(f"❌ Speech synthesis failed: {e}")