# voice_engine.py

import os
from TTS.api import TTS
from mutagen import File

tts = TTS("tts_models/en/multilingual/xtts_v2").to("cpu")

def is_audio_valid(path):
    audio = File(path)
    return audio is not None and audio.mime[0].startswith("audio/")

def make_voice(text, output_path="voice.wav"):
    tts.tts_to_file(text=text, speaker_wav="senpai.wav", file_path=output_path, language="en")
    if not is_audio_valid(output_path):
        raise ValueError("Generated audio is not valid")
    return output_path
