### 🎮 Telaffuz Oyunu (Pronunciation Game)

Bu proje, kullanıcıların Türkçe kelimeleri doğru ve akıcı bir şekilde telaffuz etmesini eğlenceli bir oyun mekaniğiyle test eden, **Python** ve **Streamlit** tabanlı interaktif bir web uygulamasıdır. Ses tanıma teknolojilerini kullanarak konuşma pratiği yapmayı keyifli hale getirir. 

### ✨ Özellikler

* **Modern Web Arayüzü:** Streamlit ile geliştirilmiş, kullanıcı dostu ve hızlı yanıt veren sade arayüz.
* **Ses Tanıma (Speech Recognition):** Mikrofon yardımıyla kullanıcının sesini anlık olarak algılar ve metne dönüştürür.
* **Akıllı Doğrulama:** Ekranda hedef olarak gösterilen kelime/cümle ile kullanıcının telaffuzunu eşleştirerek doğruluk skoru hesaplar.
* **Eğlenceli Öğrenme:** Çocuklar, dil öğrenenler veya diksiyonunu geliştirmek isteyen herkes için harika bir interaktif pratik aracıdır.

### 🚀 Kurulum ve Çalıştırma

Uygulamayı yerel bilgisayarınızda ayağa kaldırmak için aşağıdaki adımları sırasıyla uygulayabilirsiniz: 

### 1. Depoyu Klonlayın

bash

git clone https://github.com/Asu-developer/Telaffuz-Oyunu.git
cd Telaffuz-Oyunu

Use code with caution.

### 2. Bağımlılıkları Yükleyin

Projenin çalışması için gerekli kütüphaneleri (Streamlit, ses tanıma paketleri vb.) yükleyin: 

bash

pip install -r requirements.txt

Use code with caution.

*(Eğer kütüphaneler bilgisayarınızda henüz yüklü değilse, manuel olarak pip install streamlit speechrecognition komutunu da kullanabilirsiniz).* 

### 3. Uygulamayı Başlatın

Web sitesini yerel sunucunuzda çalıştırmak için terminale şu komutu yazın: 

bash

py -m streamlit run app.py

Use code with caution.

Komutu çalıştırdıktan sonra tarayıcınızda otomatik olarak http://localhost:8501 adresi açılacaktır. 

### 🛠️ Kullanılan Teknolojiler

* **Geliştirme Dili:** Python 3.x
* **Web Çerçevesi (Framework):** Streamlit
* **Ses İşleme:** SpeechRecognition / PyAudio (veya ilgili kütüphaneler)

### 🤝 Katkıda Bulunma

Projeyi geliştirmeye yardımcı olmak ister misiniz? Her türlü hata bildirimi, iyileştirme ve yeni özellik önerisi için bir **Pull Request** açabilir veya **Issue** oluşturabilirsiniz. 

1. Projeyi fork'layın (https://github.com/Asu-developer/Telaffuz-Oyunu/fork)
2. Yeni bir özellik dalı açın (git checkout -b yeni-ozellik)
3. Değişikliklerinizi kaydedin (git commit -am 'Yeni özellik eklendi')
4. Dalınızı push edin (git push origin yeni-ozellik)
5. Pull Request gönderin

### 📄 Lisans

Bu proje **MIT Lisansı** altında korunmaktadır. Daha fazla bilgi için LICENSE dosyasına göz atabilirsiniz.
