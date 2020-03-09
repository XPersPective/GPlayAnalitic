# GPlayAnalitic

GPlayAnalitic, hangi uygulamayı yapmalıyım yada trend  uygulamalar neler gibi sorulara cevap olması amaçıyla yazdığım deneysel bir çalışmadır. 

* girilen anahtar kelime için gplay store de arama yapar ve bulunan sonuçların foto dahil uygulama bilgilerini getirir ve veritabanına kaydeder. 

* gplay/googlePlaySearch.py içindeki      def googlePlaySearchRun(self, aramaSozcugu: str, maxForTest=10): fonksiyonunda
varsayılan getirilecek sonuç değerini(yani maxForTest i) 0 yaparsanız tum sonuçları getirir. ilk deneme için  maxForTest değerini 5 gibi bir rakam verip deneyebilirsiniz.
denemem sonucunda 250 gibi bir soncu bi kaç saatte getirdi taktir size kalmış.

* Önemli yanı uygulamanın ilk çıkış tarihini içeriyor ve günlük ortalama indirilme miktarını gösteriyor oluşu bu sayede yeni trendleri yakalamak mümkün.
programın yazımında performanstan cok verilerin sağlıklı bişekilde getirilmesine öncelik verdim biraz acele yazılmış bir uygulama. verileri işleme, analiz  ve grafikleştirme gibi kısımları eklemeyi düşünüyordum pek mümkün olmayacak gibi bu yüden en azından birinlerine faydalı olursa diye bu haliyle paylaşıyorum.


* dosyayı herhangi bir yere kopyalayın ve apprun.exe tıklayın ve arama yapın.
program çalıştıgında firefox tarayıcısı calışacak sağlıklı çalışması için simge durumuna küçültmeyin.(önemli),
Söz konusu arama için işlem tamamlanmadan iptal edilirse, indirilen resimler ve  bilgiler kaydedilmiş dahi olsa silinir.(sadece söz konusu arama için)
program kötü amaçlı hiç bir kod barındırmıyor bunu kaynak kodundan görebilirsiniz zira kaynak kodlarını dll ye cevirmedim.
uygulama dışında kitap film gibi store de bulunan diğer kategorideki içerikleri sağlıklı bir şekilde getirmeyecektir zira programın hedefi uygulamalar.(oyun arama kısmını test etmedim.)

Rutin uyarı: programın kullanımıyla ilgili tüm sorumluluk kullanıcıya aittir. program ticari olarak dağıtılamaz. Genel fikir vermesi için deneysel amaçlı yazılmıltır. 

Yararlı olması dileğiyle...https://flutterdersleri.com/  
