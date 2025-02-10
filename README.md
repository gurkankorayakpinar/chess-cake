# Chess cake

- Bu projede, FEN kodu verilen bir oyundaki "en iyi hamle" hesaplanmakta ve "konum puanı" gösterilmektedir.

***

- Projenin çalıştırılabilmesi için; Stockfish programının indirilmesi, "stockfish" klasörünün proje klasörü içerisine eklenmesi ve "executable file" isminin de "stockfish.exe" şeklinde olması gerekmektedir. Ayrıca, FEN kodunun yorumlanabilmesi için `chess` modülü kullanılmıştır.

- FEN kodundaki "w" veya "b" harfleri, hamle sırasının hangi oyuncuda olduğunu gösterir. Mesela "b" harfi, hamle sırasının siyah taşlarda olduğu anlamına gelir. Dolayısıyla, sorgulama yapılabilmesi için hamle sırasının beyaz taşlarda olması şart değildir.

- Hatalı FEN kodu girilmesi durumunda, "hata mesajı" alınması sağlanmıştır.

***

# 1. En iyi hamle

- Hesaplama süresi "5 saniye" olarak belirlenmiştir.

- Standart notasyondan farklı olarak, mesela "e4" yerine "e2e4" şeklinde çıktılar alınmaktadır.

- Hesaplama esnasında, "en passant" ve "rok" gibi özel hamleler de algılanabilmektedir.

***

# 2. Konum puanı

- Hesaplama derinliği "20" olarak belirlenmiştir.

- Sonucun "eksi" çıkması, siyah taşların avantajlı olduğunu gösterir.

- Kaçınılmaz mat (unavoidable mat) konumlarında, mesela "4 hamlede mat" gibi çıktılar alınmaktadır ve bu sonuçlarda "negatif sayı" yoktur.