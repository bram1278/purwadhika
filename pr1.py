# Soal 1
# Sembilan belas tahun yang lalu umur anak setengah tahun lebih muda dari seperempat umur ibunya.
# Umur anak sekarang 19 tahun lebih tua dari sepertujuh umur ibunya
# Output : Umur Ibu saat melahirkan anaknya
# oleh : Albertus Bramantyo
 
# bedawaktu = 19
# umuranakdulu = umuribudulu/4 - 0.5
# umuranakdulu = umuranakkini - bedawaktu
# umuranakkini = umuranakdulu + bedawaktu
# umuranakkini = 19 + (umuribukini/7)
# umuranakdulu + bedawaktu = 19 + (umuribukini/7)
# umuranakdulu = 19 + (umuribukini/7) - bedawaktu
# umuribudulu/4 - 0.5 = 19 + (umuribukini/7) - bedawaktu
# umuribudulu/4 = (umuribukini/7) + 0.5 
# umuribudulu = (umuribukini * 4/7) + 0.5
# umuribudulu = umuribukini - bedawaktu
# umuribukini - bedawaktu = (umuribukini * 4/7) + 0.5
# umuribukini * (3/7) = bedawaktu + 0.5
# umuribukini = (bedawaktu + 0.5) * (7/3)
# umuribuhamil = umuribukini - umuranakkini

bedawaktu = 19
umuribukini = float((bedawaktu + 0.5) * (7/3))
umuranakkini = 19 + (umuribukini/7)
umuribuhamil = umuribukini - umuranakkini

print(f"Umur ibu saat hamil adalah {umuribuhamil} ")