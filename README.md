# Chess cake

- Bu projede, FEN kodu verilen bir oyundaki en iyi hamle, konum puanı ve önde olan tarafın kazanç olasılığı gösterilmektedir.

***

- Projenin çalıştırılabilmesi için; Stockfish programının "stockfish" isimli klasör içerisinde yer alması ve "executable file" isminin de "stockfish.exe" şeklinde olması gerekmektedir.

- FEN kodu için "input" sistemi mevcuttur.

- FEN kodunun yorumlanabilmesi için `chess` modülü kullanılmıştır.

- FEN kodundaki "w" veya "b" harfleri, hamle sırasının hangi oyuncuda olduğunu ("white" veya "black") gösterir. Dolayısıyla, FEN kodunun incelenebilmesi için hamle sırasının beyaz taşlarda olması şart değildir.

- Hatalı FEN kodu girilmesi durumunda, "hata mesajı" alınması sağlanmıştır.

- Mat olan konumlarda, "Konum" dışındaki diğer çıktıların alınması engellenmiştir.

***

# 1. En iyi hamle

- Hesaplama süresi "5 saniye" olarak belirlenmiştir.

- Standart notasyondan farklı olarak, mesela "e4" yerine "e2e4" şeklinde çıktılar alınmaktadır.

- Hesaplama esnasında, "en passant" ve "rok" gibi özel hamleler de algılanabilmektedir.

***

# 2. Konum puanı

- Hesaplama derinliği "20" olarak belirlenmiştir.

- Santipiyon değeri 100'e bölünerek "konum puanı" elde edilmektedir.

- Sonucun "eksi" çıkması, siyah taşların avantajlı olduğunu gösterir.

- Kaçınılmaz mat (unavoidable mat) konumlarında, mesela "4 hamlede mat!" gibi çıktılar alınmaktadır ve bu çıktılarda "negatif sayı" yoktur.

***

# 3. Kazanç olasılığı

- Kazanç olasılığı için "sigmoid büyüme eğrisi" kullanılmıştır.

- Gerçekçi bir olasılık hesabı için, sigmoid büyüme eğrisindeki "k" sabiti "0.4" olarak ayarlanmıştır.

***
***
***

# Düzeltilecek veya eklenecek özellikler

- Kaçınılmaz mat (unavoidable mat) konumlarında, hangi tarafın önde olduğu gösterilecek.

- Berabere biten oyunlar için farklı bir çıktı alınması sağlanacak.