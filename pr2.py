# Soal 2
# Jumlah umur andi dan umur ayahnya sekarang adalah 50 tahun.
# 4 tahun yang lalu umur ayah andi 6 kali umur andi.
# Output : Umur andi dan umur ayah saat ini adalah : ...
# oleh : Albertus Bramantyo

# bedawaktu = 4
# andikini + ayahkini = 50
# ayahdulu = 6 * andidulu
# ayahdulu = ayahkini - bedawaktu
# 6 * andidulu = ayahkini - bedawaktu
# ayahkini = 6 * andidulu + bedawaktu
# ayahkini = 6 * (andikini - bedawaktu) + bedawaktu
# ayahkini = 6 * andikini - 5 * bedawaktu
# andikini + ayahkini = 50
# andikini + 6 * andikini - 5 * bedawaktu = 50
# 7 * andikini = 50 + 5 * bedawaktu
# andikini = (50 + 5 * bedawaktu)/7
# ayahkini = 6 * andikini - 5 * bedawaktu

bedawaktu = 4
andikini = (50 + 5 * bedawaktu)/7
ayahkini = 6 * andikini - 5 * bedawaktu

print(f"Umur Andi saat ini adalah {andikini}, Umur ayah saat ini adalah {ayahkini}")

