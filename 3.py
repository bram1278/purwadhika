x = 10

x += 1
x -= 1
x *= 2
x %= 2

x = x + 1
x = x - 1
x = x * 2

print(10 == 5) # 10 tidak sama dengan 5, FALSE
print(10 > 5) # 10 lebih besar dari 5, TRUE
print(10 < 5)
print(10 >= 5)
print(10<=5)

a = 10
b = "10"

print(a==b) # FALSE karena a adalah integer dan b adalah string

print(a==int(b)) # TRUE karena b diubah menjadi integer

print(str(a)==b) # TRUE karena a diubah menjadi string

# kondisi 1 and kondisi 2 

# And = hasil TRUE jika semua kondisi TRUE
# Or = hasil TRUE jika salah satu kondisi bernilai TRUE
# boolean and boolean
# True/False and True/False

# print(not True)

kondisi1 = 10 > 5
kondisi2 = 5 < 2
a = 10

print(kondisi1 and kondisi2)
print(10 != 2) # tidak sama dengan
print(10 == 2) # sama dengan

# IF kondisi : 

nilai = 80

if nilai > 70 : 
    print("Anda Lulus")
elif nilai < 40: # else if
    print("Anda Remidial")
else:
    print("Anda Tidak Lulus")

single = True
kerja = True

if single and kerja :
    print("Anda kurang bergaul")
elif single and not kerja :
    print("Anda harus cari kerja")
elif not single and not kerja:
    print("CARI KERJA")
else:
    print("Anda Taken")

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

# Lat 2: 
# input : masukkan angka
# kondisi : cek angka
# output : angka yang anda masukkan (angka) adalah angka GENAP / GANJIL

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