# voice_engine.py

import os
from TTS.api import TTS  # Requires TTS library installed

# Load your model once
tts = TTS("tts_models/en/multilingual/xtts_v2").to("cpu")  # or "cuda" if available

def make_voice(text, output_path="voice.wav"):
    tts.tts_to_file(text=text, speaker_wav="senpai.wav", file_path=output_path, language="en")
    return output_path