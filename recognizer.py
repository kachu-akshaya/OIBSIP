class SimpleRecognizer:
    def __init__(self):
        self.use_microphone = False
        self.setup()
    
    def setup(self):
        """Simple setup without complex dependencies"""
        try:
            import speech_recognition as sr
            self.recognizer = sr.Recognizer()
            self.use_microphone = True
            print("✅ Microphone available")
        except:
            print("❌ Using text input only")
            self.use_microphone = False
    
    def listen(self):
        """Simple listen with fallback"""
        if not self.use_microphone:
            return input("💬 Type command: ").lower()
        
        try:
            with self.recognizer.Microphone() as source:
                print("🎤 Listening...")
                audio = self.recognizer.listen(source, timeout=3)
            text = self.recognizer.recognize_google(audio)
            return text.lower()
        except:
            return input("💬 Type command: ").lower()