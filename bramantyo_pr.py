# PR oleh Albertus Bramantyo

# Soal 1
# Sembilan belas tahun yang lalu umur anak setengah tahun lebih muda dari seperempat umur ibunya.
# Umur anak sekarang 19 tahun lebih tua dari sepertujuh umur ibunya
# Output : Umur Ibu saat melahirkan anaknya
 
# bedawaktu1 = 19
# umuranakdulu = umuribudulu/4 - 0.5
# umuranakdulu = umuranakkini - bedawaktu1
# umuranakkini = umuranakdulu + bedawaktu1
# umuranakkini = 19 + (umuribukini/7)
# umuranakdulu + bedawaktu1 = 19 + (umuribukini/7)
# umuranakdulu = 19 + (umuribukini/7) - bedawaktu1
# umuribudulu/4 - 0.5 = 19 + (umuribukini/7) - bedawaktu1
# umuribudulu/4 = (umuribukini/7) + 0.5 
# umuribudulu = (umuribukini * 4/7) + 0.5
# umuribudulu = umuribukini - bedawaktu1
# umuribukini - bedawaktu1 = (umuribukini * 4/7) + 0.5
# umuribukini * (3/7) = bedawaktu1 + 0.5
# umuribukini = (bedawaktu1 + 0.5) * (7/3)
# umuribuhamil = umuribukini - umuranakkini

bedawaktu1 = 19
umuribukini = (bedawaktu1 + 0.5) * (7/3)
umuranakkini = 19 + (umuribukini/7)
umuribuhamil = umuribukini - umuranakkini

print(f"Umur ibu saat hamil adalah {umuribuhamil} ")

# Soal 2
# Jumlah umur andi dan umur ayahnya sekarang adalah 50 tahun.
# 4 tahun yang lalu umur ayah andi 6 kali umur andi.
# Output : Umur andi dan umur ayah saat ini adalah : ...
# oleh : Albertus Bramantyo

# bedawaktu2 = 4
# andikini + ayahkini = 50
# ayahdulu = 6 * andidulu
# ayahdulu = ayahkini - bedawaktu2
# 6 * andidulu = ayahkini - bedawaktu2
# ayahkini = 6 * andidulu + bedawaktu2
# ayahkini = 6 * (andikini - bedawaktu2) + bedawaktu2
# ayahkini = 6 * andikini - 5 * bedawaktu2
# andikini + ayahkini = 50
# andikini + 6 * andikini - 5 * bedawaktu2 = 50
# 7 * andikini = 50 + 5 * bedawaktu2
# andikini = (50 + 5 * bedawaktu2)/7
# ayahkini = 6 * andikini - 5 * bedawaktu2

bedawaktu2 = 4
andikini = (50 + 5 * bedawaktu2)/7
ayahkini = 6 * andikini - 5 * bedawaktu2

print(f"Umur Andi saat ini adalah {andikini}, Umur ayah saat ini adalah {ayahkini}")