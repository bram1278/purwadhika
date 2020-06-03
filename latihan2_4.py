# 4. "Hari, hari ini tidak mAsuk SEKOLAH"
#     hitung karakter A = 5

#     input : masukkan kalimat
#     input : masukkan karakter
#     output : jumlah karakter (karakter)
#     dalam (kalimat) adalah ...

kalimat = input("Masukkan kalimat: ")
kecil = kalimat.lower()
karakter = input("Masukkan karakter: ")
karakterkecil = karakter.lower()
count = kecil.count(karakter)

print(f"Jumlah huruf {karakter} dalam kalimat {kalimat} adalah {count} ".format(karakter,kalimat,count))
