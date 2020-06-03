# PR oleh Albertus Bramantyo

# Soal 1
# Sembilan belas tahun yang lalu umur anak setengah tahun lebih muda dari seperempat umur ibunya.
# Umur anak sekarang 19 tahun lebih tua dari sepertujuh umur ibunya
# Output : Umur Ibu saat melahirkan anaknya
 
# bedawaktu1 = 19
# rasiodulu1 = 4
# rasiokini1 = 7
# selisihdulu1 = 0.5
# selisihkini1 = 19
# umuranakdulu = umuribudulu/rasiodulu1 - selisihdulu1
# umuranakdulu = umuranakkini - bedawaktu1
# umuranakkini = umuranakdulu + bedawaktu1
# umuranakkini = selisihkini1 + (umuribukini/rasiokini1)
# umuranakdulu + bedawaktu1 = selisihkini1 + (umuribukini/rasiokini1)
# umuranakdulu = selisihkini1 + (umuribukini/rasiokini1) - bedawaktu1
# umuribudulu/rasiodulu1 - selisihdulu1 = selisihkini1 + (umuribukini/rasiokini1) - bedawaktu1
# umuribudulu/rasiodulu1 = selisihkini1 + (umuribukini/rasiokini1) - bedawaktu1 + selisihdulu1 
# umuribudulu = (selisihkini1 + (umuribukini/rasiokini1) - bedawaktu1 + selisihdulu1)*rasiodulu1
# umuribudulu = umuribukini - bedawaktu1
# umuribukini - bedawaktu1 = (selisihkini1 + (umuribukini/rasiokini1) - bedawaktu1 + selisihdulu1)*rasiodulu1
# umuribukini = bedawaktu1 + (selisihkini1 + (umuribukini/rasiokini1) - bedawaktu1 + selisihdulu1)*rasiodulu1
# umuribukini = bedawaktu1 + (umuribukini*rasiodulu1/rasiokini1) + (selisihkini1 - bedawaktu1 + selisihdulu1)*rasiodulu1
# umuribukini * (1 - rasiodulu1/rasiokini1) = bedawaktu1 + (selisihkini1 - bedawaktu1 + selisihdulu1)*rasiodulu1
# umuribukini = (bedawaktu1 + (selisihkini1 - bedawaktu1 + selisihdulu1)*rasiodulu1) * (rasiokini1/(rasiokini1-rasiodulu1))
# umuranakkini = selisihkini1 + (umuribukini/rasiokini1)
# umuribuhamil = umuribukini - umuranakkini

bedawaktu1 = 19
rasiodulu1 = 4
rasiokini1 = 7
selisihdulu1 = 0.5
selisihkini1 = 19
umuribukini = (bedawaktu1 + (selisihkini1 - bedawaktu1 + selisihdulu1)*rasiodulu1) * (rasiokini1/(rasiokini1-rasiodulu1))
umuranakkini = selisihkini1 + (umuribukini/rasiokini1)
umuribuhamil = umuribukini - umuranakkini

print(f"Umur ibu saat hamil adalah {umuribuhamil} ")

# Soal 2
# Jumlah umur andi dan umur ayahnya sekarang adalah 50 tahun.
# 4 tahun yang lalu umur ayah andi 6 kali umur andi.
# Output : Umur andi dan umur ayah saat ini adalah : ...
# oleh : Albertus Bramantyo

# bedawaktu2 = 4
# totalkini = 50
# rasiodulu2 = 6
# ayahdulu = rasiodulu2 * andidulu
# ayahdulu = ayahkini - bedawaktu2
# rasiodulu2 * andidulu = ayahkini - bedawaktu2
# ayahkini = rasiodulu2 * andidulu + bedawaktu2
# ayahkini = rasiodulu2 * (andikini - bedawaktu2) + bedawaktu2
# ayahkini = rasiodulu2 * andikini + (1 - rasiodulu2) * bedawaktu2
# andikini + ayahkini = totalkini
# andikini + rasiodulu2 * andikini + (1 - rasiodulu2) * bedawaktu2 = totalkini
# andikini * (1 + rasiodulu2) = totalkini - ((1 - rasiodulu2) * bedawaktu2)
# andikini = (totalkini - ((1 - rasiodulu2) * bedawaktu2))/(1 + rasiodulu2)
# ayahkini = totalkini - andikini

bedawaktu2 = 4
totalkini = 50
rasiodulu2 = 6
andikini = (totalkini - ((1 - rasiodulu2) * bedawaktu2))/(1 + rasiodulu2)
ayahkini = totalkini - andikini

print(f"Umur Andi saat ini adalah {andikini}, Umur ayah saat ini adalah {ayahkini}")