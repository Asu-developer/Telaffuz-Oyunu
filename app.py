import random
import time
import io
import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd
import speech_recognition as sr
import streamlit as st
from googletrans import Translator

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Kelime Çeviri Oyunu Pro", page_icon="🎙️", layout="centered")

# --- FONKSİYONLAR ---
def Translate(text_to_translate, dest_lang="en"):
    try:
        translator = Translator()
        translated = translator.translate(text_to_translate, src="tr", dest=dest_lang)
        return translated.text
    except Exception as e:
        st.error(f"Çeviri Hatası: {e}")
        return None

def Record_voice(speech_lang="en-US"):
    duration = 3
    sample_rate = 44100

    countdown_place = st.empty()
    for i in range(3, 0, -1):
        countdown_place.markdown(f"<h3 style='text-align:center; color:orange;'>🎙️ {i} saniye içinde kayıt başlıyor...</h3>", unsafe_allow_html=True)
        time.sleep(1)
    
    countdown_place.markdown("<h3 style='text-align:center; color:red;'>🔴 ŞİMDİ KONUŞUN! (3 Saniye)</h3>", unsafe_allow_html=True)

    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
    sd.wait()
    countdown_place.markdown("<h3 style='text-align:center; color:green;'>✅ Analiz Ediliyor...</h3>", unsafe_allow_html=True)
    time.sleep(0.5)
    countdown_place.empty()

    wav.write("output.wav", sample_rate, recording)

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language=speech_lang)
        return text
    except:
        return None

# --- KELİME HAVUZU ---
seviyeye_göre_kelimeler = {
    "kolay": ["kedi", "köpek", "elma", "süt", "güneş", "kuş", "balık", "masa", "kitap", "kalem"],
    "orta": ["muz", "okul", "arkadaş", "pencere", "sarı", "bilgisayar", "telefon", "öğretmen"],
    "zor": ["teknoloji", "üniversite", "bilgi", "telaffuz", "hayal gücü", "tebrikler", "yapay zeka"]
}

# --- DURUM (STATE) YÖNETİMİ ---
if "true_count" not in st.session_state: st.session_state.true_count = 0
if "false_count" not in st.session_state: st.session_state.false_count = 0
if "current_word" not in st.session_state: st.session_state.current_word = random.choice(seviyeye_göre_kelimeler["kolay"])
if "wrong_words" not in st.session_state: st.session_state.wrong_words = []
if "streak" not in st.session_state: st.session_state.streak = 0
if "practice_mode" not in st.session_state: st.session_state.practice_mode = False

def yeni_kelime_sec(zorluk, sadece_hatalilar=False):
    if sadece_hatalilar and st.session_state.wrong_words:
        secilen = random.choice(st.session_state.wrong_words)
        st.session_state.current_word = secilen["Türkçe"]
    else:
        st.session_state.current_word = random.choice(seviyeye_göre_kelimeler[zorluk])

# --- ARAYÜZ TASARIMI ---
st.markdown("<h1 style='text-align: center; color: #1f77b4;'>🎙️ Kelime Çeviri & Telaffuz Master Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Türkçe kelimenin İngilizce karşılığını seslendirin, telaffuzunuzu test edin!</p>", unsafe_allow_html=True)

# --- YAN MENÜ (SIDEBAR) ---
with st.sidebar:
    st.header("🎮 Oyun Ayarları")
    mod = st.radio("Oyun Modu:", ["Normal Kelime Havuzu", "🎯 Sadece Hatalı Kelimeleri Tekrar Et"])
    
    if mod == "🎯 Sadece Hatalı Kelimeleri Tekrar Et":
        if not st.session_state.wrong_words:
            st.warning("Henüz hiç yanlış yapmadınız! Normal moda dönüldü.")
            st.session_state.practice_mode = False
            diffuculty = st.selectbox("Zorluk Derecesi:", ["kolay", "orta", "zor"], key="diff_box")
        else:
            st.success("Tekrar Modu Aktif! Sadece hatalı kelimeler sorulacak.")
            st.session_state.practice_mode = True
            diffuculty = "kolay"
    else:
        st.session_state.practice_mode = False
        diffuculty = st.selectbox("Zorluk Derecesi:", ["kolay", "orta", "zor"], on_change=yeni_kelime_sec, args=("kolay", False))
    
    st.markdown("---")
    st.subheader("📊 Canlı İstatistikler")
    st.write(f"🟢 **Doğru Sayısı:** {st.session_state.true_count}")
    st.write(f"🔴 **Yanlış Sayısı:** {st.session_state.false_count}")
    st.write(f"🔥 **Seri (Streak):** {st.session_state.streak}")
    
    net_puan = st.session_state.true_count - (st.session_state.false_count / 4)
    st.metric(label="Toplam Net Puan", value=f"{net_puan:.2f} N")
    
    if st.button("Oyunu ve Skorları Sıfırla", use_container_width=True):
        st.session_state.true_count = 0
        st.session_state.false_count = 0
        st.session_state.streak = 0
        st.session_state.wrong_words = []
        st.session_state.practice_mode = False
        st.session_state.current_word = random.choice(seviyeye_göre_kelimeler["kolay"])
        st.rerun()

