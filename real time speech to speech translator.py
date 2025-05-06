import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os
import tempfile

def listen_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak something...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"🔤 You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return ""
    except sr.RequestError:
        print("⚠️ Could not request results.")
        return ""

def translate_text(text, dest_lang='es'):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_lang)
        print(f"🌍 Translated: {translated.text}")
        return translated.text
    except Exception as e:
        print(f"❌ Translation failed: {e}")
        return ""

def speak_text(text, lang='es'):
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
            tts.save(fp.name)
            playsound.playsound(fp.name)
    except Exception as e:
        print(f"🔊 Text-to-Speech failed: {e}")

def main():
    target_language = 'es'  # Spanish
    target_lang_code = 'es'

    while True:
        print("\n--- New Translation Session ---")
        input_text = listen_microphone()
        if input_text.lower() in ["exit", "quit", "stop"]:
            print("👋 Exiting...")
            break

        translated_text = translate_text(input_text, dest_lang=target_lang_code)
        if translated_text:
            speak_text(translated_text, lang=target_lang_code)

if __name__ == "__main__":
    main()
