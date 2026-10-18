### 🎮 Telaffuz Oyunu (Pronunciation Game)

Bu proje, kullanıcıların Türkçe kelimeleri doğru ve akıcı bir şekilde telaffuz etmesini eğlenceli bir oyun mekaniğiyle test eden, **Python** tabanlı bir geliştirme projesidir. Ses tanıma ve yapay zeka entegrasyonları ile konuşma pratiği yapmayı kolaylaştırır. 

### ✨ Özellikler

* **Ses Tanıma:** Kullanıcının mikrofonundan aldığı ses sinyallerini metne dönüştürür.
* **Akıllı Doğrulama:** Ekranda gösterilen kelime veya cümle ile kullanıcının telaffuzunu karşılaştırır ve doğruluk skoru üretir.
* **Farklı Çalışma Modları:** Hem terminal tabanlı (main.py) hem de web/arayüz tabanlı (app.py) kullanım esnekliği sunar.
* **Eğlenceli Öğrenme:** Çocuklar, dil öğrenenler veya diksiyonunu geliştirmek isteyenler için interaktif oyunlaştırma prensipleri içerir.

### 🚀 Kurulum

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz: 

### 1. Depoyu Klonlayın

bash

git clone https://github.com/Asu-developer/Telaffuz-Oyunu.git
cd Telaffuz-Oyunu

Use code with caution.

### 2. Gerekli Kütüphaneleri Yükleyin

Projede ses işleme ve arayüz elementleri için gerekli Python paketlerini yükleyin: 

bash

pip install -r requirements.txt

Use code with caution.

*(Eğer requirements.txt henüz mevcut değilse, projenizde kullandığınız SpeechRecognition, pyaudio veya arayüz kütüphanelerini tek tek kurabilirsiniz).* 

### 🕹️ Nasıl Çalıştırılır?

Projenizde iki ana giriş noktası bulunmaktadır: 

### Mod 1: Terminal / Konsol Üzerinden Çalıştırma

Temel oyun mantığını konsol üzerinden deneyimlemek için: 

bash

python main.py

Use code with caution.

### Mod 2: Arayüz / Uygulama Üzerinden Çalıştırma

Geliştirilmiş görsel arayüzü başlatmak için: 

bash

python app.py

Use code with caution.

### 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Ses İşleme:** SpeechRecognition / PyAudio
* **Arayüz (Opsiyonel):** Projenin app.py içeriğine göre (Tkinter / Flask / Streamlit)

### 🤝 Katkıda Bulunma

Katkı sağlamak isterseniz lütfen bir **Fork** oluşturun ve ardından bir **Pull Request** gönderin. Her türlü hata bildirimi ve özellik önerisi projenin gelişimi için değerlidir! 

1. Bu depoyu fork'layın (https://github.com/Asu-developer/Telaffuz-Oyunu/fork)
2. Özellik dalınızı oluşturun (git checkout -b yeni-ozellik)
3. Değişikliklerinizi commit edin (git commit -am 'Yeni özellik eklendi')
4. Dalınızı push edin (git push origin yeni-ozellik)
5. Bir Pull Request oluşturun

### 📄 Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır. Detaylar için LICENSE dosyasına göz atabilirsiniz.
