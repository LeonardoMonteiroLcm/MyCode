import os
import speech_recognition as sr # pip install SpeechRecognition
from pydub import AudioSegment  # pip install pydub

def mp3_to_text(mp3_file, output_file):
    try:
        # Converter o arquivo MP3 para WAV
        audio = AudioSegment.from_mp3(mp3_file)
        wav_file = "temp_audio.wav"
        audio.export(wav_file, format="wav")

        # Reconhecimento de fala
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_file) as source:
            print("Carregando áudio...")
            audio_data = recognizer.record(source)
            print("Reconhecendo fala...")
            text = recognizer.recognize_google(audio_data, language="pt-BR")

        # Salvar o texto em um arquivo
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Conversão concluída! Texto salvo em {output_file}")

        # Remover o arquivo WAV temporário
        os.remove(wav_file)

    except Exception as e:
        print(f"Erro: {e}")

# Exemplo de uso
mp3_to_text("audio.mp3", "texto.txt")
