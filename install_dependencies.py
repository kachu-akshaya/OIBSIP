#!/usr/bin/env python3
"""
Script to install voice assistant dependencies
"""

import subprocess
import sys

def run_command(command):
    """Run a shell command"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def main():
    print("🔧 Installing Voice Assistant Dependencies...")
    print("=" * 50)
    
    # List of packages to install
    packages = [
        "SpeechRecognition",
        "pyttsx3", 
        "requests",
        "python-dotenv"
    ]
    
    success_count = 0
    
    for package in packages:
        print(f"📦 Installing {package}...")
        success, stdout, stderr = run_command(f"pip install {package}")
        
        if success:
            print(f"✅ {package} installed successfully!")
            success_count += 1
        else:
            print(f"❌ Failed to install {package}")
            print(f"   Error: {stderr}")
    
    print("=" * 50)
    print(f"📊 Results: {success_count}/{len(packages)} packages installed")
    
    if success_count == len(packages):
        print("🎉 All dependencies installed successfully!")
        print("🚀 You can now run: python main.py")
    else:
        print("❌ Some dependencies failed to install.")
        print("💡 You may need to install system dependencies first:")
        print("   Ubuntu/Debian: sudo apt-get install python3-pyaudio portaudio19-dev")
        print("   macOS: brew install portaudio")

if __name__ == "__main__":
    main()