# ==========================================
# 1. GÖRSELLERİ TANIMLAMA (Tam Ekran)
# ==========================================
image bg orman:
    "orman2.jpg"
    size (1920, 1080)
image bg yeralti:
    "bug underworld colony.jpg"
    size (1920, 1080)
image bg kurt:
    "wolf.jpg"
    size (1920, 1080)
image bg baykus:
    "owl scarry stare.jpg"
    size (1920, 1080)
image bg sincap:
    "sincap.jpg"
    size (1920, 1080)
image bg bocek:
    "bug.jpg"
    size (1920, 1080)
image bg geyik:
    "deer.jpg"
    size (1920, 1080)

# ==========================================
# 2. DEĞİŞKENLER (Oyun İçi Mantık)
# ==========================================
default erzak = 100
default saygi = 50
default gizli_harita = False

# ==========================================
# 3. ÖZEL EKRANLAR (UI / Arayüz)
# ==========================================
screen durum_paneli():
    frame:
        xalign 0.98
        yalign 0.02
        vbox:
            text "Erzak: [erzak]" size 30 color "#FFA500"
            text "Saygı: [saygi]" size 30 color "#87CEFA"

screen zamanlayici(sure, hedef_etiket):
    text "HIZLI KARAR VER!" xalign 0.5 yalign 0.1 size 50 color "#ff0000"
    timer sure action Jump(hedef_etiket)


# ==========================================
# OYUN BAŞLANGICI
# ==========================================
label start:
    scene bg orman with dissolve
    play music "audio/orman_sesi.mp3" fadein 2.0
    show screen durum_paneli
    
    $ oyuncu_ismi = renpy.input("Karakterinizin adını girin (Boş bırakırsanız 'Yabancı' olursunuz):").strip()
    if oyuncu_ismi == "":
        $ oyuncu_ismi = "Yabancı"

    "Ormanda Büyük Kıtlık başladı. Erzak ve Saygı seviyeni dengede tutarak hayatta kalmalısın."

    menu:
        "Kaderini Belirleyecek Klanı Seç:"
        "Kurt Klanı (Süreli Karar Mekaniği)":
            $ klan = "Kurt"
            jump kurt_hikayesi
        "Baykuş Klanı (Bilmece Mekaniği)":
            $ klan = "Baykuş"
            jump baykus_hikayesi
        "Sincap Klanı (Kilitli Seçenek Mekaniği)":
            $ klan = "Sincap"
            jump sincap_hikayesi
        "Böcek Klanı (Erzak Yönetimi)":
            $ klan = "Böcek"
            jump bocek_hikayesi
        "Geyik Klanı (Sesli İpucu Mekaniği)":
            $ klan = "Geyik"
            jump geyik_hikayesi


# ==========================================
# HİKAYE 1: KURT KLANI
# ==========================================
label kurt_hikayesi:
    scene bg kurt with dissolve
    play sound "audio/kurt_sesi.mp3"
    "Kurt klanının liderisin. Bir gece çadırında uyurken dışarıdan sesler geldi."
    "Sana suikast düzenliyorlar! Üzerine mızraklı bir sincap atladı!"
    
    show screen zamanlayici(3.0, "kurt_gec_kaldi")
    
    menu:
        "Sağa doğru yuvarlanıp kaç!":
            hide screen zamanlayici
            $ saygi += 20
            "Kıl payı kurtuldun! Liderlik reflekslerin saygını artırdı."
            jump kurt_devam
            
        "Kılıcını çekip savaş!":
            hide screen zamanlayici
            $ erzak -= 20
            $ saygi += 30
            "Saldırganı hakladın ama çadırın zarar gördü."
            jump kurt_devam

label kurt_gec_kaldi:
    hide screen zamanlayici
    "Çok yavaş kaldın... Suikastçi seni gafil avladı. (Son: Uyuyan Kral)"
    jump oyun_sonu

