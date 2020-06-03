### Lambda, Map, dan Filter

# Lambda - Anonymous function, one time use (bisa dipanggil berulang-ulang jika dimasukkan ke function), small size
# Basic syntax

a = lambda argumen: print(argumen) # lambda dapat memiliki banyak argumen, tetapi hanya dapat memiliki 1 expression/fungsi/program

# a("Selamat Pagi") 

# print(a) # notif function lambda 

kuadrat = lambda x: x ** 2

# print(kuadrat(5))

def kuadrat2(x):
    return x ** 2

# print(kuadrat2(5))

pangkat = lambda x, y: x ** y

# print(pangkat(5)) # error karena hanya memasukkan 1 argumen tetapi dibutuhkan 2 argumen

# print(pangkat(5,3))

cek = lambda x: True if x%2 == 0 else False

# print(cek(39))
# print(cek(80))

cek2 = lambda x: "Angka Genap" if x%2 == 0 else "Angka Ganjil"

# print(cek2(39))
# print(cek2(80))

genap = []
ganjil = []

cek3 = lambda x: genap.append(x) if x%2 == 0 else ganjil.append(x)

# print(cek3(59)) # mendapat hasil none karena perintah lambda hanya append
# print(genap)
# print(ganjil)

#### Map, hasil dari map function berupa object map sehingga tidak dapat diakses by index maupun len atau melihat isinya
### harus dikonversi
### Basic Syntax nya
### Data iterables = list, tuple, dictionary, dll

# map(function, data iterables) ## function 1, data iterables banyaknya sesuai dengan argumen di dalam function

a = [1,2,3,4,5]
b = []

# print(kuadrat2(a)) # error karena unsupported operand type(s) for ** or pow(): 'list' and 'int'

for i in a:
    b.append(kuadrat2(i))
# print(b)
# map(kuadrat2, a) # tidak keluar hasil apa-apa karena anonymous
# print(map(kuadrat2, a)) # map object at ...
c = list(map(kuadrat2, a))
# print(c)

def pangkat2(x,y):
    return x ** y

# pangkat2(a, c) # error karena unsupported operand type(s)

# d = map(pangkat2, a) 
# print(d) # keluar map object

d = list(map(pangkat2, a,c))

# print(d)

e = list(map(pangkat2, a, list(map(kuadrat2, a)))) # di dalam map ada map
# print(e)

kuadrat3 = lambda x: x ** 2
pangkat3 = lambda x,y: x ** y

kuadrat4 = lambda x: x ** 3

i = list (map(kuadrat3, a))
i2 = list(map(lambda x: x **3, a))

f = list(map(kuadrat3, a))

g = list(map(lambda x: x ** 2,a))
g1 = list(map(lambda x: x ** 2,a))

####################################
print(f)
print(g)

####################################
h = list(map(pangkat3, a, g))
# h1 = list(map(lambda x,y: x ** y, a, g))

# h2 = list(map(lambda x,y: x ** y, a, list(map(lambda x: x ** x, a))))

h2 = list(map(lambda x,y: x ** y, list(map(lambda x: x ** 3, a)), list(map(lambda x: x ** 2, a ))))


# print(f)
# print(g)
# print(h)
# # print(h1)
# print(h2)
# print(i)
# print(i2)

jumlah = lambda x,y,z: x + y + z

k = list(map(jumlah, g1, i2, h2))
print(k)

k2 = list(map(lambda x,y,z: x + y + z, g1,i2,h2))
print(k2)

k3 = list(map(lambda x,y,z: x + y + z, list(map(lambda x: x ** 2,a)),list(map(lambda x: x **3, a)),list(map(lambda x,y: x ** y, list(map(lambda x: x ** 3, a)), list(map(lambda x: x ** 2, a ))))))
print(k3)

##### FIlter
# Basic Syntax :
# filter(function, data iterable) # hasil dari filter adalah data yang bernilai True berdasarkan function, function berupa function - comparison atau pengujian kondisi
# hanya menerima 1 data iterables, filter hanya bisa dipakai jika function mengandung pengecekan True atau False 
a = [1,2,3,4,5,6,7,8]


# s = filter(lambda x: x%2 == 0, a)

# print(s) # print object at ...

s = list(filter(lambda x: x%2 == 0, a))
print(s) # s = [2, 4, 6, 8]

u = list(filter(lambda x: x%2 == 0, a)) 

# operator yang dapat digunakan dalam function filter
# == 
# !=
# >=
# =<
# >
# <
# .isdigit
# .isalpha
# .alnum
# .islower
# .isupper

genap = []
ganjil = []

# gh = map(lambda x: genap.append(x) if x%2 == 0 else ganjil.append(x), a)

# print(gh) 
# print(genap)
# print(ganjil)

####### Reduce
## Basic Syntax
# menghasilkan 1 data
# faktorial 1 x 2 x 3 x 4 x 5
# Reduce(function, data iterables)

a = [1,2,3,4,5]
from functools import reduce

# df = reduce(lambda x,y: x+y, a)
# print(df)

# ada data 1,2,3,4,5,6,7,8,9,10
# ada fungsi lambda x,y : x + y
# iterasi 1: 1 + 2
# iterasi 2: (1 + 2) + 3
# iterasi 3: ((1+2)+3) + 4
# iterasi 4: (((1+2)+3)+4) +5, dst

df = reduce(lambda x,y: 2*x+2*y, a)
print(df)
##########################
# berapa jumlah total dari bilangan ganjil yang telah dipangkat 3 dari 1 - 200

