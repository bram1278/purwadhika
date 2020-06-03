# 3. masukkan nilai jari-jari
#    output : luas lingkaran ... dan keliling lingkaran ...

import math

jari2 = int(input("Masukkan nilai jari-jari :"))
x = math.pi*pow(jari2,2)
y=(2*math.pi*jari2)

print(f"Luas lingkaran adalah {round(x,2)} dan keliling lingkaran adalah {round(y,2)}")