# Lat
# Input : Masukkan nilai

# Nilai di atas 100:
# Nilai di luar jangkauan
# Nilai di bawah 0:
# Tidak bisa menerima nilai negatif

# kondisi :
# 90 ke atas grade A
# 85 ke atas grade A-
# 80 ke atas grade B
# 75 ke atas grade B-
# 70 ke atas grade C
# 65 ke atas grade D
# Di bawah itu remidial

# Output :
# Nilai anda (nilai) dan Grade anda (grade)

nilai = int(input("Masukkan nilai ujian anda: "))

if (nilai > 100):
    grade = "error luar jangkauan";
elif (nilai >= 90):
    grade = "A" ;
elif (nilai >= 85) :
    grade = "A-" ;
elif (nilai >= 80) :
    grade = "B" ;
elif (nilai >= 75) :
    grade = "B-" ;
elif (nilai >= 70) :
    grade = "C" ;
elif (nilai >= 65) :
    grade = "D" ;
elif (nilai < 0) :
    grade = "error negatif"
else :
    grade = "remidial"

print(f"Nilai anda {nilai} mendapat grade {grade}")

# alternatif1: bisa digunakan if nilai <= 100 and nilai >=0 pada baris pertama lalu gunakan if nilai >= 90, dst
# alternatif2: bisa digunakan if 90 <= nilai <= 100

# Lat 2: 
# input : masukkan angka
# kondisi : cek angka
# output : angka yang anda masukkan (angka) adalah angka GENAP / GANJIL

nilai2 = int(input("Masukkan nilai anda: "))
ceknilai = nilai2%2

if (ceknilai == 0) :
    kondisi = "GENAP";
else :
    kondisi = "GANJIL";

print(f"Angka yang anda masukkan {nilai2} adalah angka {kondisi}")

# Lat 3 :
# Rumus : IMT = massa (kg) / tinggi (m) ^ 2

# input : masukkan massa (kg)
#         masukkan tinggi (cm)
# 
# kondisi : 
# IMT < 18.5 = berat badan kurang
# 18.5 - 24.9 = berat badan ideal
# 25 - 29.9 = berat badan berlebih
# 30 - 39.9 = berat badan sangat berlebih
# IMT > 39.9 = obesitas

# output :
#  Massa : (massa) (Kg)
# Tinggi : (tinggi) (m) 
# IMT ....., BERAT BADAN ANDA IDEAL (sesuai kondisi)

massa = float(input("Masukkan massa (kg): "))
tinggi = float(input("Masukkan tinggi (cm): "))
tinggi2 = float(tinggi/100) # tidak salah, tetapi bisa gunakan tinggi2 = tinggi/100

IMT = massa/(pow(tinggi2,2))
IMT2 = round(IMT,2)

if IMT < 18.5 :
    status = "kurang";
elif IMT >= 18.5 and IMT <= 24.9 :
    status = "ideal";
elif IMT >= 25 and IMT <= 29.9 :
    status = "berlebih";
elif IMT >= 30 and IMT <= 39.9 :
    status = "sangat berlebih";
else :
    status = "obesitas";

konstantaideal1 = 18.5
konstantaideal2 = 24.9
ideal1 = konstantaideal1 * pow(tinggi2,2)
ideal1a = round(ideal1,2)
ideal2 = konstantaideal2 * pow(tinggi2,2)
ideal2a = round(ideal2,2)

print(f"IMT anda adalah {IMT2}, \n status berat badan anda adalah {status}, \n berat badan ideal anda adalah dari {ideal1a} kg hingga {ideal2a} kg ")