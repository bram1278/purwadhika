### Function
# def nama function (): ## memberi nama kepada fungsi yang kita buat, tujuannya agar bisa kita panggil
#     program nya

## fungsi ...

## pakai fungsi

# print("Halo selamat pagi Joni")
# print("Apa kabar hari ini")

# print("Halo selamat pagi Siti")
# print("Apa kabar hari ini")

# print("Halo selamat pagi Andre")
# print("Apa kabar hari ini")

# def salam(nama):
#     print(f"Halo selamat pagi {nama}")
#     print("Apa kabar hari ini")

# salam("Joni")
# salam("Siti")
# salam("Andre")

## Global Variabel (variabel yang ada di luar fungsi), cth:
a = 12
b = []

## Local Variabel

def namabuah():
    print("Ini buah Jeruk")

def hargabuah(): ## Fungsi bisa tidak memakai variabel atau memakai variabel
    namabuah()
    print("Harga jeruk per kilo 60.000")

def hargatotal(kilo): ## kilo adalah variabel lokal yang nilainya kita tentukan
    hargabuah()
    c = 20
    harga = kilo * 60000*a*c  
    print(f"Harga buah {kilo} kg, adalah {harga}")

hargatotal(4) ## Nilai 4 akan dimasukkan ke dalam variabel kilo
## kilo = 4

# print(a+c) ## error nama c tidak didefinisi, karena c variabel lokal

def BMI2(berat, tinggi):
    hasil = berat / (tinggi ** 2)
    print("nilai BMI : ",hasil)

# BMI(60, 1.85) ## berat = 60, tinggi = 1.85
# BMI(1.85,60) ## hasilnya beda dengan BMI(60,1.85)
# ##keyword
# BMI(tinggi=1.85, berat=60) 
# ## nilai default
# BMI() ## error karena butuh 2 variabel berat dan tinggi

## Return Function ## return/kembalian adalah ketika fungsi jalan

print(5+5) ## nilai kembalian 10

def BMI(berat, tinggi): ## Tidak bisa ada dua fungsi yang bernama sama
    hasil = berat / (tinggi ** 2)
    print("nilai BMI : ")
    return hasil ## kembaliannya hanya nilai "hasil"

BMI(58, 1.75) ## hasil penghitungan tidak ditampilkan
data = BMI(58, 1.75)
print(data)

# def gangen(angka):
#     if angka%2 == 0:
#         print("Angka Genap")
#     else:
#         print("Angka Ganjil")

# gangen(980)
# gangen(58)
# gangen(15)
# gangen(97)

def gangen(angka): # Hasilnya tidak ada "Angka Genap" atau "Angka Ganjil" yang diprint
    if angka%2 == 0:
        return("Angka Genap")
    else:
        return("Angka Ganjil")

print(gangen(980))
print(gangen(58))
print(gangen(15))
print(gangen(97))

# masukkan email :

# fungsi cek email

# def cek email(namaemail):

# namalist=[isinya daftar email]
# for i in namalist:
#     cekemail(i)

# nama = masukkan email : ....... 
# cekemail(nama)
# cekemail(email)
# cekemail(nama)
# cekemail(email)
# cekemail(nama)
# cekemail(email)
# cekemail(nama)
# cekemail(email)

# import rumus # import dari save-an file python yang lain 
# rumus.luas(20)

# import rumus as r 
# r.luas(15)

from rumus import luas
luas(23)

def pangkat(angka1, angka2):
    print(angka1 ** angka2)

pangkat(2,3)

## Latihan

# Pakai def dengan return function
# Lat 1:
# Pakai def : 
# Kalkulator (+,-, /, *)

# inputan:
# input angka 1 : 8
# input angka 1 : 10
# masukkan operator : +

# output : hasil penjumlahan 8 + 10 = 18

# Lat 2:
# pakai dict dan def:
# kamus = IND - ENG untuk hari 

# Translator (Encoder-Decoder Kode Morse)
# Silakan masukkan kalimat : Aman
# Output nya: (kode morse nya) .- / - - / .-/ -.

# Silakan masukkan kalimat: .- / - - / .-/ -.
# Output nya: Aman
# Tidak ada pilihan apakah ingin translasi Indo ke morse atau morse ke Indo

# Lat 3:
# Pakai def
# Fizz Buzz
# input masukkan angka :
# outputnya : 
# angka yang habis dibagi 3 : Fizz
# angka yang habis dibagi 5 : Buzz
# angka yang habis dibagi 3 dan 5: Fizz Buzz
# cth output: 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz

# Lat 4: 
# pakai def: 
# Caesar cipher
# masukkan kata : Joni
# masukkan angka : 2
# hasil caesar cipher : Lnpk (huruf maju dua)

# masukkan kata : Joni
# masukkan angka : -2
# hasil caesar cipher : hmlg  (huruf mundur dua)

# Latihan 5
# pakai def dan dict
# Batas maksimal 4000
# keluar notif: angka di luar jangkauan
# Translator (Encoder-Decoder Angka Romawi)
# Silakan masukkan angka : 2018
# Output nya: (angka romawinya) MMXVIII

# Silakan masukkan kalimat: MMXVIII
# Output nya: 2018
# Tidak ada pilihan apakah ingin translasi nomor ke romawi atau romawi ke nomor

# Kirim Email

## Lat 6 
# Pakai def function
# konversi angka digital
# Masukkan angka : 9
# outputnya
#  __
# |__|
#  __|

## Rekursive Function # ada function di dalam function tetapi berulang-ulang

# Faktorial :
# 2! = 2 x 1
# 3! = 3 x 2 x 1
# 5! = 5 x 4 x3 x 2 x 1

def faktorial(x):
    if (x <= 2):
        return x
    else:
        return x * faktorial(x-1) 

print(faktorial(2))
print(faktorial(3))
print(faktorial(4))