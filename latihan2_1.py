# Latihan :
# 1. input : masukkan jumlah hari?
#    output : nyatakan dalam tahun, bulan, hari

# 4. "Hari, hari ini tidak mAsuk SEKOLAH"
#     hitung karakter A = 5

#     input : masukkan kalimat
#     input : masukkan karakter
#     output : jumlah karakter (karakter)
#     dalam (kalimat) adalah ...

import math

hari = int(input("Masukkan jumlah hari :"))
hitungtahun = math.floor(hari/360)
sisa = hari % 360
hitungbulan = math.floor(sisa/30)
sisa1 = sisa % 30
hitungminggu = math.floor(sisa1 / 7)
hitunghari = math.floor(sisa1/1)

print(f"{hari} hari adalah {hitungtahun} tahun, {hitungbulan} bulan, {hitungminggu} minggu, {hitunghari} hari ")