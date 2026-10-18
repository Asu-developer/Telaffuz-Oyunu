import random
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import time 

def get_language_name(lang_code):
    languages = {"en": "İngilizce", "tr": "Türkçe"}
    return languages.get(lang_code, "Bilinmeyen Dil")

def Record_voice(speech_lang="en-US"):
    duration = 3  
    sample_rate = 44100

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    print("\nŞimdi konuşun 3 saniyeniz var...")
    recording = sd.rec(
        int(duration * sample_rate), 
        samplerate=sample_rate,      
        channels=1,                  
        dtype="int16"
    )               
    sd.wait()
    wav.write("output.wav", sample_rate, recording)
    print("Kayıt tamamlandı, ses tanınıyor...")

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language=speech_lang)
        print("Söylediğiniz sözcük:", text)
        return text  
        
    except sr.UnknownValueError:             
        print("Konuşma tanınamadı.")
        return None
    except sr.RequestError as e:             
        print(f"Hizmet hatası: {e}")
        return None

def Translate(text_to_translate, dest_lang="en"):
    if not text_to_translate:
        print("Hata Oldu!: Çevrilecek metin bulunamadı.")
        return None

    try:
        translator = Translator()
        translated = translator.translate(text_to_translate, src="tr", dest=dest_lang)
        return translated.text
    except Exception as e:
        print("Hata Oldu!: " + str(e))
        return None

seviyeye_göre_kelimeler = {
    "kolay": [
        "kedi", "köpek", "elma", "süt", "güneş", "kuş", "balık", "masa", "kitap", "kalem",
        "su", "ekmek", "ev", "ağaç", "deniz", "çocuk", "anne", "baba", "kapı", "yeşil"
    ],
    "orta": [
        "muz", "okul", "arkadaş", "pencere", "sarı", "bilgisayar", "telefon", "öğretmen", "öğrenci", "otobüs",
        "bisiklet", "mutluluk", "Gelecek", "kütüphane", "sinema", "tiyatro", "gökyüzü", "bulut", "rüzgar", "yağmur"
    ],
    "zor": [
        "teknoloji", "üniversite", "bilgi", "telaffuz", "hayal gücü", "tebrikler", "karakteristik", "sürdürülebilirlik",
        "biyokimya", "medeniyet", "küreselleşme", "özelleştirme", "faydalanmak", "gerçekleştirmek",
        "değerlendirmek", "yapay zeka", "cumhuriyet", "mühendislik", "psikoloji", "koleksiyon"
    ]
}
point =  0
true = 0
false = 0
while True:
    print("######## Kelime Çeviri Oyununa Hoş Geldiniz ########")
    diffuculty = input("Zorluk (zor, orta, kolay): ").strip().lower()

    if diffuculty not in seviyeye_göre_kelimeler:
        print("Geçersiz zorluk seçtiniz! Otomatik olarak 'kolay' modu seçildi.")
        diffuculty = "kolay"

    word = random.choice(seviyeye_göre_kelimeler[diffuculty])

    print("""Bu kelimenin İNGİLİZCESİNİ seslendirin! 
Kelime: """ + word)

    Translate_word = Translate(word, dest_lang="en")
    Mic_Word = Record_voice(speech_lang="en-US")

    if Mic_Word and Translate_word:
        if Mic_Word.lower() == Translate_word.lower():
            print("🎉 Doğru telaffuz ettin!")
            true = true + 1
        else:
            print("❌ Yanlış telaffuz. Doğrusu " + Translate_word + " olmalıydı.")
            false = false + 1
    else:
        print("Sistem hatası veya ses algılanamadığı için kontrol yapılamadı.")
        
    secim = input("\nDevam etmek istiyor musunuz? (devam/tamam): ").strip().lower()
    if secim == "tamam":
        print("Oyun bitti! Katıldığınız için teşekkürler.")
        print("Net Puanın: " + str(true-(false/4)) + "N")
        print("Doğru: " + str(true))
        print("Yanlış: " + str(false))
        break