# İlerleme Çubuğu
progress_value = min(max(net_puan / 10, 0.0), 1.0)
st.caption(f"🏆 Seviye İlerlemesi (Hedef: 10 Net Puan)")
st.progress(progress_value)

if st.session_state.streak >= 3:
    st.warning(f"🔥 Harikasın! Üst üste {st.session_state.streak} kez doğru telaffuz ettin!")

Translate_word = Translate(st.session_state.current_word, dest_lang="en")

st.markdown(
    f"""
    <div style="background: linear-gradient(135deg, #1f77b4, #aec7e8); padding:30px; border-radius:15px; text-align:center; color:white; box-shadow: 2px 4px 10px rgba(0,0,0,0.1);">
        <span style="font-size:16px; font-weight:bold; opacity:0.8;">SORULAN KELİME</span><br>
        <strong style="font-size:45px; letter-spacing: 2px;">{st.session_state.current_word.upper()}</strong>
    </div>
    """,
    unsafe_allow_html=True,
)

# Tarayıcının kendi seslendirme motorunu (Web Speech API) kullanan Buton
if Translate_word:
    st.write("")
    tts_html = f"""
    <div style="text-align: right;">
        <button onclick="window.speechSynthesis.speak(new SpeechSynthesisUtterance('{Translate_word}'))" 
        style="background-color: #f0f2f6; border: 1px solid #d1d5db; color: #374151; padding: 6px 12px; border-radius: 8px; font-size: 14px; cursor: pointer;">
            🔊 Doğrusunu Dinle
        </button>
    </div>
    """
    st.components.v1.html(tts_html, height=45)

st.write("")

if st.button("🎤 SES KAYDINI BAŞLAT", use_container_width=True, type="primary"):
    Mic_Word = Record_voice(speech_lang="en-US")

    if Mic_Word and Translate_word:
        st.markdown(f"**Sizin Söylediğiniz:** `{Mic_Word}` | **Olması Gereken:** `{Translate_word}`")

        if Mic_Word.lower() == Translate_word.lower():
            st.balloons()
            st.success(f"🎉 Mükemmel! '{Translate_word}' doğru telaffuz.")
            st.session_state.true_count += 1
            st.session_state.streak += 1
            
            if st.session_state.practice_mode:
                st.session_state.wrong_words = [w for w in st.session_state.wrong_words if w["Türkçe"] != st.session_state.current_word]
        else:
            st.error(f"❌ Yanlış Telaffuz. Doğrusu '{Translate_word}' olmalıydı.")
            st.session_state.false_count += 1
            st.session_state.streak = 0

            if not any(w["Türkçe"] == st.session_state.current_word for w in st.session_state.wrong_words):
                st.session_state.wrong_words.append({
                    "Türkçe": st.session_state.current_word,
                    "Doğrusu": Translate_word,
                    "Son Söylenen": Mic_Word
                })

        yeni_kelime_sec(diffuculty, sadece_hatalilar=st.session_state.practice_mode)
        time.sleep(2.5)
        st.rerun()
    else:
        st.error("⚠️ Ses algılanamadı veya net okunamadı. Lütfen butona basıp sürede tekrar konuşun.")
        st.session_state.streak = 0

# --- YANLIŞ BİLİNEN KELİMELER LİSTESİ ---
st.markdown("---")
st.subheader("📚 Yanlış Yapılan Kelimeler Çalışma Listesi")

if st.session_state.wrong_words:
    st.caption("Bu kelimeleri tekrar etmek telaffuzunuzu geliştirecektir:")
    st.table(st.session_state.wrong_words)
else:
    st.info("Harika gidiyorsun! Henüz hiç yanlış yapmadın. 🚀")