label kurt_devam:
    "Suikastçi sincabı esir aldın. Onu kimin gönderdiğini öğrenmen gerekiyor."
    menu:
        "Ona rüşvet olarak kendi erzağından teklif et.":
            $ erzak -= 30
            "Erzakları görünce, onu Baykuşların kiraladığını itiraf etti!"
            menu:
                "Baykuşlara savaş aç!":
                    "Baykuşların yuvalarını dağıttın. Ormanın tek hakimi sensin ama çok kan döküldü. (Son: Kanlı Zafer)"
                    jump oyun_sonu
                "Baykuşlara şantaj yapıp erzaklarını al.":
                    $ erzak += 60
                    "Siyaseti öğrendin! Savaşmadan ormanın en zengini oldun. (Son: Zeki Kurt)"
                    jump oyun_sonu
        "Onu ormandan sürgün et ve güvenliği artır.":
            $ saygi += 20
            "Kimse klanına bir daha saldırmaya cesaret edemedi. Ormanda korku ve saygı ile hükmettin. (Son: Katı Muhafız)"
            jump oyun_sonu


# ==========================================
# HİKAYE 2: BAYKUŞ KLANI
# ==========================================
label baykus_hikayesi:
    scene bg baykus with dissolve
    play sound "audio/baykus_sesi.mp3"
    "Yüce Ağaç'taki Baykuş Meclisi'ne girmek istiyorsun. Muhafız seni durdurdu."
    "Muhafız: 'Meclise sadece zeki olanlar girebilir. Şu bilmecenin cevabını söyle:'"
    "Muhafız: 'Konuşmadan seslenir, kanatsız uçar, dişsiz ısırır. Nedir bu?'"
    
    $ cevap = renpy.input("Klavyeden cevabı yazın:").strip().lower()
    
    if cevap == "rüzgar" or cevap == "ruzgar":
        $ saygi += 40
        "Muhafız: 'Doğru cevap!' İçeri alındın."
        "Meclis içten içe kaynıyor. Kurt klanı elinizdeki tüm erzağı vergi olarak istiyor!"
        menu:
            "Kurtlara zehirli mantarlar verelim. (Karanlık Plan)":
                $ saygi -= 20
                "Plan işe yaradı, Kurtlar zayıfladı ama ormandaki diğer hayvanlar sizden korkup uzaklaştı. (Son: Yalnız Zehir)"
                jump oyun_sonu
            "Böceklerle anlaşıp erzakları yeraltına saklayalım.":
                $ erzak -= 10
                "Kurtlar geldiğinde depoları boş buldu. Siz ise yeraltında güvendesiniz. (Son: Derin Strateji)"
                jump oyun_sonu
    else:
        $ saygi -= 30
        "Muhafız: 'Yanlış cevap! Cahillerin meclisimizde yeri yok!' Yüce Ağaç'tan kovuldun. (Son: Kovulan Cahil)"
        jump oyun_sonu


# ==========================================
# HİKAYE 3: SİNCAP KLANI
# ==========================================
label sincap_hikayesi:
    scene bg sincap with dissolve
    "Erzak ararken eski bir sandık buldun."
    menu:
        "Sandığı aç.":
            "İçinden ormanın yeraltı tünellerini gösteren gizli bir harita çıktı!"
            $ gizli_harita = True
            $ erzak += 10
        "Sandığı umursama, erzak aramaya devam et.":
            "Sadece birkaç ceviz bulabildin."
            $ erzak += 30
            
    "Birkaç gün sonra Kurt ordusu sincap köyüne saldırdı! Köşeye sıkıştınız."
    menu:
        "Savaşarak direnmeye çalış.":
            "Çok küçüksünüz, direnişiniz kırıldı. (Son: Kaybedilmiş Savaş)"
            jump oyun_sonu
        "Haritadaki gizli tüneli kullanarak kaç." if gizli_harita:
            $ saygi += 50
            "Harita sayesinde tüm klanı yeraltına kaçırdın! Artık klanın kahramanısın. (Son: Zeki Kurtarıcı)"
            jump oyun_sonu


