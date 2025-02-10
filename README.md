# Chess cake

- Bu projede, FEN kodu verilen bir oyundaki en iyi hamle hesaplanmakta olup; ayrıca, konum puanı ve önde olan tarafın kazanç olasılığı gösterilmektedir.

***

- Projenin çalıştırılabilmesi için; Stockfish programının indirilmesi, "stockfish" klasörünün proje klasörü içerisine eklenmesi ve "executable file" isminin de "stockfish.exe" şeklinde olması gerekmektedir. Ayrıca, FEN kodunun yorumlanabilmesi için `chess` modülü kullanılmıştır.

- FEN kodundaki "w" veya "b" harfleri, hamle sırasının hangi oyuncuda olduğunu gösterir. Mesela "b" harfi, hamle sırasının siyah taşlarda olduğu anlamına gelir. Dolayısıyla, sorgulama yapılabilmesi için hamle sırasının beyaz taşlarda olması şart değildir.

- Hatalı FEN kodu girilmesi durumunda, "hata mesajı" alınması sağlanmıştır.

- Mat olan konumlar için, sadece "Konum" çıktısının alınması sağlanmıştır.

***

# 1. En iyi hamle

- Hesaplama süresi "5 saniye" olarak belirlenmiştir.

- Standart notasyondan farklı olarak, mesela "e4" yerine "e2e4" şeklinde çıktılar alınmaktadır.

- Hamle hesabı esnasında, "en passant" ve "rok" gibi özel hamleler de algılanabilmektedir.

***

# 2. Konum puanı

- Hesaplama derinliği "20" olarak belirlenmiştir.

- Santipiyon değeri 100'e bölünerek "konum puanı" elde edilmektedir. (Mesela "300 santipiyon = 3 puan" gibi.)

- Sonucun "eksi" çıkması, siyah taşların avantajlı olduğunu gösterir.

- Kaçınılmaz mat (unavoidable mat) konumlarında, mesela "4 hamlede mat" gibi çıktılar alınmaktadır ve bu sonuçlarda "negatif sayı" yoktur.

***

# 3. Kazanç olasılığı

- Kazanç olasılığı için "sigmoid büyüme eğrisi" kullanılmıştır. Konum puanı ne kadar yüksek ise, payda da o kadar küçülür ve kazanma olasılığı da o oranda 1'e (yani %100'e) yaklaşır.

- Gerçekçi bir olasılık hesabı için "k" sabiti "0.4" kabul edilmiştir.

***
***
***

# Düzeltilecek veya eklenecek özellikler

- Kaçınılmaz mat (unavoidable mat) konumlarında hangi tarafın önde olduğu gösterilecek.

- Berabere biten oyunlar için farklı bir çıktı alınması sağlanacak.