######## Class

# OOP = Object Oriented Programming

# Python - multi paradigma
# Procedural programming (data dijalankan dari atas ke bawah, per baris)

# OOP = Object = ketika kita akan membangun-mendevelop aplikasi

# Game: 
# karakter 1 - karakter 2 - karakter 3 - karakter 4 ....
# nama :
# tipe :
# defense :
# attack :

## Class - sejenis Blueprint - Template
# Class :
# instance - object nya

# Class : 
# Object itu punya 2 hal 
# 1. Attribut
# 2. Method

# Syntax dasar 
# class nama-kelas():
#     pass # agar tidak error

# class karyawan():
#     pass

# budi = karyawan()

# print(budi) # mendapat notif <_main_.karyawan object at ...

# class karyawan():
#     nama = 'nama'
#     gender = "gender"
#     def jabatan(): # kalau di luar tidak perlu argumen, tetapi di dalam fungsi class, harus ada argumen
#         print("jabatan saya manager")
        
# class karyawan():
#     nama = 'nama'
#     gender = "gender"
#     def jabatan(self): # diprint None 
#         print("jabatan saya manager")
    
# class karyawan():
#     nama = 'nama'
#     gender = "gender"
#     def jabatan(self): # diprint None 
#         print(self.nama, "jabatan saya manager")

# class karyawan():
#     nama = 'nama'
#     gender = "gender"
#     def __init__(self): # langsung keluar pesan sendiri
#         print("inisialisasi")
#     def jabatan(self, level):
#         print(self.nama, "jabatan saya manager", level)

class karyawan():
    def __init__(self, _nama, _gender): 
        self.nama = _nama
        self.gender = _gender
    def jabatan(self, level):
        print(self.nama, "jabatan saya manager", level)

# budi = karyawan() 
# budi.nama = "Budi Sugiarto"
# budi.gender = "Pria"
# print(budi.nama) # diprint Budi Sugiarto
# print(budi.gender) # diprint Budi Sugiarto
# # print(budi.jabatan()) # diprint None 
# budi.jabatan() # diprint Budi Sugiarto jabatan saya manager

# budi.jabatan("Senior") 

class karyawan():
    def __init__(self, _nama, _gender, _gaji): 
        self.nama = _nama
        self.gender = _gender
        self.gaji = _gaji
    def jabatan(self, level):
        print(self.nama, "jabatan saya manager", level)

# budi = karyawan() # error

budi = karyawan("Budi Sugiarto", "Pria", 9000000)

print(budi.gaji)

###### Team Assignment
#### Kelompok 2 - 3 orang

# Ketika di run awal :
# MENU -
# Login dan Register

# Register 
# Masukkan data 
# USER ID : ..... (harus kombinasi huruf dan angka) === lakukan pengecekan duplikasi Tidak boleh ada user ID yang sama
# Password : ... (harus gabungan huruf kapital, huruf kecil dan angka, minimal 8 karakter)
# Email : .... (lakukan verifikasi email)
# Ketentuan valid dan tidak valid sesuai tugas sebelumnya 

# Nama : ...
# Email : ...
# Gender : ...
# Usia : ...
# Pekerjaan : ...
# Hobi : (isi lebih dari satu)
# Alamat : ...
# Nama kota : ...
# RT : ...
# RW : ...
# Zip Code : ...
# Geo : Lat - Langitude
# No HP : ....

# Simpan (Y/N)
# -- kalau Y : Data tersimpan
# -- kalau N : Data tidak tersimpan

# Baik Y atau N == Kembali ke menu awal

# Login
# Register

# - Login
# Masukkan ID dan Password == Lakukan pengecekan ID dan Password
# ## ID salah atau Password salah atau Tidak Terdaftar
# - Anda Berhasil Login

# ### MENU UTAMA

# 1. Data Personal 
# di klik : keluar data Personal
# Data Anda adalah :
# Nama : ...
# Email : ...
# Gender : ...
# Usia : ...
# Pekerjaan : ...
# Hobi : (isi lebih dari satu)
# Alamat : ...
# Nama kota : ...
# RT : ...
# RW : ...
# Zip Code : ...
# Geo : Lat - Langitude
# No HP : ....

# 2. Konversi Kode Morse
# 3. Kalkulator
# 4. Konversi Romawi
# 5. Hitung hari # masukkan hari terus angka, 100 hari dari hari ini adalah ...
# 6. Kamus Hari (ENG - IND & IND - ENG) # Auto Detect, user tidak input pilih translasi IND-ENG atau ENG-IND
# 7. Manipulasi Karakter : (atau bisa kalian ganti dengan project lain)
# 8. Konversi jumlah hari (dari inputan ubah ke tahun, bulan, minggu, hari)
# 9. Nilai faktorial
# 10. Jumlah angka Fibonacci (sesuai inputan user) misal: user input 7 (jumlah 7 deret pertama bilangan fibonacci dan keluarkan deretnya)
# 11. Data USER === menampilkan user ID dan Password serta email dari seluruh data yang ada
# 12. Menu CRUD:
# opsi:
# Nama barang dan Stok = Gudang
# Nama barang dan harga = Toko-kasir 
# Nama karyawan dan gaji = Penggajian
# Nama Mahasiswa dan nilai = Kampus

# ** Optional : Boleh tambahkan fungsi lain 
# *** Coba gunakan Def, Lambda, filter, reduce dan map 
# **** Kirim Email : Deadline nya 31 Mei 2020