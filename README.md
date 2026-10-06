#  The Clan War (Klanların Savaşı) - İnteraktif Görsel Roman

**The Clan War**, Büyük Kıtlık dönemiyle yüzleşen bir ormandaki güç mücadelelerini konu alan, oyuncu kararlarına dayalı ve çoklu sonlara (branching narrative) sahip stratejik bir görsel romandır. Gelişmiş değişken yönetimi, zaman sınırlı mekanikler ve etkileşimli bilmeceler ile geleneksel tıklama oyunlarının ötesine geçerek dinamik bir oyun deneyimi sunar.

---

##  Öne Çıkan Teknik Özellikler

Bu proje, temel hikaye anlatımının yanı sıra aşağıdaki programlama mantıklarını ve oyun mekaniklerini barındırır:

*   **Dinamik Kaynak Yönetimi (Variable Tracking & UI):** Ekranın sağ üst köşesinde sürekli güncellenen bir arayüz ile oyuncunun "Erzak" ve "Saygı" seviyeleri takip edilir. Alınan her karar bu değişkenleri matematiksel olarak etkiler ve kritik seviyeler oyun sonlarını doğrudan değiştirir.
*   **Dallanan Senaryo Ağacı (Branching Narrative):** 5 farklı klanın her biri için özel olarak yazılmış, 3 aşamalı karar ağaçları barındırır. Oyun toplamda **40 farklı benzersiz sona** sahiptir.
*   **Zaman Sınırlı Kararlar (Timer & QTE):** Oyuncunun reflekslerini test eden, 3 saniye içinde karar verilmediğinde zaman aşımı koşulunu (timeout condition) tetikleyerek farklı bir hikaye dalına geçen Quick Time Event mekanikleri.
*   **Koşullu Kilit Mekanizmaları (Boolean Logic):** Hikayenin önceki aşamalarında elde edilen eşyalara veya bilgilere (örneğin "Gizli Harita"yı bulma durumuna) göre True/False mantığıyla dinamik olarak açılıp kapanan gizli menü seçenekleri.
*   **Etkileşimli Girdi ve Veri İşleme (String Manipulation):** Oyuncunun klavyeden metin girişi yapmasını gerektiren bilmece sistemleri. Girilen veriler, büyük/küçük harf duyarlılığı sorunlarını önlemek amacıyla (örneğin `.lower()` fonksiyonu ile) işlenerek kontrol edilir.
*   **İşitsel İpuçları (Audio Cues):** Yön bulma ve karar verme aşamalarında çevresel ses efektlerinin stratejik bir ipucu olarak kullanıldığı duyusal mekanikler.

---

##  Klanlar ve Oynanabilir Gruplar

Oyuncu, ormanın kaderini belirlemek için 5 farklı gruptan birinin liderliğini üstlenir:

1.  **Kurt Klanı (Kraliyet Muhafızları):** Kaba kuvveti ve otoriteyi temsil eder. İsyanları bastırmak ve gücü korumak üzerine kurulu hızlı refleksler gerektirir.
2.  **Baykuş Klanı (Bilge Danışmanlar):** Siyaset, şantaj ve zekayı temsil eder. Oynamak için klavye girdileriyle şifre/bilmece çözmek gerekir.
3.  **Sincap Klanı (Toplayıcılar):** Ormanın ezilen işçi sınıfıdır. Gizlilik, harita kullanımı ve kilitli seçenekleri bularak hayatta kalmaya odaklanır.
4.  **Böcek Klanı (Yeraltı Gücü):** Dış dünyadan izole, koloniyi yönetmeye odaklanan ve sıkı bir "Erzak Yönetimi" gerektiren krallık.
5.  **Geyik Klanı (Barışçıl Direniş):** Tehlikelerden kaçmak ve doğru yönü bulmak için doğanın seslerini (işitsel ipuçları) dinlemeye odaklanır.

---

##  Kullanılan Teknolojiler

*   **Oyun Motoru:** Ren'Py Visual Novel Engine
*   **Programlama Dili:** Python (Arka plan mantığı, karar ağaçları, veri tipleri ve UI için)
*   **Geliştirme Ortamı:** Visual Studio Code

---

##  Kurulum ve Çalıştırma

1. Bilgisayarınıza [Ren'Py](https://www.renpy.org/) oyun motorunu indirin ve kurun.
2. İndirdiğiniz `The Clan War` proje klasörünü Ren'Py ana dizinine (veya projenin bulunduğu workspace klasörüne) taşıyın.
3. Ren'Py Launcher'ı açın ve sol listeden **The Clan War** projesini seçin.
4. Sağ alt kısımdaki **Launch Project** butonuna tıklayarak oyunu başlatın.

---

**Geliştirici:** Mislina Danaci
**Tarih:** Ekim 2026
