#!/usr/bin/env python3
"""
Quick demo script for HumorMe
This script demonstrates how to use the humor detection model programmatically.
"""

import os
import tempfile
import librosa
import soundfile as sf
from transformers import pipeline

def demo_humor_detection():
    """Demonstrate humor detection with sample audio"""
    print("🎭 HumorMe Demo Script")
    print("=" * 30)
    
    try:
        # Load the model
        print("📥 Loading humor detection model...")
        classifier = pipeline("audio-classification", model="rishiA/humor_model_v2")
        print("✅ Model loaded successfully!")
        
        # Check if we have any audio files in the current directory
        audio_extensions = ['.wav', '.mp3', '.m4a', '.flac']
        audio_files = []
        
        for file in os.listdir('.'):
            if any(file.lower().endswith(ext) for ext in audio_extensions):
                audio_files.append(file)
        
        if audio_files:
            print(f"\n🎵 Found audio files: {audio_files}")
            print("You can test the model with these files by running:")
            for file in audio_files:
                print(f"  python -c \"from transformers import pipeline; c=pipeline('audio-classification', model='rishiA/humor_model_v2'); print(c('{file}'))\"")
        else:
            print("\n📁 No audio files found in current directory.")
            print("To test the model:")
            print("1. Add some audio files (.wav, .mp3, .m4a) to this directory")
            print("2. Run the web app: python app.py")
            print("3. Record audio or upload files through the web interface")
        
        print("\n🚀 To start the web application:")
        print("   python app.py")
        print("   Then open: http://localhost:5000")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you have installed all dependencies:")
        print("   pip install -r requirements.txt")

if __name__ == "__main__":
    demo_humor_detection()