# ==========================================
# HİKAYE 4: BÖCEK KLANI
# ==========================================
label bocek_hikayesi:
    scene bg yeralti with dissolve
    "Yeraltındaki devasa koloniyi yönetiyorsun. Yeryüzünden gelen mülteciler erzaklarınızı tüketiyor."
    
    menu:
        "Mültecilere acıyıp erzağı paylaş.":
            $ erzak -= 60
            $ saygi += 40
            "Herkes seni çok sevdi ama erzaklarınız dibe vurdu."
        "Mültecileri dışarı at!":
            $ erzak += 20
            $ saygi -= 40
            "Erzaklarınız korundu ama işçiler bu kadar acımasız olmandan dolayı isyan etmeye başladı."
            menu:
                "İşçileri zorla çalıştır. (Tiranlık)":
                    $ saygi -= 30
                    "Kendi klanın sana karşı ayaklandı ve seni tahttan indirdi! (Son: Zalimin Düşüşü)"
                    jump oyun_sonu
                "Depolardan onlara ekstra pay dağıtarak gönüllerini al.":
                    $ erzak -= 40
                    $ saygi += 50
                    "Biraz erzak kaybettin ama isyanı durdurup koloniyi bir arada tuttun. (Son: Dengeli Siyasetçi)"
                    jump oyun_sonu
            
    if erzak <= 20:
        "Kalan azıcık erzak uğruna koloni birbirine saldırdı... (Son: Açlık Kaosu)"
        jump oyun_sonu
    else:
        "Zorlukları atlattınız. Yeraltı artık tamamen size ait. (Son: Sağlam İrade)"
        jump oyun_sonu


# ==========================================
# HİKAYE 5: GEYİK KLANI
# ==========================================
label geyik_hikayesi:
    scene bg orman with dissolve
    "Karanlık ormanda süründen ayrı düştün. Zifiri karanlık."
    "Birden sağ tarafındaki çalılıklardan bir ses duydun!"
    
    play sound "audio/kurt_sesi.mp3"
    "Sesin ne olduğunu iyi düşün. Yırtıcıysa aksi yöne kaç, değilse bekle."
    
    menu:
        "Sesin Kurt olduğuna eminim, hemen Sola kaç!":
            $ erzak -= 10
            $ saygi += 30
            "Doğru bildin! Karanlıkta yem olmaktan kurtuldun."
            "Koşarken bir vadiye ulaştın. İleride kamp ateşi yakan insanlar (avcılar) var."
            menu:
                "İnsanların kampına gizlice yaklaşıp erzaklarını çal.":
                    $ erzak += 50
                    $ saygi += 20
                    "Çok tehlikeliydi ama başardın! Çaldığın erzaklarla sürünü kış boyu yaşatacaksın. (Son: Gözüpek Kahraman)"
                    jump oyun_sonu
                "İnsanlardan uzak dur, ormanın soğuğunda kal.":
                    "Güvendesiniz ama kışı çok zor şartlarda, açlıkla savaşarak geçirdiniz. (Son: Vahşi ve Özgür)"
                    jump oyun_sonu
            
        "Bekle, o sadece bir baykuş olmalı.":
            $ saygi -= 50
            "Yanlış tahmin... Kurt sürüsü karanlıktan üzerine atladı. (Son: Yanıltıcı Sessizlik)"
            jump oyun_sonu


# ==========================================
# OYUN SONU
# ==========================================
label oyun_sonu:
    hide screen durum_paneli
    scene bg orman with dissolve
    stop music fadeout 2.0
    
    " "
    "Hikayenin sonuna ulaştın, [oyuncu_ismi]."
    "Elde Ettiğin Son Saygı: [saygi]"
    "Elde Ettiğin Son Erzak: [erzak]"
    "Oynadığın için teşekkürler!"
    return